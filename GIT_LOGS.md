# Git Push Logs

This file tracks all version deployments to GitHub Pages.

## Command Template

```powershell
git add .; git checkout -b v1.20.0; git commit -m "your change description"; git push -u origin v1.20.0; git checkout main; git merge v1.20.0; git push origin main
```

## Version History

v1.21.0: removed language-specific index pages (en/index.html and fa/index.html) and simplified 
v1.22.0: fix breadcrumb navigation to point to main index page
v1.23.0: moved stories-data.json to docs folder and removed subtitle, genre, and readingTime metadata fields from story structure
v1.24.0: removed translation metadata links and footer navigation from story pages
v1.25.0: improved story page typography with centered title, 65ch max-width, justified text, and responsive font sizing
v1.26.0: fixed story page CSS asset paths; centered header/breadcrumb; set story width to 60ch and removed story content background
v1.27.0: aligned story header to 60ch reading column; forced transparent story background; improved text justification (hyphenation + inter-word)
v1.28.0: interleaved EN/FA story titles on mobile while keeping left/right alignment; preserved two-column layout on larger screens
v1.29.0: updated Persian version of lady-prince story
v1.30.0: added new story "The Corpse" (English + Persian source files created)
v1.31.0: migrated story sources from .txt to .md and updated build script to read .md (with .txt fallback)
v1.32.0: regenerated docs output so "The Corpse / جنازه" appears on the main page and story pages are rebuilt from updated sources
v1.33.0: added new story folders for "Nabekar / نابکار", "Destiny / سزنوشت", and "Manuscripts / دست نوشته ها"