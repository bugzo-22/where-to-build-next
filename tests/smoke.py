#!/usr/bin/env python3
"""Smoke tests for Where to Build Next — validates company data in index.html."""

import re
import sys
import os

html_path = os.path.join(os.path.dirname(__file__), '..', 'index.html')

try:
    with open(html_path, 'r') as f:
        html = f.read()
except FileNotFoundError:
    print(f'FAIL: Could not read {html_path}')
    sys.exit(1)

errors = []
warnings = []

# --- Extract COMPANIES block ---
companies_match = re.search(r'const COMPANIES = \[(.*?)\];\s*\n', html, re.DOTALL)
if not companies_match:
    print('FAIL: Could not find COMPANIES array in index.html')
    sys.exit(1)

companies_block = companies_match.group(1)

# --- Parse company objects by matching braces ---
company_blocks = []
depth = 0
start = -1
for i, ch in enumerate(companies_block):
    if ch == '{':
        if depth == 0:
            start = i
        depth += 1
    elif ch == '}':
        depth -= 1
        if depth == 0 and start != -1:
            company_blocks.append(companies_block[start:i+1])
            start = -1


def parse_field(block, field):
    """Extract a field value from a JS object literal string."""
    # Match field: "value"
    m = re.search(rf'{field}:\s*"((?:[^"\\]|\\.)*)"', block, re.DOTALL)
    if m:
        return m.group(1)
    # Match field: 'value'
    m = re.search(rf"{field}:\s*'((?:[^'\\]|\\.)*)'", block, re.DOTALL)
    if m:
        return m.group(1)
    # Match field: null
    m = re.search(rf'{field}:\s*null\b', block)
    if m:
        return None
    # Match field: "" (empty string)
    m = re.search(rf'{field}:\s*""', block)
    if m:
        return ''
    return '__MISSING__'


REQUIRED_FIELDS = [
    'id', 'name', 'color', 'emoji', 'oneliner', 'fund', 'stage',
    'raised', 'location', 'founders', 'product', 'thesis', 'numbers', 'category'
]
VALID_CATEGORIES = {'ai', 'energy', 'devtools', 'security', 'other'}

companies = []
for block in company_blocks:
    company = {}
    for field in REQUIRED_FIELDS + ['careers', 'valuation']:
        company[field] = parse_field(block, field)
    companies.append(company)

if len(companies) == 0:
    errors.append('No companies parsed from COMPANIES array')

# --- Check 1: Required fields ---
for c in companies:
    name = c.get('name') or c.get('id') or '(unknown)'
    for field in REQUIRED_FIELDS:
        val = c.get(field)
        if val == '__MISSING__':
            errors.append(f'{name}: missing required field "{field}"')
        elif val == '':
            errors.append(f'{name}: empty required field "{field}"')

# --- Check 2: Duplicate IDs ---
ids = [c['id'] for c in companies if c.get('id') and c['id'] != '__MISSING__']
seen = set()
dupes = set()
for id_ in ids:
    if id_ in seen:
        dupes.add(id_)
    seen.add(id_)
if dupes:
    errors.append(f'Duplicate company IDs: {", ".join(sorted(dupes))}')

# --- Check 3: Valid categories ---
for c in companies:
    name = c.get('name', '(unknown)')
    cat = c.get('category')
    if cat and cat != '__MISSING__' and cat not in VALID_CATEGORIES:
        errors.append(f'{name}: invalid category "{cat}" (expected: {", ".join(sorted(VALID_CATEGORIES))})')

# --- Check 4: Careers URLs ---
for c in companies:
    name = c.get('name', '(unknown)')
    careers = c.get('careers')
    if careers and careers not in ('__MISSING__', None) and not careers.startswith('https://'):
        errors.append(f'{name}: careers URL does not start with https:// ("{careers}")')

# --- Check 5: Non-empty locations ---
for c in companies:
    name = c.get('name', '(unknown)')
    loc = c.get('location')
    if loc is not None and loc != '__MISSING__' and loc.strip() == '':
        errors.append(f'{name}: location is empty')

# --- Check 6: Airtable form URL ---
airtable_match = re.search(r'const AIRTABLE_FORM = "([^"]*)"', html)
if not airtable_match:
    errors.append('AIRTABLE_FORM constant not found')
elif not airtable_match.group(1).startswith('https://airtable.com/'):
    errors.append(f'AIRTABLE_FORM URL looks invalid: "{airtable_match.group(1)}"')

# --- Check 7: Company count sanity ---
if len(companies) < 10:
    warnings.append(f'Only {len(companies)} companies found — expected at least 10')

# --- Report ---
print(f'\nSmoke Test Results')
print('=' * 40)
print(f'Companies found: {len(companies)}')
categories_used = sorted(set(c.get('category', '') for c in companies if c.get('category') and c['category'] != '__MISSING__'))
print(f'Categories used: {", ".join(categories_used)}')

if warnings:
    print(f'\nWarnings ({len(warnings)}):')
    for w in warnings:
        print(f'  !  {w}')

if errors:
    print(f'\nErrors ({len(errors)}):')
    for e in errors:
        print(f'  x  {e}')
    print(f'\nRESULT: FAIL')
    sys.exit(1)
else:
    print(f'\nAll checks passed.')
    print(f'RESULT: PASS')
    sys.exit(0)
