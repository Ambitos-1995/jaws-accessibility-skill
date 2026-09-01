# Priority WCAG 2.2 Patterns (Not a Complete Criteria Matrix)

Last reviewed: 2026-08-31

## TOC

1. Coverage boundary and normative status
2. Overview: WCAG 2.2 vs 2.1
3. Principle 1: Perceivable
4. Principle 2: Operable
5. Principle 3: Understandable
6. Principle 4: Robust
7. Deprecated criteria
8. Evidence model for audits
9. Official references

---

## 1. Coverage boundary and normative status

- WCAG 2.2 is a W3C Recommendation (published 2023-10-05, updated 2024-12-12) and was approved as ISO/IEC 40500:2025. The W3C Recommendation remains the implementation reference used here.
- In legal contexts, enforceability depends on the applicable law and harmonized standard.
- This file contains **priority implementation patterns, not all 86 success criteria and not a conformance checklist**. Use the official WCAG 2.2 Quick Reference as the complete criteria matrix: https://www.w3.org/WAI/WCAG22/quickref/
- Use these examples as engineering guidance, then map the complete applicable criteria set to the legal baseline with `spanish-eu-legislation.md`. WAI-ARIA Authoring Practices describe widget design patterns; they are not additional WCAG success criteria and do not by themselves establish conformance.

---

## 2. Overview: WCAG 2.2 vs 2.1

WCAG 2.2 adds 9 new success criteria (2 Level A, 4 Level AA, 3 Level AAA) and deprecates 1 (4.1.1 Parsing). Total: 86 success criteria.

New Level A:
- 3.2.6 Consistent Help
- 3.3.7 Redundant Entry

New Level AA:
- 2.4.11 Focus Not Obscured (Minimum)
- 2.5.7 Dragging Movements
- 2.5.8 Target Size (Minimum)
- 3.3.8 Accessible Authentication (Minimum)

New Level AAA:
- 2.4.12 Focus Not Obscured (Enhanced)
- 2.4.13 Focus Appearance
- 3.3.9 Accessible Authentication (Enhanced)

---

## 3. Principle 1: Perceivable

### 1.1.1 Non-text Content (A)
All non-text content must have a text alternative.

```html
<!-- BAD -->
<img src="team-photo.jpg">
<button><svg>...</svg></button>

<!-- GOOD -->
<img src="team-photo.jpg" alt="The team at the 2024 annual conference">
<button>
  <svg aria-hidden="true">...</svg>
  <span class="sr-only">Close menu</span>
</button>

<!-- Decorative image — empty alt -->
<img src="decorative-wave.svg" alt="" role="presentation">
```

### 1.2.2 Captions (Prerecorded) (A)
Prerecorded synchronized media with audio must provide accurate, synchronized captions for speech and meaningful non-speech audio, subject to the criterion's media-alternative exception.

### 1.2.3 Audio Description or Media Alternative (Prerecorded) (A)
Prerecorded video needs either audio description or an equivalent time-based media alternative when meaningful visual information is not already conveyed in the soundtrack.

### 1.2.5 Audio Description (Prerecorded) (AA)
At Level AA, prerecorded video in synchronized media needs audio description for meaningful visual information, subject to the criterion's scope and exceptions. A transcript alone does not automatically satisfy this AA criterion.

### 1.3.1 Info and Relationships (A)
Information, structure, and relationships conveyed visually must be programmatically determinable.

```html
<!-- BAD: visual-only heading -->
<div class="big-bold-text">Our Programs</div>

<!-- GOOD: semantic heading -->
<h2>Our Programs</h2>

<!-- BAD: visual-only required field -->
<input type="text"> <span style="color:red">*</span>

<!-- GOOD: programmatic required -->
<label for="name">Name <span aria-hidden="true">*</span></label>
<input id="name" type="text" aria-required="true" required>
```

### 1.3.5 Identify Input Purpose (AA)
Input fields that collect user data must have appropriate `autocomplete` attributes.

```html
<!-- BAD -->
<input type="text" name="fname">

<!-- GOOD -->
<input type="text" name="fname" autocomplete="given-name">
<input type="email" name="email" autocomplete="email">
<input type="tel" name="phone" autocomplete="tel">
```

### 1.4.3 Contrast (Minimum) (AA)
Text must have a contrast ratio of at least 4.5:1 (3:1 for large text >= 18pt or 14pt bold).

```html
<!-- BAD: gray on white = ~2.5:1 -->
<p class="text-gray-400 bg-white">Hard to read</p>

<!-- GOOD: dark gray on white = ~7:1 -->
<p class="text-gray-700 bg-white">Easy to read</p>
```

### 1.4.11 Non-text Contrast (AA)
UI components and graphical objects must have at least 3:1 contrast against adjacent colors.

```html
<!-- BAD: low-contrast border -->
<input class="border-gray-200 bg-white">

<!-- GOOD: sufficient contrast border -->
<input class="border-gray-500 bg-white">
```

### 1.4.13 Content on Hover or Focus (AA)
Content that appears on hover/focus must be dismissible, hoverable, and persistent.

```tsx
// BAD: tooltip disappears when moving mouse to it
<div onMouseEnter={show} onMouseLeave={hide}>
  <span>Hover me</span>
  {visible && <div className="tooltip">Info</div>}
</div>

// GOOD: tooltip stays visible when hovering over it, dismissible with Escape
<div onMouseEnter={show} onMouseLeave={hide}>
  <span>Hover me</span>
  {visible && (
    <div
      className="tooltip"
      onMouseEnter={show}
      onMouseLeave={hide}
      role="tooltip"
    >
      Info
    </div>
  )}
</div>
```

### 1.4.10 Reflow (AA)
At an equivalent viewport of 320 CSS pixels wide for vertically scrolling content, information and functionality must remain available without two-dimensional scrolling, except for content that requires two-dimensional layout for meaning or use.

---

## 4. Principle 2: Operable

### 2.1.1 Keyboard (A)
All functionality must be operable through a keyboard interface.

```tsx
// BAD: only click handler
<div onClick={handleAction}>Do something</div>

// GOOD: keyboard-accessible button
<button onClick={handleAction}>Do something</button>

// If you must use a div (rare), add keyboard support:
<div
  role="button"
  tabIndex={0}
  onClick={handleAction}
  onKeyDown={(e) => {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      handleAction();
    }
  }}
>
  Do something
</div>
```

### 2.1.2 No Keyboard Trap (A)
Keyboard users must be able to move focus away from a component using only a keyboard interface, or be told the non-standard exit method. Restricting focus while a modal dialog is open can satisfy this criterion when the user has a keyboard way to dismiss or leave it.

WCAG does not prescribe one complete modal interaction model. The APG dialog pattern is informative guidance and conventionally cycles focus within a modal, supports Escape to close, and restores focus appropriately. Report a WCAG failure only after mapping the actual user impact to a normative success criterion; do not report deviation from an APG example as a failure by itself.

### 2.4.3 Focus Order (A)
Focusable components must receive focus in an order that preserves meaning and operability.

```html
<!-- BAD: visual order differs from DOM order -->
<div style="display: flex; flex-direction: row-reverse">
  <button>Third visually, first in DOM</button>
  <button>Second</button>
  <button>First visually, third in DOM</button>
</div>

<!-- GOOD: DOM order matches visual order -->
<div style="display: flex">
  <button>First</button>
  <button>Second</button>
  <button>Third</button>
</div>
```

### 2.4.7 Focus Visible (AA)
Keyboard focus indicator must be visible.

```css
/* BAD */
*:focus { outline: none; }

/* GOOD — Tailwind pattern */
.btn {
  @apply focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500;
}
```

### 2.4.11 Focus Not Obscured (Minimum) (AA) — NEW in 2.2
The focused element must not be entirely hidden by author-created content (sticky headers, FABs, cookie banners).

```css
/* GOOD: ensure focused elements aren't hidden behind sticky header */
html {
  scroll-padding-top: 5rem; /* height of sticky header */
}

/* For fixed bottom bars */
main {
  scroll-padding-bottom: 4rem; /* height of fixed bottom bar */
}
```

### 2.5.7 Dragging Movements (AA) — NEW in 2.2
Any functionality that uses dragging must offer a single-pointer alternative.

```tsx
// BAD: drag-only reordering
<SortableList onDrag={reorder} />

// GOOD: drag + button alternative
<SortableList onDrag={reorder}>
  {items.map(item => (
    <li key={item.id}>
      {item.name}
      <button onClick={() => moveUp(item.id)} aria-label={`Move ${item.name} up`}>Up</button>
      <button onClick={() => moveDown(item.id)} aria-label={`Move ${item.name} down`}>Down</button>
    </li>
  ))}
</SortableList>
```

### 2.5.8 Target Size (Minimum) (AA) — NEW in 2.2
Interactive targets must be at least 24x24 CSS pixels, or satisfy one of the criterion's exceptions (including spacing, equivalent control, inline, user-agent-controlled, or essential presentation). Treat 44x44 CSS pixels as a strong usability recommendation, not the WCAG 2.2 AA minimum.

```html
<!-- BAD: tiny icon button -->
<button class="w-4 h-4"><svg>...</svg></button>

<!-- GOOD: meets 44x44 recommendation -->
<button class="min-w-[44px] min-h-[44px] p-2">
  <svg class="w-5 h-5" aria-hidden="true">...</svg>
  <span class="sr-only">Settings</span>
</button>
```

---

## 5. Principle 3: Understandable

### 3.1.1 Language of Page (A)
The default language must be declared.

```html
<html lang="es">  <!-- Spanish -->
<html lang="en">  <!-- English -->
```

### 3.1.2 Language of Parts (AA)
Content in a different language must be marked.

```html
<p>The foundation uses the concept of <span lang="es">accesibilidad universal</span>.</p>
```

### 3.2.6 Consistent Help (A) — NEW in 2.2
If a page provides help mechanisms (contact info, chat, FAQ links), they must appear in the same relative order across pages.

```html
<!-- GOOD: footer help section consistent across all pages -->
<footer>
  <nav aria-label="Help">
    <a href="/faq">FAQ</a>
    <a href="/contact">Contact us</a>
    <a href="tel:+34900000000">Call: 900 000 000</a>
  </nav>
</footer>
```

### 3.3.1 Error Identification (A)
Errors must be identified and described to the user in text.

```tsx
// BAD: only visual indication
<input className={error ? "border-red-500" : ""} />

// GOOD: visual + programmatic + text description
<input
  aria-invalid={!!error}
  aria-describedby={error ? "email-error" : undefined}
  className={error ? "border-red-500" : ""}
/>
{error && (
  <p id="email-error" role="alert" className="text-red-600 text-sm">
    Please enter a valid email address.
  </p>
)}
```

### 3.3.2 Labels or Instructions (A)
Form fields must have labels or instructions.

```html
<!-- BAD: placeholder as label -->
<input type="email" placeholder="Email">

<!-- GOOD: visible label -->
<label for="email">Email address</label>
<input id="email" type="email" autocomplete="email">
```

### 3.3.7 Redundant Entry (A) — NEW in 2.2
Information previously entered by the user in the same process must be auto-populated or available for selection.

```tsx
// BAD: user must re-type shipping address for billing
<Step1><AddressForm name="shipping" /></Step1>
<Step2><AddressForm name="billing" /></Step2>

// GOOD: offer to reuse shipping address
<Step2>
  <label>
    <input type="checkbox" onChange={copyShipping} />
    Billing address same as shipping
  </label>
  <AddressForm name="billing" defaultValues={useSameAddress ? shippingData : undefined} />
</Step2>
```

### 3.3.8 Accessible Authentication (Minimum) (AA) — NEW in 2.2
Authentication must not rely on cognitive function tests as the ONLY method. Must support at least one of:
- Password managers (allow paste in password fields)
- WebAuthn / biometric login
- Magic links / email codes
- OAuth / SSO

```html
<!-- BAD: blocks pasting -->
<input type="password" onpaste="return false">

<!-- GOOD: allows paste, supports autocomplete -->
<input type="password" autocomplete="current-password">
```

---

## 6. Principle 4: Robust

### 4.1.2 Name, Role, Value (A)
All UI components must have accessible name, role, and state exposed to assistive technology.

```tsx
// BAD: custom toggle with no semantics
<div className="toggle" onClick={toggle}>
  <div className={active ? "on" : "off"} />
</div>

// GOOD: proper semantics
<button
  role="switch"
  aria-checked={active}
  aria-label="Dark mode"
  onClick={toggle}
>
  <span className={active ? "translate-x-5" : "translate-x-0"} />
</button>
```

### 4.1.3 Status Messages (AA)
Status messages that don't receive focus must be exposed via live regions.

```html
<!-- The container must exist EMPTY in initial HTML -->
<div aria-live="polite" role="status" class="sr-only"></div>

<!-- Content injected dynamically AFTER initial render -->
<script>
  statusRegion.textContent = "Form submitted successfully.";
</script>
```

---

## 7. Deprecated criteria

### 4.1.1 Parsing (formerly A)
WCAG 2.2 marks this criterion obsolete and removes it. The updated WCAG 2.0 and WCAG 2.1 materials also state that 4.1.1 should be considered **always satisfied for content using HTML or XML**.

Do not report an HTML/XML accessibility failure under 4.1.1. Map the actual user impact to another applicable criterion, commonly 1.3.1 (Info and Relationships) or 4.1.2 (Name, Role, Value). Markup validation can still be useful for code quality, and a dated procurement procedure may separately require a legacy validation check, but that does not turn the defect into a current WCAG 4.1.1 failure.

---

## 8. Evidence model for audits

For each finding, record:
- WCAG SC id and level
- Result: `PASS`, `FAIL`, `NOT TESTED`, or `NOT APPLICABLE`
- Page/route and control identifier
- Reproduction steps
- Complete environment ID, including assistive technology and browser builds
- Expected result
- Actual result
- Code-level remediation note

---

## 9. Official references

- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- WCAG 2.2 Quick Reference: https://www.w3.org/WAI/WCAG22/quickref/
- Understanding docs index: https://www.w3.org/WAI/WCAG22/Understanding/
- W3C WCAG FAQ, including the status of 4.1.1 in WCAG 2.0/2.1: https://www.w3.org/WAI/standards-guidelines/wcag/faq/
- WAI-ARIA Authoring Practices introduction (APG is informative, not normative): https://www.w3.org/WAI/ARIA/apg/about/introduction/
- WCAG 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- WCAG 2.2 ISO/IEC announcement: https://www.w3.org/press-releases/2025/wcag22-iso-pas/
