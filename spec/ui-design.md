# 7. UI & Visual Design

Part of the [{{PROJECT_NAME}} specification](./README.md).

The visual language is part of the product, so it lives here — at the *intent*
altitude (tokens, structure, patterns), not class names or markup. Concrete
per-screen mockups live in [`../wireframe/`](../wireframe/).

## 7.1 Design principles
- TODO(agent): 2–4 principles (e.g. content-first, minimal, calm).

## 7.2 Layout & structure
- TODO(agent): column width, rhythm, header/nav, responsive behaviour.

## 7.3 Colour & theme
Express colour as **role tokens**, not raw values, so light & dark derive from
one set. Adapt this starter table:

| Token | Role | Light | Dark |
|---|---|---|---|
| `background` | Page surface | near-white | near-black |
| `foreground` | Primary text | near-black | off-white |
| `muted` | Secondary text | mid grey | mid grey |
| `subtle` | Chip/card/code bg | faint wash | faint wash |
| `border` | Dividers, field borders | light grey | dark grey |
| `strong` | Primary button surface (inverts) | foreground | foreground |

- TODO(agent): decide light/dark strategy (auto from OS? manual toggle?).

## 7.4 Typography
- TODO(agent): font families, type scale, and any i18n constraints (e.g. must
  render CJK content well).

## 7.5 Shared UI patterns
Reuse these rather than inventing new ones — TODO(agent) to confirm/extend:
meta row · chip · tag · primary button · form field · back link · empty state ·
flash message.

## 7.6 Copy & microcopy
- **UI language:** TODO(agent) — pick the UI copy language. Note which content is
  *data* (shown as authored, possibly another language) vs *chrome* (translated).
- **Dates:** TODO(agent) — pick a format (e.g. ISO `YYYY-MM-DD`).
- Pin fixed strings (empty states, success/error flashes) so they're consistent.

## 7.7 Accessibility
- TODO(agent): contrast in both themes, legible sizes, real links, keyboard
  focus, machine-readable timestamps.

---

## Mockup conventions (for `../wireframe/*.html`)

The HTML mockups are **bare wireframes** — structure and copy over styling, so
nobody mistakes a mockup for final visual design. Each screen file:

- **Shared styles, no remote assets**: link the local
  [`../wireframe/wireframe.css`](../wireframe/wireframe.css); add only truly
  page-specific rules inline. No `http(s)`/CDN assets, fonts, or `@import`.
- **Minimal CSS**: a single hairline `1px solid gray` border for all frames and
  dividers, system font, one `foreground`/`background` pair, auto light/dark via
  `@media (prefers-color-scheme: dark)`. No colour, hover, shadow, or radius.
- **Annotation**: a blue `<aside class="note">` at the top (NOT a `<footer>`,
  which the real app may use) explaining the screen + its route, with a link back
  to `index.html`.
- Real sample copy; content that would be user-authored can be shown as-is.

Copy `_TEMPLATE.html` for each new screen; `index.html` links them all.
`validate.py` checks these conventions structurally.
