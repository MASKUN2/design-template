# wireframe/

One **bare-wireframe** HTML per screen — structure and copy over styling, so a
mockup is never mistaken for final design. [`index.html`](./index.html) is the
gallery; [`wireframe.css`](./wireframe.css) holds the shared styles.

Rules: every screen links `wireframe.css` (no remote assets), uses one hairline
border + system font + auto light/dark (no colour/hover/shadow), and carries a
blue `<aside class="note">` linking back to `index.html`. Follow the existing
screens as the pattern. Design system:
[`../spec/ui-design.md`](../spec/ui-design.md) §7.
