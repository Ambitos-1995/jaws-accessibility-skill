# JAWS & NVDA Compatibility Guide

Last reviewed: 2026-03-03

## TOC

1. JAWS vs NVDA: Fundamental differences
2. Interaction modes
3. ARIA divergences
4. Tables
5. Forms
6. Modals and dialogs
7. Navigation in SPAs
8. Anti-patterns
9. Known bugs by version
10. Version log template

---

## 1. JAWS vs NVDA: Fundamental differences

| Aspect | JAWS (Freedom Scientific) | NVDA (NV Access) |
|---|---|---|
| **License** | Commercial (~$1,000/year) | Free / open source |
| **Engine** | Proprietary heuristics + custom virtual buffer | Strict W3C AAM interpretation |
| **Error tolerance** | High — tries to "fix" bad code | Low — exposes errors directly |
| **Market share** | ~40.5% primary (WebAIM Survey #10) | ~37.7% primary (WebAIM Survey #10) |
| **Best paired with** | Chrome (primary), Edge | Firefox (primary), Chrome |
| **Testing role** | "Real world" user experience | Standards compliance validation |

**Always test with both.** A component that works in JAWS may fail in NVDA because JAWS compensates for ARIA errors. NVDA exposes the actual accessibility tree as the browser constructs it.

---

## 2. Interaction modes

Both screen readers operate in two primary modes:

### Browse Mode (Virtual Cursor)
- Default mode when reading web content.
- User navigates with arrow keys, heading shortcuts (H), landmark shortcuts (D), etc.
- Screen reader intercepts keystrokes.

### Focus Mode (Forms Mode / Application Mode)
- Activated automatically when user enters a form field.
- Keystrokes pass directly to the web page.
- JAWS calls this "Forms Mode," NVDA calls it "Focus Mode."

### Mode switching behavior

| Trigger | JAWS | NVDA |
|---|---|---|
| Entering `<input>` | Auto-switches to Forms Mode | Auto-switches to Focus Mode |
| Entering `<select>` | Auto-switches | Auto-switches |
| `role="application"` | Forces Forms Mode on entire subtree | Forces Focus Mode on entire subtree |
| Leaving form field (Tab out) | Returns to Browse Mode | Returns to Browse Mode |
| Manual toggle | **Insert + Z** | **Insert + Space** |

### Critical warning: `role="application"`
Disables ALL virtual cursor navigation within that subtree. Only use for canvas-based apps or custom widgets with no web equivalent. **Never** on general page content.

---

## 3. ARIA divergences

### `aria-description` vs `aria-describedby`

| Feature | JAWS 2024/2025 | NVDA 2024+ |
|---|---|---|
| `aria-describedby` | Fully supported | Fully supported |
| `aria-description` | Inconsistent — may be ignored in grids/tables | Supported since 2023.1 |

**Recommendation**: Always use `aria-describedby` with a helper DOM node.

```html
<!-- GOOD: works in both -->
<button aria-describedby="btn-help">Submit</button>
<span id="btn-help" class="sr-only">Submitting will send your application. This cannot be undone.</span>

<!-- RISKY: may fail in JAWS -->
<button aria-description="Submitting will send your application.">Submit</button>
```

### `aria-current`

| Context | JAWS 2025 | NVDA |
|---|---|---|
| Navigation links | Announces "current page" | Announces "current" |
| Inside `role="grid"` rows | May be silenced | Works correctly |
| Breadcrumbs | Works | Works |

**Mitigation for grids**: Provide visual + textual redundancy. Don't rely solely on `aria-current` in grid contexts.

### `aria-live` regions

| Pattern | JAWS | NVDA |
|---|---|---|
| Container present empty, content injected later | Works | Works |
| Container AND content injected simultaneously | Ignored | May work inconsistently |
| `aria-live="assertive"` | Interrupts immediately | Interrupts immediately |
| `aria-live="polite"` | Queued after current speech | Queued after current speech |
| Nested live regions | Unpredictable | Unpredictable |

**Critical rule**: The `aria-live` container must exist in the initial HTML **empty**.

```html
<!-- In initial HTML (empty, waiting) -->
<div id="status" aria-live="polite" role="status" class="sr-only"></div>

<!-- Later, via JavaScript -->
<script>
document.getElementById('status').textContent = '3 results found';
</script>
```

### `aria-hidden`

| Pattern | Result |
|---|---|
| `aria-hidden="true"` on element with NO focusable children | Correctly hidden from AT |
| `aria-hidden="true"` on element WITH focusable children | Creates "ghost elements" — JAWS lands on them silently |
| `aria-hidden="true"` on `<body>` | Hides entire page — screen reader goes silent |

**Fix for focusable children**:
```html
<!-- BAD -->
<div aria-hidden="true">
  <button>Ghost button</button>
</div>

<!-- GOOD: use inert or display:none instead -->
<div inert>
  <button>Not reachable by any input method</button>
</div>
```

---

## 4. Tables

### Data tables vs layout tables

JAWS uses heuristics to determine if a `<table>` is for data or layout. Tables without `<th>`, `<caption>`, or `summary` may be treated as layout tables, causing JAWS to **silence row/column announcements**.

```html
<!-- Data table: explicit role -->
<table role="table">
  <caption>Program schedule for 2025</caption>
  <thead>
    <tr>
      <th scope="col">Program</th>
      <th scope="col">Day</th>
      <th scope="col">Time</th>
    </tr>
  </thead>
  <tbody>...</tbody>
</table>

<!-- Layout table: explicit role -->
<table role="presentation">...</table>
```

### Complex tables (merged cells)

```html
<th scope="col" id="day">Day</th>
<th scope="col" id="morning">Morning</th>
<th scope="col" id="afternoon">Afternoon</th>
<td headers="day morning">Workshop A</td>
<td headers="day afternoon">Workshop B</td>
```

---

## 5. Forms

### Label association

| Method | JAWS | NVDA | Recommendation |
|---|---|---|---|
| `<label for="id">` | Best | Best | **Always prefer this** |
| `aria-label` | Works | Works | Use for icon-only buttons |
| `aria-labelledby` | Works | Works | Use to combine multiple text sources |
| `title` attribute | Fallback only | Fallback only | Avoid — not announced in all modes |
| `placeholder` only | Not a label | Not a label | **Never use as sole label** |

### Error handling pattern

```tsx
<div className="flex flex-col gap-1">
  <label htmlFor="email">Email address</label>
  <input
    id="email"
    type="email"
    aria-invalid={!!error}
    aria-describedby={error ? "email-error" : "email-hint"}
    aria-required="true"
    autocomplete="email"
  />
  <p id="email-hint" className="text-sm text-gray-600">
    We will never share your email.
  </p>
  {error && (
    <p id="email-error" role="alert" className="text-sm text-red-600">
      {error}
    </p>
  )}
</div>
```

### Grouping related fields

```html
<fieldset>
  <legend>Shipping address</legend>
  <label for="street">Street</label>
  <input id="street" autocomplete="street-address">
  <label for="city">City</label>
  <input id="city" autocomplete="address-level2">
</fieldset>
```

---

## 6. Modals and dialogs

### Required behavior
1. **Focus trap**: Tab cycles within the modal only.
2. **Escape closes**: Pressing Escape dismisses the modal.
3. **Focus restoration**: On close, focus returns to the trigger element.
4. **Background inert**: Content behind the modal must be unreachable.

### Implementation pattern

```tsx
// Using native <dialog> (best for JAWS/NVDA)
<dialog
  ref={dialogRef}
  aria-labelledby="dialog-title"
  aria-describedby="dialog-desc"
>
  <h2 id="dialog-title">Confirm deletion</h2>
  <p id="dialog-desc">This action cannot be undone.</p>
  <button onClick={confirm}>Delete</button>
  <button onClick={cancel}>Cancel</button>
</dialog>
```

Native `<dialog>` with `.showModal()`:
- Automatically traps focus (JAWS and NVDA)
- Automatically sets `aria-modal="true"` behavior
- Escape key closes by default
- Background receives `inert` automatically

### Custom modal (when `<dialog>` is not an option)

```html
<div role="dialog" aria-modal="true" aria-labelledby="modal-title">...</div>
```

Plus JavaScript for: focus trap, Escape key handler, `inert` on `<main>`, focus restoration on close.

---

## 7. Navigation in SPAs

### The problem
In SPAs (Next.js, React Router), route changes don't trigger a full page load. Screen readers may not announce new content.

### Next.js Route Announcer
Next.js 14+ includes a built-in Route Announcer that checks `document.title`, then `<h1>`, then URL pathname.

**Ensure every page has a unique `<title>`:**
```tsx
export const metadata = {
  title: 'Programs — My Foundation',
};
```

### Focus management after route change

```tsx
useEffect(() => {
  const heading = document.querySelector('h1');
  if (heading) {
    heading.setAttribute('tabindex', '-1');
    heading.focus();
  }
}, [pathname]);
```

### Skip link

```html
<a
  href="#main-content"
  className="sr-only focus:not-sr-only focus:fixed focus:top-4 focus:left-4
    focus:z-50 focus:bg-white focus:px-4 focus:py-2 focus:rounded focus:shadow-lg"
>
  Skip to main content
</a>
<main id="main-content" tabindex="-1">...</main>
```

---

## 8. Anti-patterns

| Anti-pattern | Why it fails | Fix |
|---|---|---|
| `<a><button>Click</button></a>` | Nested interactive elements — JAWS reads name 3 times | Use `<a>` OR `<button>`, never nested |
| `<div onclick="...">` without role/tabindex | Invisible to keyboard users and screen readers | Use `<button>` |
| `role="application"` on page wrapper | Disables ALL virtual cursor navigation | Remove it; only use for canvas/WebGL |
| Positive `tabindex` (tabindex="1", "2") | Creates unpredictable focus order | Use only `tabindex="0"` or `tabindex="-1"` |
| Auto-playing audio/video | Interferes with screen reader speech output | Never auto-play; provide controls |
| `outline: none` without replacement | Keyboard users lose all focus indication | Always provide focus-visible styles |
| Relying on color alone for information | Fails for color-blind users + screen readers | Add text, icons, or patterns |
| `aria-live` + `aria-describedby` on same element | Double announcement in JAWS and NVDA | Separate into distinct DOM nodes |

---

## 9. Known bugs by version

### JAWS 2024
- **Excessive `aria-roledescription` repetition**: JAWS reads the custom role description multiple times when navigating grid rows.
- **`aria-live` in Shadow DOM**: Inconsistent announcement of live regions inside Web Components with Shadow DOM.

### JAWS 2025
- **`aria-current` silenced in `role="grid"` rows**: JAWS may ignore `aria-current` on rows inside a grid.
- **`aria-description` ignored in grid rows**: `role="row"` in grids causes `aria-description` to not be exposed.
- **`aria-roledescription` regressions**: Fixed the 2024 excessive repetition, but now may silence state metadata in grid rows.

### JAWS 2026 betas
- **Conditional silencing in `role="row"` + `grid`**: Ongoing inconsistencies with state metadata in grid rows vs JAWS 2024 and NVDA behavior.

### NVDA 2024+
- **`aria-description`**: Fully supported since 2023.1.
- **`<dialog>` native support**: Solid since 2023.3 — properly announces dialog role and traps virtual cursor.
- **`<details>`/`<summary>`**: Works correctly, announces expanded/collapsed state.

### Mitigation strategies
1. Never rely on a single ARIA attribute for critical information in grid contexts.
2. Test with the exact version deployed in your target environment.
3. Use NVDA as the compliance baseline — it follows the spec strictly.
4. Provide redundancy: visual indicators + text + ARIA combined.
5. Monitor changelogs: [JAWS](https://support.freedomscientific.com/), [NVDA](https://www.nvaccess.org/download/).

---

## 10. Version log template

Use this template to track regressions:

```text
Date:
AT:
AT version:
Browser:
Browser version:
Component:
Scenario:
Expected:
Observed:
Workaround:
Status:
```
