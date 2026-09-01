# JAWS Audit Methodology

Last reviewed: 2026-08-31

## TOC

1. Environment setup
2. Essential JAWS commands
3. Pre-audit: automated scan
4. Manual audit: 8-phase JAWS testing flow
5. Cross-validation with NVDA
6. Severity model
7. Report template
8. CI/CD integration
9. Sources

---

## 1. Environment setup

### Required software

| Component | Version | Notes |
|---|---|---|
| JAWS | Latest stable supported release | Record the exact version/build; avoid beta versions for formal audits |
| NVDA | Latest stable supported release | Record the exact version/build; avoid snapshots for formal audits |
| Chrome | Latest stable | Primary browser for JAWS |
| Firefox | Latest stable | Primary browser for NVDA |
| axe DevTools | Latest | Chrome extension for automated pre-scan |

### Required environment record

Record this before testing. Reproduce the same environment on retest, or document the difference:

| Field | Required evidence |
|---|---|
| Operating system | Exact Windows edition, version, OS build, architecture, and relevant display scaling |
| Screen reader | Exact JAWS/NVDA release and build; stable/beta channel |
| Browser | Exact browser version and update channel |
| Keyboard | JAWS Desktop or Laptop layout; physical keyboard and NumPad availability |
| Speech | Voice/synthesizer, language, speech rate, punctuation, and verbosity |
| Braille | Display model, connection, translation table, and mode, or `NOT APPLICABLE` |
| JAWS personalization | Test profile, custom labels, Flexible Web rules, scripts, and personalized site settings |
| JAWS AI | AI Labeler and Page Explorer state; AI Labeler is enabled by default in JAWS 2026 |
| Browser accessibility path | Native browser accessibility path or JAWS native UIA early-adopter mode |
| Other inputs | Zoom, high contrast/forced colors, touch, switch, or voice input used in the scenario |

### JAWS configuration for auditing

1. **Preserve the user's configuration**: use a dedicated test profile or document the current settings. Do not reset a person's production configuration as part of an audit.

2. **Verbosity level**: Set to **Intermediate** for auditing (not Beginner or Advanced).
   - Settings Center → Speech → Verbosity → Intermediate

3. **Punctuation level**: Use a documented punctuation level appropriate to the content. Punctuation verbosity does not expose ARIA attributes; verify name, role, state, and description through actual announcements and the browser accessibility tree.
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
- **Chrome accessibility diagnostics**: Use `chrome://accessibility` only to inspect accessibility state when diagnosing a problem. Do not rely on a non-standard flag as an audit prerequisite.
- **Zoom**: Set to 100% for baseline testing; test text at 200% for WCAG 1.4.4 and reflow at an equivalent width of 320 CSS pixels (commonly 400% zoom at a 1280 CSS-pixel viewport) for WCAG 1.4.10.

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
| **Tab / Shift+Tab** | Next / previous focusable control or link |
| **U / Shift+U** | Next / previous unvisited link |
| **V / Shift+V** | Next / previous visited link |
| **K / Shift+K** | Next / previous PlaceMarker |
| **D / Shift+D** | Next / previous element of a different type |
| **R / Shift+R** | Next / previous region |
| **Q / Shift+Q** | Next / previous main region |
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
| **Enter** or automatic mode switching | Enter Forms Mode on an applicable control |
| **NumPad +** | Exit Forms Mode / activate the PC cursor in Desktop layout |
| **Insert + Z** | Toggle the virtual cursor |
| **Insert + Space** | Start a layered command; it is not a virtual-cursor toggle |
| **Escape** | Test a component's documented dismissal behavior; it is not the universal Forms Mode exit command |
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

### Table layer and Laptop layout

- Press **Insert + Space, T** in Desktop layout or **Caps Lock + Space, T** in Laptop layout to enter the Table Layer, then use arrow keys to move and the layout's current-cell command.
- In the JAWS Laptop layout, the JAWS key is normally **Caps Lock** instead of Insert. **Caps Lock + Semicolon** activates the PC cursor and is the no-NumPad equivalent used to leave Forms Mode. The documented Laptop table commands include **Alt+Shift+M** (previous cell), **Alt+Shift+Period** (next cell), **Alt+Shift+Y** (cell above), **Alt+Shift+N** (cell below), and **Alt+Shift+Comma** (current cell).
- Record which layout was used. Do not publish Desktop keystrokes as though they were universal.

---

## 3. Pre-audit: automated scan

Before manual testing, run automated tools to catch deterministic issues efficiently. Automated coverage varies by product and rule set; do not assign a universal percentage or infer conformance from a score.

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
4. Record individual failures. A Lighthouse score is not a WCAG conformance result, and no fixed score threshold proves or disproves conformance.

### Step 3: Heading structure check
1. Install HeadingsMap extension.
2. Verify heading hierarchy is logical (`h1` → `h2` → `h3`, no skips).
3. Verify headings communicate the page structure. Multiple `<h1>` elements are valid HTML and are not automatically a WCAG failure; assess whether the resulting hierarchy is meaningful and usable.

### What automated tools CANNOT catch
- Logical focus order (only whether focus exists)
- Quality of alt text (only whether it exists)
- Correct use of live regions (only whether `aria-live` exists)
- Whether screen reader announcements make sense in context
- Whether the user experience is actually usable

---

## 4. Manual audit: 8-phase JAWS testing flow

For site-wide audits, first follow the final **WCAG-EM 2.0 W3C Group Note published 2026-07-23**: define scope and target level, inventory page/component types and complete processes, select a representative sample (plus a documented random sample when appropriate), evaluate it, and report limitations. The phases below are the interaction script for each sampled page or flow; they are not a substitute for representative sampling.

### Phase 1: Page Load
1. **Load the page with JAWS active.**
2. Verify: Does JAWS announce the page title and useful orientation information? JAWS 2026 no longer starts reading the full page automatically by default, so absence of automatic Say All is not a failure.
3. Verify: Is the language announced correctly? (Should match `<html lang="...">`.)
4. Press **Insert + F6**: Check heading structure.
5. Press **R**: Navigate through regions. Use **Q** to locate the main region. Verify that the page exposes useful banner, navigation, main, and content-information regions where applicable.

### Phase 2: Skip Link
1. Press **Tab** once from page load.
2. Verify: the bypass mechanism is available at or near the start of the repeated content. A skip link is the common pattern, but WCAG 2.4.1 does not require one exact implementation or accessible name.
3. Press **Enter** on skip link.
4. Verify: Focus moves to `<main>` or `<h1>` of content area.

### Phase 3: Navigation
1. Navigate all site-navigation controls with **Tab**. Use **Arrow keys** only for composite widgets whose semantics and documented interaction pattern require them (for example a true ARIA menu), not for an ordinary list of navigation links.
2. Verify: All items are announced with their role ("link," "button," "menu item").
3. If the navigation uses a disclosure pattern, keep ordinary links in the Tab sequence and test Enter/Space and Escape according to the documented disclosure behavior. If it is a true composite `menu`/`menubar`, test the corresponding APG arrow-key pattern. Do not impose menu arrow keys on an ordinary navigation list merely because it has a dropdown.
4. If a true composite menu is present:
   - Verify: `aria-expanded` is announced ("collapsed" / "expanded").
   - Verify: Submenu items are reachable with arrow keys.
   - Verify: **Escape** closes submenu and returns focus to trigger.

### Phase 4: Content
1. Press **H** to navigate through all headings.
2. Verify: Heading hierarchy is logical and announced correctly.
3. Navigate to images with **G**.
4. Verify: Decorative images are silent. Informative images have descriptive alt text announced.
5. Navigate focusable links with **Tab / Shift+Tab** and browse unvisited/visited links with **U / V**.
6. Verify: Link text is descriptive (not "click here" or "read more" without context).
7. Navigate to lists with **I**.
8. Verify: JAWS announces "list of N items."
9. For prerecorded media with audio, verify synchronized captions and an adjacent transcript. Verify audio description or an equivalent alternative when meaningful visual information is not conveyed in the soundtrack.
10. If the page links to a PDF in the evaluation scope, inventory it and hand it to the dedicated PDF-accessibility evaluation. Record **NOT TESTED** until that evaluation returns evidence.

### Phase 5: Forms
1. Navigate to form with **F** (next form field).
2. Verify: Each field's label is announced when focused.
3. Enter invalid data and submit.
4. Verify: Error messages are announced (via `role="alert"` or `aria-live`).
5. Verify: `aria-invalid="true"` is announced on the erroneous field.
6. Verify: `aria-describedby` links the error message to the field.
7. Check `autocomplete` attributes with **Insert + F5** (form field list).
8. Confirm Forms Mode can be entered on applicable controls and exited with **NumPad +** in Desktop layout or **Caps Lock + Semicolon** in Laptop layout.

### Phase 6: Interactive Components
The following checks use native HTML behavior and common APG interaction patterns as implementation guidance. APG patterns are informative guidance, not additional WCAG success criteria. If a component differs from an APG example, report a WCAG failure only when the observed user impact fails a normative success criterion.

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
2. Verify: the document title changes and the user receives a deterministic indication of the new view through the framework announcer, focus strategy, or another tested mechanism.
3. Verify the product's documented focus strategy. Moving focus to the new `<h1>` is often effective, but it is not the only valid strategy and should not be imposed when it harms expected browser history or focus behavior.
4. Press browser **Back** button.
5. Verify: Previous page is announced and focus is managed.

After page-level checks, execute every complete process selected under WCAG-EM from start to finish. A process is not a `PASS` when only its individual pages or components were sampled.

---

## 5. Cross-validation with NVDA

After completing the JAWS audit, repeat key tests with NVDA + Firefox:

### Priority tests for NVDA
1. **ARIA attributes**: Compare the browser accessibility mappings and announcements in both readers. Different heuristics can expose different authoring defects; neither reader is a conformance oracle.
2. **Live regions**: Test all dynamic content announcements.
3. **Table semantics**: Verify headers are announced correctly.
4. **Form validation**: Verify error messages are associated and announced.
5. **Custom widgets**: Test modals, tabs, accordions — NVDA mode switching differs from JAWS.

### NVDA-specific commands

| Command | Action |
|---|---|
| **NVDA + Space** | Toggle Browse/Focus mode |
| **NVDA + F7** | Elements list (including links, headings, form fields, buttons, and landmarks as supported) |
| **NVDA + F5** | Refresh the browse-mode document; this is not an elements list |
| **Ctrl** | Stop speech |

---

## 6. Severity model

### Evaluation result vocabulary

Use one of these states for every requirement and sampled scenario:

| Result | Meaning |
|---|---|
| **PASS** | Sufficient evidence shows the requirement is met in the recorded scope and environment |
| **FAIL** | Reproducible evidence shows the requirement is not met |
| **NOT TESTED** | The required method, environment, specialist review, or evidence was unavailable |
| **NOT APPLICABLE** | The requirement does not apply, with a documented reason |

Do not use `PASS` for an automated-only check when the requirement needs manual or assistive-technology evidence. Severity describes the impact of a `FAIL`; it is separate from the result state.

| Severity | Definition | Example |
|---|---|---|
| **Critical** | Blocks core functionality or access to essential information; no reasonable workaround | Form cannot be submitted; modal traps focus permanently |
| **High** | Significant barrier in an important task, though a difficult workaround may exist | Required errors are not announced; primary navigation cannot be operated by keyboard |
| **Medium** | Partial failure or degraded experience | Missing autocomplete attributes; low-contrast non-text elements |
| **Low** | Limited inconvenience with little task impact | Decorative image has redundant alternative text; link wording could be clearer |

---

## 7. Report template

### Issue format

```markdown
## Issue: [Short description]

- **Finding ID**: [Sequential ID]
- **Severity**: Critical / High / Medium / Low
- **WCAG SC**: [X.X.X] — [Criterion name] (Level [A/AA])
- **Page/Component**: [URL or component name]
- **Element**: [CSS selector or description]
- **Result**: PASS / FAIL / NOT TESTED / NOT APPLICABLE
- **Environment ID**: [Reference to the complete environment record]
- **Screen reader**: [Exact JAWS/NVDA release and build, or NOT TESTED]
- **Browser**: [Exact browser version and channel]
- **Keyboard layout**: [JAWS Desktop/Laptop; physical keyboard and NumPad]
- **AI/personalization**: [AI Labeler, Page Explorer, UIA, custom labels, scripts, Flexible Web]

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
- **Retest result**: [PASS / FAIL / NOT TESTED / NOT APPLICABLE]
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

Automated tools cannot determine accessibility or establish WCAG conformance. **Manual testing with keyboard, JAWS, and NVDA remains necessary** for:
- Focus order logic
- Screen reader announcement quality
- Live region behavior
- Complex widget usability
- SPA navigation experience

## 9. Sources

- W3C WCAG-EM 2.0 Group Note, published 2026-07-23: https://www.w3.org/TR/wcag-em-2/
- WAI-ARIA Authoring Practices introduction (informative, not normative): https://www.w3.org/WAI/ARIA/apg/about/introduction/
- W3C guidance on evaluation-tool limits: https://www.w3.org/WAI/test-evaluate/tools/selecting/
- Freedom Scientific JAWS keystrokes, including HTML, Forms Mode, Table Layer, and Laptop layout: https://support.freedomscientific.com/content/html/jawshq/JAWS-Keystrokes.html
- Freedom Scientific Surf's Up web navigation: https://support.freedomscientific.com/SurfsUp/5-Navigating.htm
- Freedom Scientific Forms Mode: https://support.freedomscientific.com/SurfsUp/9-Forms.htm
- Freedom Scientific PlaceMarkers: https://support.freedomscientific.com/SurfsUp/15-PlaceMarkers.htm
- JAWS current releases and notes: https://support.freedomscientific.com/Downloads/JAWS/JAWSWhatsNew?version=2026
- NVDA stable user guide: https://download.nvaccess.org/releases/stable/documentation/en/userGuide.html
