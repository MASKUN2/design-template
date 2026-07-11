# wireframe/

Standalone HTML **wireframes** — one file per user-facing screen, plus
[`index.html`](./index.html), a gallery linking them all.

These are deliberately **bare**: structure and copy over styling, so a mockup is
never mistaken for final visual design. See
[`../spec/ui-design.md`](../spec/ui-design.md) §7 for the design system itself.

## Conventions (enforced by `../validate.py`)

- **Self-contained**: inline `<style>` only; no external assets/fonts/CDN.
- **Minimal CSS**: one hairline `1px solid gray` border for all frames/dividers,
  system font, one `foreground`/`background` pair, auto light/dark via
  `@media (prefers-color-scheme: dark)`. No colour, hover, shadow, or radius.
- **Annotation**: a blue `<aside class="note">` at the top (never a `<footer>` —
  the real app may use that) describing the screen + its route, linking back to
  `index.html`.

## Files

- [`index.html`](./index.html) — gallery; must link every screen.
- `_TEMPLATE.html` — copy this to `NN-<name>.html` (two-digit prefix) per screen.
  Ignored by the validator.
- `01-example.html` — worked example; replace or delete.
