# JAWS And NVDA Compatibility Guide

Last reviewed: 2026-08-31

## Core Position

Always test with both:
- JAWS + Chrome
- NVDA + Firefox

Treat both as real user agents with different browser/platform mappings and heuristics. Resolve conformance questions against normative HTML, WAI-ARIA, and WCAG requirements rather than declaring either reader a standards oracle.

## Practical Differences

| Aspect | JAWS | NVDA |
|---|---|---|
| General behavior | Uses a virtual buffer plus product-specific heuristics | Uses browse/focus modes and browser accessibility mappings |
| Recommended audit pairing | Chrome (and Edge when relevant to the audience) | Firefox (and Chrome when relevant to the audience) |
| Risk profile | Product heuristics and AI-generated labels can conceal authoring defects during informal use | Different mappings can expose different defects; a pass here still does not prove conformance |

## High-Risk Patterns

These are common cross-reader failure zones:
- grids and complex tables
- custom widgets with weak semantics
- late-inserted live regions
- SPA route changes without focus management
- `aria-hidden` combined with focusable descendants
- labels or instructions carried only by ARIA when visible text is absent

## Preferred Patterns

### Labels

Prefer:
- `<label for>`
- `aria-labelledby` when combining multiple visible text sources
- `aria-describedby` for hints and errors

Avoid:
- placeholder-only labeling
- title-only labeling
- relying on `aria-description` as the sole explanation channel

### Live Regions

Prefer:
- an empty live-region container in initial HTML
- later text updates into that existing node

Avoid:
- creating and populating the live region in the same step
- nested or competing live regions

### Tables And Grids

Prefer:
- native table markup where possible
- explicit header relationships
- visible redundancy for critical status information

Avoid:
- assuming one ARIA state will be announced the same way in both readers

### SPA Navigation

Always verify:
- title updates
- focus moved to the new main heading or landmark
- status messages announced deterministically

## Audit Notes

When documenting a bug:
1. record exact AT version
2. record browser version
3. record whether the issue reproduces in both readers
4. describe expected announcement vs actual announcement
5. reference the full environment record from `jaws-audit-methodology.md`, including keyboard layout, voice/Braille settings, AI Labeler, custom labels, and UIA mode

## Recommendation

If behavior appears version-specific, treat it as a test finding, not as universal truth, unless you have current vendor documentation or direct reproduction evidence.

For JAWS 2026, disable or account for AI Labeler/custom labels when testing author-provided accessible names; otherwise a generated label can make an inaccessible control appear usable without fixing the page. Record whether AI features, custom labels, and browser UIA mode were enabled.

## Sources

- Freedom Scientific web-navigation training: https://support.freedomscientific.com/SurfsUp/5-Navigating.htm
- JAWS 2026 release notes: https://support.freedomscientific.com/Downloads/JAWS/JAWSWhatsNew?version=2026
- NVDA stable user guide: https://download.nvaccess.org/releases/stable/documentation/en/userGuide.html
- WAI-ARIA Authoring Practices: https://www.w3.org/WAI/ARIA/apg/
