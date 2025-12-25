# Pages & Scripts - Bilingual Short Stories

Static bilingual story site served via GitHub Pages. Simple workflow: write stories in `.txt` files, run one command, and your entire website is generated.

## Quick Start

1. **Add a story:** Create folder in `stories-source/` with `story-en.txt` and `story-fa.txt`
2. **Build:** Run `.\tools\build-stories.ps1`
3. **View:** Open `docs\index.html` in browser

That's it! All pages, navigation, and styling are auto-generated.

## Project Structure

```
pages/
├── README.md                   ← You are here
├── .gitignore
│
├── docs/                       ← Website output (GitHub Pages serves this)
│   ├── assets/                 ← CSS, images, fonts
│   ├── en/                     ← English story pages
│   ├── fa/                     ← Persian story pages
│   └── index.html              ← Landing page
│
├── stories-source/             ← Your .txt story files
│   ├── lady-prince/
│   │   ├── story-en.txt
│   │   └── story-fa.txt
│   └── ...
│
├── templates/                  ← Design templates
│   ├── story-en.html
│   ├── story-fa.html
│   └── index-template.html
│
├── tools/                      ← Build scripts
│   └── build-stories.ps1       ← Main build command
│
└── documentation/              ← Detailed guides
    ├── HOW_IT_WORKS.md         ← Start here!
    ├── SIMPLE_WORKFLOW.md      ← Complete workflow guide
    └── STRUCTURE.md            ← Project organization
```

## Documentation

- **[HOW_IT_WORKS.md](documentation/HOW_IT_WORKS.md)** - Overview and quick examples
- **[SIMPLE_WORKFLOW.md](documentation/SIMPLE_WORKFLOW.md)** - Complete workflow guide
- **[STRUCTURE.md](documentation/STRUCTURE.md)** - Project organization details

## Story Format

Each story uses a simple text format with metadata:

```
---
title: Story Title
subtitle: Brief description
genre: Fantasy
reading-time: 5 min
---

Your story content here.

Each paragraph separated by blank lines.

Use *asterisks* for italics.
```

## Commands

```powershell
# Build all stories and generate website
.\tools\build-stories.ps1

# Preview locally
start docs\index.html
```

## Publish to GitHub Pages

**One-time setup:** In GitHub repository settings → Pages → set source to `main` branch `/docs` folder

**Quick one-liner (recommended):**

```powershell
.\tools\build-stories.ps1; git add .; git checkout -b v1.19.0; git commit -m "fix: resolve UTF-8 encoding issue causing Persian title corruption"; git push -u origin v1.19.0; git checkout main; git merge v1.19.0; git push origin main
```

This command: builds → creates feature branch → commits → pushes branch → merges to main → deploys

**Or step-by-step:**

```powershell
# 1. Build and commit to feature branch
.\tools\build-stories.ps1
git add .
git checkout -b v1.17.0
git commit -m "Your changes"
git push -u origin v1.17.0

# 2. Merge to main to deploy
git checkout main
git merge v1.17.0
git push origin main
```

GitHub Pages will automatically deploy from `main/docs` within ~1 minute.

## Benefits

✅ Write in simple .txt files  
✅ One command builds everything  
✅ Change design once, update all stories  
✅ Auto-generated navigation  
✅ Bilingual support built-in  
✅ GitHub Pages ready  
