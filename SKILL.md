---
name: jaws-accessibility
description: Accessibility engineering for web products with JAWS/NVDA testing and Spain/EU compliance scoping. Use for WCAG 2.2 implementation, ARIA and keyboard/focus behavior, screen-reader regressions, audits, remediation plans, or web-accessibility scope checks under Ley 11/2023, RD 1112/2018, RD 193/2023, the EAA, and EN 301 549. Do NOT use for native mobile apps, PDF accessibility, or non-web content.
---

# JAWS Accessibility Skill

Provide practical, implementation-first support for accessible web interfaces and accessibility audits.

Use progressive disclosure. Load only the reference file needed for the current task.

## Reference Routing

| Situation | File to load |
|---|---|
| Legal scope, obligations, timelines, exemptions | `references/spanish-eu-legislation.md` |
| Priority WCAG 2.2 patterns and links to the complete normative matrix | `references/wcag-22-criteria.md` |
| JAWS/NVDA behavior differences, ARIA compatibility, anti-patterns | `references/jaws-nvda-compatibility.md` |
| End-to-end audit execution and reporting | `references/jaws-audit-methodology.md` |
| WCAG 3.0 monitoring and future planning | `references/future-standards.md` |

PDF accessibility is outside this skill's testing scope. If a web audit includes published PDFs, route those files to a dedicated PDF-accessibility methodology or specialist. Keep them in the product inventory and record **NOT TESTED** until that separate evaluation is complete; never infer PDF/UA or WCAG conformance from a browser or screen-reader spot check.

## Operating Rules

1. Prioritize native HTML semantics before ARIA.
2. Treat WCAG 3.0 as non-normative draft guidance, not a compliance baseline.
3. If legal/compliance is requested, state exact dates and legal scope explicitly.
4. Distinguish mandatory requirements from recommended best practices.
5. Validate with at least:
   - JAWS + Chrome
   - NVDA + Firefox
   For a formal or full audit, record the complete environment described in `references/jaws-audit-methodology.md`. If either reader is unavailable, continue with code, keyboard, accessibility-tree, and automated checks, but label the screen-reader result as **NOT TESTED**; never infer a pass.
6. For SPA flows, always verify:
   - focus placement after route changes
   - meaningful page title updates
   - announcement behavior for status changes
7. When uncertain about AT/browser behavior, request or document the exact JAWS/NVDA/browser versions.

## Delivery Format

For implementation tasks:
- explain user impact
- identify the root cause
- provide a minimal fix
- add a quick manual test script for keyboard + JAWS + NVDA

For audit tasks:
- use the 8-phase flow in `references/jaws-audit-methodology.md`
- group findings by severity: Critical, High, Medium, Low
- map each finding to WCAG SC, technical evidence, reproduction steps, and remediation
- use only `PASS`, `FAIL`, `NOT TESTED`, or `NOT APPLICABLE` for evaluation results; do not turn missing evidence into a pass

For legal/compliance scope questions:
- start with `references/spanish-eu-legislation.md`
- clarify whether the case is private-sector or public-sector
- mark legal interpretation as operational guidance, not legal advice

## Known Compatibility Risks

Screen readers regress often. Unless you have verified a specific JAWS/browser/version combination yourself, do not present version-specific quirks as guaranteed facts.

High-risk patterns:
- grids and complex tables where meaning depends only on ARIA state
- `aria-current`, `aria-description`, or `aria-roledescription` used as the only carrier of critical information
- live-region announcements injected too late
- SPA navigation without explicit focus management

Mitigation:
- do not rely on one ARIA attribute alone for critical meaning
- provide visible and textual redundancy
- resolve standards questions against HTML, WAI-ARIA, WCAG, and platform accessibility mappings; no screen reader is a conformance oracle
- document exact AT/browser versions when behavior differs

## Most Frequent Critical Errors

| Error | Impact | Solution |
|---|---|---|
| `aria-hidden="true"` on a container with focusable descendants | Silent focusable "ghost" elements | Use `display:none`, `visibility:hidden`, or remove focusability |
| Nested interactive elements | Repeated or confusing announcements | Use one interactive control with the correct semantic role |
| Data table or grid with weak semantics | Headers and state may not be exposed reliably | Use correct table/grid semantics and test in JAWS and NVDA |
| Live region created and populated at the same time | Announcement may be skipped | Render the live region container first, then update its contents |
| SPA route changes without focus management | Focus stays behind or becomes unclear | Move focus to the new page heading or landmark |
| Removed visible focus styles | Keyboard users lose orientation | Keep visible focus indicators |
| Competing announcement mechanisms | Double or inconsistent speech output | Separate live-region and descriptive text responsibilities |

## Quick Checklist

Before delivering any web component:

1. Is all functionality operable with keyboard only?
2. Do interactive elements have clear accessible names?
3. Is text contrast >= 4.5:1 and UI element contrast >= 3:1, subject to the applicable WCAG exceptions?
4. Do pointer targets satisfy WCAG 2.5.8 (24x24 CSS px or an allowed spacing/exception), with 44x44 as a usability target where practical?
5. Do images have correct `alt` behavior?
6. Does the page have `<html lang>` and logical headings?
7. Do forms have labels, errors, and appropriate `autocomplete`?
8. Do modals trap focus and return it to the trigger on close?
9. Do live regions exist in initial HTML?
10. Has it been tested with JAWS + Chrome and NVDA + Firefox, or explicitly marked **NOT TESTED** with those readers?

## Common Implementation Priorities

1. Keyboard operability and visible focus
2. Name/Role/Value integrity
3. Robust form labels, errors, and instructions
4. Focus management in dialogs, menus, and SPAs
5. Accessible tables, status messages, and live regions
6. Touch target size and alternative input methods

## Escalation Points

Escalate risk when:
- a component works in one reader but fails in the other
- compliance claims rely only on automated tools
- focus is lost, trapped, or visually hidden
- live-region behavior is not deterministic
- a legal answer depends on sector-specific enforcement details

## Maintaining This Skill

When changing this skill, keep `SKILL.md` as the router and put detailed procedures in the routed references. Validate the canonical directory before installing it:

```powershell
python C:\Users\Tecnología\.codex\skills\.system\skill-creator\scripts\quick_validate.py .
python scripts\validate_skill_content.py .
python -m unittest discover -s tests -p "test_*.py"
```

The semantic validator covers critical command mappings, standards status, legal definitions, audit evidence, official-source links, and synchronization. Structural validation alone is not evidence that the guidance is correct.
