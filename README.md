# pagesandscripts.github.io

Static short story site served via GitHub Pages. The landing page showcases bilingual content: a hero illustration followed by dual story lists (English and Persian) so visitors can drop straight into either language.

## Structure

- `index.html` – Root landing page with hero image and side-by-side English/Persian story lists (stacks on mobile).
- `en/index.html` / `fa/index.html` – Optional deeper landing pages for each language if you want longer descriptions.
- `assets/css/` – Shared styling (`main.css`) plus RTL overrides (`rtl.css`) loaded by Persian pages.
- `assets/images/` – Global art (subfolders for `cover/`, `shared/`, and optional per-language imagery under `en/` and `fa/`).
- `assets/fonts/` – Custom typefaces grouped by language as needed.
- `en/stories/<slug>/` and `fa/stories/<slug>/` – Paired story folders. Each contains `index.html`, optional `custom.css`, and a local `images/` directory. Keep slugs identical across languages so cross-links stay predictable.

Copy the `en/stories/story-template/` and `fa/stories/story-template/` folders when drafting new stories. Update both language versions together so the landing page lists stay in sync.

## Authoring notes

- Keep every HTML or CSS file under ~400 lines for readability; split large pages into partials or shared assets if needed.
- Reference the shared cover art (`assets/images/cover/watercolor_black_horse.avif`) from the landing page hero.
- Add “Read in English/Persian” cross-links between translated stories to help readers switch languages mid-story.
- Generate a local preview of the landing page with `powershell -File tools/generate-local-preview.ps1`; this writes `local-preview.html` (ignored by git) for quick browser inspection.
