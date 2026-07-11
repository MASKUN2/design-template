# 7. UI & Visual Design

Part of the [{{PROJECT_NAME}} specification](./README.md). The visual language at
the *intent* altitude — tokens, structure, patterns. Concrete per-screen mockups
live in [`../wireframe/`](../wireframe/).

## 7.1 Design principles
- **Reading-first.** The content is the interface; chrome recedes.
- **Minimal and calm.** A single neutral palette, generous whitespace, no motion.

## 7.2 Layout & structure
- One centred column (~640–720px) with consistent padding, on every page.
- A persistent header: the site title (links home) and minimal nav.
- Mobile-first; the single column collapses cleanly on narrow viewports.

## 7.3 Colour & theme
Colour as **role tokens**, not raw values, so light & dark derive from one set.
Themes follow the OS setting (no manual toggle):

| Token | Role | Light | Dark |
|---|---|---|---|
| `background` | Page surface | near-white | near-black |
| `foreground` | Primary text | near-black | off-white |
| `muted` | Secondary text, meta | mid grey | mid grey |
| `subtle` | Chip / card / code bg | faint wash | faint wash |
| `border` | Dividers, field borders | light grey | dark grey |
| `strong` | Primary button surface (inverts) | foreground | foreground |

Accent colour is reserved for feedback (success / error) only.

## 7.4 Typography
- Sans-serif for UI and body; monospace for code.
- A small fixed scale: page title → section title → body → meta (muted).
- Must read well for the content's language(s), including non-ASCII.

## 7.5 Shared UI patterns
Meta row (date · state) · primary button (one per form) · form field · back
link · empty state (a muted sentence, never a blank screen) · status label
(draft / published).

## 7.6 Copy & microcopy
- Plain, calm, consistent. Pin fixed strings so they never drift:
  - Empty post list → *"No posts yet."*
  - Delete confirmation → *"Delete this post? This can't be undone."*
- Dates render in a single consistent format (e.g. ISO `YYYY-MM-DD`).

## 7.7 Accessibility
- Sufficient contrast in both themes; legible sizes; real links; visible keyboard
  focus; timestamps carry machine-readable values.
