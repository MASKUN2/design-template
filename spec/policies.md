# 5. Policies & Business Rules

Part of the [{{PROJECT_NAME}} specification](./README.md). Non-negotiable rules,
numbered so other docs can cite them (e.g. `§5.2`).

## 5.1 Content visibility
- A post that is not published is **private**: never listed, never reachable by
  its slug, never exposed on any public surface. Only the author sees drafts.
- Public listings are ordered newest-first by publication date.

## 5.2 Identifiers
- Every post has a **unique, URL-safe slug**. Reusing an existing slug is rejected.
- Slugs may contain non-ASCII characters and must work end-to-end in URLs.

## 5.3 Integrity
- Publishing stamps a publication timestamp once; unpublishing does not clear it.
- Deleting a post is permanent and removes it from every surface.

## 5.4 Authorisation
- All create/edit/delete/publish actions require the **author** credential.
- Reading published content is the only action available without authentication.

---

# 6. Non-Functional Requirements

| Area | Requirement |
|---|---|
| **Performance** | Public pages render fast; the read path is the priority. |
| **Hosting** | Runs on modest hardware; simple to deploy and operate solo. |
| **Security** | The author credential is never committed; drafts never leak. |
| **Backup** | Content lives in a database that can be backed up and restored. |
| **Accessibility** | Legible typography, sufficient contrast, keyboard-navigable, mobile-friendly. |
| **Internationalisation** | Content and slugs may be non-ASCII; nothing breaks on them. |
| **Maintainability** | One person can understand and run the whole system. |
