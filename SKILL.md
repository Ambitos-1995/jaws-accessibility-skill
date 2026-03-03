---
name: jaws-accessibility
description: Accessibility engineering skill for web products with JAWS and NVDA testing plus Spain/EU compliance guidance. Use when the task involves WCAG 2.2 implementation, ARIA behavior, keyboard/focus issues, screen-reader regressions, accessibility audits, remediation plans, or legal scope checks for Ley 11/2023, RD 1112/2018, EAA, and EN 301 549.
---

# JAWS Accessibility Skill

Provide practical, implementation-first support for accessible web interfaces and accessibility audits.

Use progressive disclosure. Load only the reference file needed for the current task.

## Reference routing

| Situation | File to load |
|---|---|
| Legal scope, obligations, timelines, exemptions | `references/spanish-eu-legislation.md` |
| WCAG 2.2 criteria mapping and coding patterns | `references/wcag-22-criteria.md` |
| JAWS/NVDA behavior differences, ARIA compatibility, anti-patterns | `references/jaws-nvda-compatibility.md` |
| End-to-end audit execution and reporting | `references/jaws-audit-methodology.md` |
| WCAG 3.0 monitoring and future planning (non-normative) | `references/future-standards.md` |

## Operating rules

1. Prioritize native HTML semantics before ARIA.
2. Treat WCAG 3.0 as non-normative draft guidance, not a compliance baseline.
3. If legal/compliance is requested, state exact dates and legal scope explicitly.
4. Distinguish mandatory requirements from recommended best practices.
5. Validate with at least:
   - JAWS + Chrome
   - NVDA + Firefox
6. For SPA flows, always verify:
   - focus placement after route changes
   - meaningful page title updates
   - announcement behavior for status changes
7. When uncertain about AT/browser version behavior, request or document exact versions.

## Delivery format

For implementation tasks:
- Explain the user impact.
- Identify the root cause (markup, state management, ARIA, focus, timing).
- Provide a minimal fix.
- Add a quick manual test script for keyboard + JAWS + NVDA.

For audit tasks:
- Use the 8-phase flow in `references/jaws-audit-methodology.md`.
- Return findings grouped by severity: Critical, High, Medium, Low.
- Map each finding to WCAG SC, technical evidence, reproduction steps, remediation recommendation.

For legal/compliance scope questions:
- Start with `references/spanish-eu-legislation.md`.
- Clarify whether the question is private-sector (Ley 11/2023 / EAA) or public-sector (RD 1112/2018).
- Mark any legal interpretation as operational guidance, not legal advice.

## Known bugs by JAWS version

Screen readers have frequent regressions. See `references/jaws-nvda-compatibility.md` section 9 for full context.

### JAWS 2025
- **`aria-current` silenced in grids**: `role="row"` inside a `grid` — JAWS may ignore `aria-current`.
- **`aria-description` ignored in grid rows**: same context causes `aria-description` not to be exposed.
- **`aria-roledescription` regressions**: fixed 2024 excessive repetition, but now may silence state metadata in grid rows.

### JAWS 2026 betas
- **Conditional silencing in `role="row"` + `grid`**: ongoing inconsistencies vs JAWS 2024 and NVDA.

### Mitigation
- Do not rely solely on `aria-current` or `aria-description` for critical information in grids.
- Provide visual and textual redundancy.
- Use NVDA as the strict standards-compliance reference.

## Most frequent critical errors

| Error | Impact | Solution |
|---|---|---|
| `aria-hidden="true"` on container with focusable elements | Silent "ghost elements" in JAWS | Use `display:none` or `visibility:hidden`, or remove `tabindex` from children |
| Nesting interactive elements (`<a><button>`) | JAWS reads the name 3 times | Single interactive element with correct role |
| Data table without `role="table"` or `role="grid"` | JAWS classifies as "layout table", silences `<th>` | Declare `role="table"` or `role="grid"` explicitly |
| Injecting `aria-live` with content simultaneously | JAWS ignores the live region | Empty container with `aria-live` in initial HTML |
| SPA without focus management after navigation | Focus trapped on originating link | Move focus to `<h1>` with `tabindex="-1"` + `.focus()` |
| `*:focus { outline: none }` | Keyboard users lose visual reference | Always define visible focus styles |
| `aria-live` + `aria-describedby` on same element | Double announcement in JAWS and NVDA | Separate into distinct DOM nodes |

## Quick checklist

Before delivering any web component:

1. Is all functionality operable with keyboard only?
2. Do interactive elements have clear accessible names?
3. Is text contrast >= 4.5:1 and UI element contrast >= 3:1?
4. Are touch targets at least 24x24px CSS?
5. Do images have descriptive `alt` (or `alt=""` if decorative)?
6. Does the page have `<html lang="...">` and use `<h1>`-`<h6>` in logical order?
7. Do forms have associated `<label>` elements and appropriate `autocomplete`?
8. Do modals trap focus and return it to the trigger on close?
9. Do live regions exist empty in the initial HTML?
10. Has it been tested with JAWS + Chrome and NVDA + Firefox?

## Common implementation priorities

1. Keyboard operability and visible focus.
2. Name/Role/Value integrity for interactive controls.
3. Robust form labels, errors, and instructions.
4. Focus management in dialogs, menus, and SPAs.
5. Accessible tables, status messages, and live regions.
6. Touch target size and alternative input methods.

## Escalation points

Escalate risk when:
- A component works in one reader but fails in the other.
- Compliance claims rely only on automated tools.
- Focus is lost, trapped, or visually hidden.
- `aria-live` is used without deterministic announcement behavior.
- A legal answer depends on sector-specific enforcement details.
