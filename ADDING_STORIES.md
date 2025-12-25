# Adding a New Story - Quick Guide

This guide shows you how to add a new bilingual story to your website following the reusable template structure.

## File Structure

Each story requires:
```
en/stories/[story-slug]/
├── index.html
├── custom.css
└── images/

fa/stories/[story-slug]/
├── index.html
├── custom.css
└── images/
```

## Step-by-Step Instructions

### 1. Create English Story Files

**File:** `en/stories/[story-slug]/index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>[Story Title] · Pages &amp; Scripts</title>
  <meta name="description" content="[Story Title] — a short story by pagesandscripts presented in English.">
  <link rel="stylesheet" href="../../assets/css/main.css">
  <link rel="stylesheet" href="custom.css">
</head>
<body class="story-page">
  <header class="story-header">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="../../index.html">Home</a>
      <span aria-hidden="true">/</span>
      <span>[Story Title]</span>
    </nav>
    <h1>[Story Title]</h1>
    <p class="story-subtitle">[Your story subtitle]</p>
    <ul class="story-meta-list">
      <li>Genre: [Genre]</li>
      <li>Reading time: [X min]</li>
      <li>Translation: <a href="../../fa/stories/[story-slug]/index.html" lang="fa" dir="rtl">[Persian Title]</a></li>
    </ul>
  </header>

  <main class="story-content" id="story">
    <p>[Your story content here...]</p>
  </main>

  <footer class="story-footer">
    <nav class="story-nav" aria-label="Story navigation">
      <a class="story-nav-link" href="../[previous-story]/index.html">Previous story: [Previous Title]</a>
      <a class="story-nav-link" href="../../index.html">Back to landing page</a>
      <a class="story-nav-link" href="../../fa/stories/[story-slug]/index.html" lang="fa" dir="rtl">مطالعه به فارسی</a>
    </nav>
  </footer>
</body>
</html>
```

**File:** `en/stories/[story-slug]/custom.css`

```css
/* Custom styles for [Story Title] story */
/* Add any story-specific CSS here */
```

### 2. Create Persian Story Files

**File:** `fa/stories/[story-slug]/index.html`

```html
<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>[Persian Title] · Pages &amp; Scripts</title>
  <meta name="description" content="داستان کوتاه [Persian Title] به زبان فارسی از pagesandscripts.">
  <link rel="stylesheet" href="../../assets/css/main.css">
  <link rel="stylesheet" href="../../assets/css/rtl.css">
  <link rel="stylesheet" href="custom.css">
</head>
<body class="story-page">
  <header class="story-header">
    <nav class="breadcrumb" aria-label="مسیر ناوبری">
      <a href="../../index.html" lang="en" dir="ltr">Home</a>
      <span aria-hidden="true">/</span>
      <span>[Persian Title]</span>
    </nav>
    <h1>[Persian Title]</h1>
    <p class="story-subtitle">[Your Persian subtitle]</p>
    <ul class="story-meta-list">
      <li>ژانر: [Genre in Persian]</li>
      <li>زمان مطالعه: [X دقیقه]</li>
      <li>نسخهٔ انگلیسی: <a href="../../en/stories/[story-slug]/index.html" lang="en" dir="ltr">[Story Title]</a></li>
    </ul>
  </header>

  <main class="story-content" id="story">
    <p>[متن داستان فارسی شما اینجا...]</p>
  </main>

  <footer class="story-footer">
    <nav class="story-nav" aria-label="پیمایش داستان">
      <a class="story-nav-link" href="../[previous-story]/index.html">داستان قبلی: [Previous Persian Title]</a>
      <a class="story-nav-link" href="../../index.html" lang="en" dir="ltr">Back to landing page</a>
      <a class="story-nav-link" href="../../en/stories/[story-slug]/index.html" lang="en" dir="ltr">Read in English</a>
    </nav>
  </footer>
</body>
</html>
```

**File:** `fa/stories/[story-slug]/custom.css`

```css
/* سبک‌های سفارشی برای داستان [Persian Title] */
/* Add any story-specific CSS here */
```

### 3. Update Main Index Page

Edit `index.html` in the root directory and add your story links to both columns:

```html
<div class="story-index__column story-index__column--en">
  <ul class="story-index__list">
    <!-- existing stories -->
    <li>
      <a href="en/stories/[story-slug]/index.html">
        <span>[Story Title]</span>
      </a>
    </li>
  </ul>
</div>

<div class="story-index__column story-index__column--fa" lang="fa" dir="rtl">
  <ul class="story-index__list">
    <!-- existing stories -->
    <li>
      <a href="fa/stories/[story-slug]/index.html">
        <span>[Persian Title]</span>
      </a>
    </li>
  </ul>
</div>
```

### 4. Update Previous Story Navigation

Edit the **last story** in your collection to add a "Next story" link pointing to your new story:

**English version footer:**
```html
<a class="story-nav-link" href="../[new-story-slug]/index.html">Next story: [New Story Title]</a>
```

**Persian version footer:**
```html
<a class="story-nav-link" href="../[new-story-slug]/index.html">داستان بعدی: [New Persian Title]</a>
```

## Quick Reference: Placeholders to Replace

- `[story-slug]`: URL-friendly name (e.g., `the-trial`, `lady-prince`)
- `[Story Title]`: English title (e.g., "The Trial")
- `[Persian Title]`: Persian title (e.g., "محاکمه")
- `[Your story subtitle]`: Brief description in English
- `[Your Persian subtitle]`: Brief description in Persian
- `[Genre]`: Story genre (e.g., "Fantasy", "Drama")
- `[X min]`: Reading time in minutes
- `[previous-story]`: Slug of the previous story
- `[Previous Title]`: Title of the previous story

## Example: "The Trial" Story

See the newly created files:
- `en/stories/the-trial/index.html`
- `fa/stories/the-trial/index.html`

These serve as a working template for future stories.

## Notes

- Story slugs should be lowercase with hyphens (kebab-case)
- Always create both English and Persian versions together
- Maintain consistent ordering across both language columns
- Store story-specific images in the `images/` folder
- Use `custom.css` for any story-specific styling needs
