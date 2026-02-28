---
name: smoke-test
description: Run smoke tests to validate company data and visual layout before publishing
disable-model-invocation: true
allowed-tools: Bash, Read, Grep
---

# Smoke Test: Where to Build Next

Run a two-phase smoke test to validate changes before merging to main.

## Phase 1 — Data Validation

Run the data validation script:

```
/usr/bin/python3 tests/smoke.py
```

Report the results. If any errors are found, list them clearly and stop — do not proceed to Phase 2 until data issues are fixed.

## Phase 2 — Visual / Layout Validation

Open `index.html` in the browser and verify the following:

### Main page checks:
1. **Header**: "Where to Build Next" title is visible and centered at top
2. **Search bar**: Text input is visible below the header
3. **Category filters**: Filter buttons (All Companies, AI / ML, Energy, Dev Tools, Security, Fintech) are visible
4. **Stats bar**: Shows company count, hiring count, and early stage count
5. **Company grid**: Cards render in a 2-column grid on desktop, each with emoji, name, stage badge, location badge, and oneliner
6. **Footer**: "Felicis Ventures" footer text at the bottom

### Company detail checks:
1. Click into any company card
2. Verify: company name with emoji, colored left border, stage/raised/location badges visible
3. Verify: "View Open Roles" button (if company has careers link) and "I'm Interested" button are present
4. Verify: 4 info sections render (What They're Building, Founding Team, Why This Matters, Key Numbers)
5. Verify: "Back to all companies" link works
6. Verify: bottom CTA section with buttons is present

### Mobile responsiveness:
1. Resize browser to mobile width (~375px)
2. Verify cards stack into a single column
3. Verify text is readable and not cut off
4. Verify buttons are tappable size

Report a summary of all checks with pass/fail status.
