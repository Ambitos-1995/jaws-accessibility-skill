# JAWS Audit Methodology

Last reviewed: 2026-03-03

## TOC

1. Environment setup
2. Essential JAWS commands
3. Pre-audit: automated scan
4. Manual audit: 8-phase JAWS testing flow
5. Cross-validation with NVDA
6. Severity model
7. Report template
8. CI/CD integration

---

## 1. Environment setup

### Required software

| Component | Version | Notes |
|---|---|---|
| JAWS | 2025 or latest stable | Avoid beta versions for formal audits |
| NVDA | Latest stable | Cross-validation reference |
| Chrome | Latest stable | Primary browser for JAWS |
| Firefox | Latest stable | Primary browser for NVDA |
| axe DevTools | Latest | Chrome extension for automated pre-scan |

### JAWS configuration for auditing

1. **Reset to defaults**: Settings Center → File → Reset All Settings. This ensures consistent baseline behavior.

2. **Verbosity level**: Set to **Intermediate** for auditing (not Beginner or Advanced).
   - Settings Center → Speech → Verbosity → Intermediate

3. **Punctuation level**: Set to **Most** to hear ARIA attributes being announced.
   - Settings Center → Speech → Punctuation → Most

4. **Virtual cursor settings**:
   - Settings Center → Web / HTML / PDF → Virtual Cursor
   - Enable "Auto Forms Mode" → ON
   - Enable "Auto Virtual Cursor for Web Content" → ON

5. **Sound scheme**: Enable sounds to distinguish modes.
   - A rising tone indicates switch to Forms Mode
   - A falling tone indicates switch to Browse Mode

### Browser configuration

- **Chrome**: Disable extensions that may interfere (ad blockers can hide content from AT).
- **Chrome accessibility flag**: Navigate to `chrome://accessibility` and ensure "native accessibility API" is active.
- **Zoom**: Set to 100% for baseline testing; test again at 200% for WCAG 1.4.10 Reflow.

---

## 2. Essential JAWS commands

### Navigation (Browse Mode)

| Command | Action |
|---|---|
| **↑ / ↓** | Read previous / next line |
| **H / Shift+H** | Next / previous heading |
| **1-6** | Next heading at level 1-6 |
| **T / Shift+T** | Next / previous table |
| **F / Shift+F** | Next / previous form field |
| **B / Shift+B** | Next / previous button |
| **K / Shift+K** | Next / previous link |
| **D / Shift+D** | Next / previous landmark region |
| **R / Shift+R** | Next / previous ARIA region |
| **I / Shift+I** | Next / previous list item |
| **G / Shift+G** | Next / previous graphic |

### Listings and overviews

| Command | Action |
|---|---|
| **Insert + F5** | List all form fields on page |
| **Insert + F6** | List all headings on page |
| **Insert + F7** | List all links on page |
| **Insert + F3** | Virtual HTML features list (all elements) |
| **Insert + F9** | List all frames |
| **Ctrl + Insert + T** | List all tables |

### Interaction

| Command | Action |
|---|---|
| **Enter** | Activate link / button |
| **Space** | Activate button / toggle checkbox |
| **Insert + Z** | Toggle Forms Mode on/off |
| **Insert + Space** | Toggle virtual cursor on/off |
| **Escape** | Exit Forms Mode / close dialog |
| **Ctrl** | Stop speech |
| **Insert + ↓** | Read from current position (Say All) |

### Table navigation (inside a table)

| Command | Action |
|---|---|
| **Ctrl + Alt + →** | Next cell in row |
| **Ctrl + Alt + ←** | Previous cell in row |
| **Ctrl + Alt + ↓** | Next cell in column |
| **Ctrl + Alt + ↑** | Previous cell in column |
| **Ctrl + Alt + 5 (NumPad)** | Read current cell |
| **Insert + Shift + T** | Announce column headers |

---

## 3. Pre-audit: automated scan

Before manual testing, run automated tools to catch the "low-hanging fruit" (~30-50% of issues):

### Step 1: axe DevTools scan
1. Open the page in Chrome.
2. Open DevTools → axe DevTools tab.
3. Run "Scan All of My Page."
4. Export results as CSV or JSON.
5. Focus on **Critical** and **Serious** issues.

### Step 2: Lighthouse accessibility audit
1. DevTools → Lighthouse tab.
2. Select "Accessibility" category only.
3. Run audit.
4. Score below 90 indicates significant issues.

### Step 3: Heading structure check
1. Install HeadingsMap extension.
2. Verify heading hierarchy is logical (`h1` → `h2` → `h3`, no skips).
3. Verify each page has exactly ONE `<h1>`.

### What automated tools CANNOT catch
- Logical focus order (only whether focus exists)
- Quality of alt text (only whether it exists)
- Correct use of live regions (only whether `aria-live` exists)
- Whether screen reader announcements make sense in context
- Whether the user experience is actually usable

---

## 4. Manual audit: 8-phase JAWS testing flow

### Phase 1: Page Load
1. **Load the page with JAWS active.**
2. Verify: Does JAWS announce the page title?
3. Verify: Is the language announced correctly? (Should match `<html lang="...">`.)
4. Press **Insert + F6**: Check heading structure.
5. Press **D**: Navigate through landmarks. Verify `<header>`, `<nav>`, `<main>`, `<footer>` are announced.

### Phase 2: Skip Link
1. Press **Tab** once from page load.
2. Verify: "Skip to main content" link is the first focusable element.
3. Press **Enter** on skip link.
4. Verify: Focus moves to `<main>` or `<h1>` of content area.

### Phase 3: Navigation
1. Navigate all menu items with **Tab** and **Arrow keys**.
2. Verify: All items are announced with their role ("link," "button," "menu item").
3. If dropdown menu:
   - Verify: `aria-expanded` is announced ("collapsed" / "expanded").
   - Verify: Submenu items are reachable with arrow keys.
   - Verify: **Escape** closes submenu and returns focus to trigger.

### Phase 4: Content
1. Press **H** to navigate through all headings.
2. Verify: Heading hierarchy is logical and announced correctly.
3. Navigate to images with **G**.
4. Verify: Decorative images are silent. Informative images have descriptive alt text announced.
5. Navigate to links with **K**.
6. Verify: Link text is descriptive (not "click here" or "read more" without context).
7. Navigate to lists with **I**.
8. Verify: JAWS announces "list of N items."

### Phase 5: Forms
1. Navigate to form with **F** (next form field).
2. Verify: Each field's label is announced when focused.
3. Enter invalid data and submit.
4. Verify: Error messages are announced (via `role="alert"` or `aria-live`).
5. Verify: `aria-invalid="true"` is announced on the erroneous field.
6. Verify: `aria-describedby` links the error message to the field.
7. Check `autocomplete` attributes with **Insert + F5** (form field list).

### Phase 6: Interactive Components
1. **Modals**: Open modal, verify focus is trapped inside, verify Escape closes, verify focus returns to trigger.
2. **Tabs**: Navigate with arrow keys, verify `aria-selected` is announced, verify tab panel content changes.
3. **Accordions**: Verify `aria-expanded` state changes, verify content is reachable after expanding.
4. **Carousels**: Verify controls are keyboard accessible, verify auto-play can be paused, verify current slide is announced.

### Phase 7: Dynamic Content
1. Trigger dynamic content updates (e.g., search results, notifications, loading states).
2. Verify: Live region announces the update without requiring focus change.
3. Verify: `aria-live="polite"` does not interrupt current speech.
4. Verify: `aria-live="assertive"` is used only for critical alerts.

### Phase 8: SPA Navigation
1. Click a client-side navigation link.
2. Verify: New page title/heading is announced (via Route Announcer or custom solution).
3. Verify: Focus moves to the `<h1>` of the new content.
4. Press browser **Back** button.
5. Verify: Previous page is announced and focus is managed.

---

## 5. Cross-validation with NVDA

After completing the JAWS audit, repeat key tests with NVDA + Firefox:

### Priority tests for NVDA
1. **ARIA attributes**: NVDA follows the spec strictly. Issues missed by JAWS's heuristic compensation will surface.
2. **Live regions**: Test all dynamic content announcements.
3. **Table semantics**: Verify headers are announced correctly.
4. **Form validation**: Verify error messages are associated and announced.
5. **Custom widgets**: Test modals, tabs, accordions — NVDA mode switching differs from JAWS.

### NVDA-specific commands

| Command | Action |
|---|---|
| **Insert + Space** | Toggle Browse/Focus mode |
| **Insert + F7** | Elements list (links, headings, landmarks, form fields) |
| **Insert + F5** | Elements list (all) |
| **Ctrl** | Stop speech |

---

## 6. Severity model

| Severity | Definition | Example |
|---|---|---|
| **Critical** | Blocks access to core functionality; no workaround | Form cannot be submitted; modal traps focus permanently |
| **Major** | Significant barrier but workaround exists | Error messages not announced but visible; heading order broken |
| **Moderate** | Partial failure or degraded experience | Missing autocomplete attributes; low-contrast non-text elements |
| **Minor** | Inconvenience, does not block functionality | Decorative image has redundant alt text; link text could be more descriptive |

---

## 7. Report template

### Issue format

```markdown
## Issue: [Short description]

- **Finding ID**: [Sequential ID]
- **Severity**: Critical / Major / Moderate / Minor
- **WCAG SC**: [X.X.X] — [Criterion name] (Level [A/AA])
- **Page/Component**: [URL or component name]
- **Element**: [CSS selector or description]
- **Screen reader**: JAWS 2025 / NVDA 2024.4 / Both
- **Browser**: Chrome 131 / Firefox 133

### Steps to reproduce
1. Navigate to [page]
2. Press [key sequence]
3. Expected: [what should happen]
4. Actual: [what happens instead]

### Root cause hypothesis
[Technical explanation: missing ARIA attribute, wrong role, DOM order issue, etc.]

### Recommended fix
[Specific code fix or pattern to implement]

### Tracking
- **Owner**: [Developer or team]
- **Target release**: [Sprint or date]
- **Retest status**: [Pending / Passed / Failed]
```

---

## 8. CI/CD integration

### Automated checks in pipeline

```yaml
# GitHub Actions example
accessibility-check:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4
    - run: npm ci
    - run: npm run build
    - name: Run axe-core tests
      run: npx playwright test --project=a11y
    - name: Run eslint jsx-a11y
      run: npx eslint --ext .tsx,.jsx src/ --rule 'jsx-a11y/...'
```

### Recommended test stack

| Tool | Catches | Integration |
|---|---|---|
| eslint-plugin-jsx-a11y | Missing labels, roles, alt text at code time | ESLint (pre-commit) |
| @axe-core/playwright | Runtime DOM issues: contrast, ARIA, keyboard | Playwright (CI) |
| pa11y | Full-page automated scan | CI pipeline |

### What CI cannot replace

Automated tools catch ~30-50% of accessibility issues. **Manual testing with JAWS + NVDA is irreplaceable** for:
- Focus order logic
- Screen reader announcement quality
- Live region behavior
- Complex widget usability
- SPA navigation experience
