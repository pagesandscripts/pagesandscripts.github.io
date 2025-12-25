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