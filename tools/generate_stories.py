#!/usr/bin/env python3
"""
Story Pages Generator
Generates all story HTML pages from templates and data
Usage: python tools/generate_stories.py
"""

import json
from pathlib import Path

def main():
    # Setup paths
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    output_root = repo_root / "docs"
    
    data_path = repo_root / "docs" / "stories-data.json"
    template_dir = repo_root / "templates"
    
    # Load story data
    if not data_path.exists():
        print(f"Error: Story data file not found: {data_path}")
        return 1
    
    print("Loading story data from docs/stories-data.json...")
    with open(data_path, 'r', encoding='utf-8') as f:
        story_data = json.load(f)
    
    # Load templates
    en_template_path = template_dir / "story-en.html"
    fa_template_path = template_dir / "story-fa.html"
    
    if not en_template_path.exists():
        print(f"Error: English template not found: {en_template_path}")
        return 1
    
    if not fa_template_path.exists():
        print(f"Error: Persian template not found: {fa_template_path}")
        return 1
    
    with open(en_template_path, 'r', encoding='utf-8') as f:
        en_template = f.read()
    
    with open(fa_template_path, 'r', encoding='utf-8') as f:
        fa_template = f.read()
    
    print("Templates loaded successfully.")
    
    # Generate stories
    stories = story_data['stories']
    story_count = len(stories)
    
    print(f"\nGenerating {story_count} stories...")
    
    for i, story in enumerate(stories):
        slug = story['slug']
        
        print(f"\n[{i+1}/{story_count}] Processing: {slug}")
        
        # Determine previous and next stories
        prev_story = stories[i-1] if i > 0 else None
        next_story = stories[i+1] if i < story_count - 1 else None
        
        # Generate English version
        en_dir = output_root / "en" / "stories" / slug
        en_dir.mkdir(parents=True, exist_ok=True)
        en_path = en_dir / "index.html"
        
        # Replace placeholders for English
        en_content = en_template
        en_content = en_content.replace('{{TITLE}}', story['en']['title'])
        en_content = en_content.replace('{{SLUG}}', slug)
        en_content = en_content.replace('{{CONTENT}}', story['en']['content'])
        
        # Generate navigation links
        if prev_story:
            prev_slug = prev_story['slug']
            prev_title = prev_story['en']['title']
            prev_link = f'<a class="story-nav-link" href="../{prev_slug}/index.html">Previous story: {prev_title}</a>'
        else:
            prev_link = '<span class="story-nav-link story-nav-disabled">Previous story</span>'
        
        if next_story:
            next_slug = next_story['slug']
            next_title = next_story['en']['title']
            next_link = f'<a class="story-nav-link" href="../{next_slug}/index.html">Next story: {next_title}</a>'
        else:
            next_link = '<span class="story-nav-link story-nav-disabled">Next story</span>'
        
        en_content = en_content.replace('{{PREV_LINK}}', prev_link)
        en_content = en_content.replace('{{NEXT_LINK}}', next_link)
        
        # Write English file with proper UTF-8 encoding
        with open(en_path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(en_content)
        print(f"  Created: en/stories/{slug}/index.html")
        
        # Generate Persian version
        fa_dir = output_root / "fa" / "stories" / slug
        fa_dir.mkdir(parents=True, exist_ok=True)
        fa_path = fa_dir / "index.html"
        
        # Replace placeholders for Persian
        fa_content = fa_template
        fa_content = fa_content.replace('{{TITLE}}', story['fa']['title'])
        fa_content = fa_content.replace('{{SLUG}}', slug)
        fa_content = fa_content.replace('{{CONTENT}}', story['fa']['content'])
        
        # Generate navigation links for Persian
        if prev_story:
            prev_slug = prev_story['slug']
            prev_title = prev_story['fa']['title']
            prev_link_fa = f'<a class="story-nav-link" href="../{prev_slug}/index.html">داستان قبلی: {prev_title}</a>'
        else:
            prev_link_fa = '<span class="story-nav-link story-nav-disabled">داستان قبلی</span>'
        
        if next_story:
            next_slug = next_story['slug']
            next_title = next_story['fa']['title']
            next_link_fa = f'<a class="story-nav-link" href="../{next_slug}/index.html">داستان بعدی: {next_title}</a>'
        else:
            next_link_fa = '<span class="story-nav-link story-nav-disabled">داستان بعدی</span>'
        
        fa_content = fa_content.replace('{{PREV_LINK}}', prev_link_fa)
        fa_content = fa_content.replace('{{NEXT_LINK}}', next_link_fa)
        
        # Write Persian file with proper UTF-8 encoding
        with open(fa_path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(fa_content)
        print(f"  Created: fa/stories/{slug}/index.html")
        
        # Create custom.css files if they don't exist
        en_css = en_dir / "custom.css"
        if not en_css.exists():
            en_css_content = "/* Custom styles for story */\n/* Add any story-specific CSS here */\n"
            with open(en_css, 'w', encoding='utf-8', newline='\n') as f:
                f.write(en_css_content)
            print(f"  Created: en/stories/{slug}/custom.css")
        
        fa_css = fa_dir / "custom.css"
        if not fa_css.exists():
            fa_css_content = "/* Custom styles for story */\n/* Add any story-specific CSS here */\n"
            with open(fa_css, 'w', encoding='utf-8', newline='\n') as f:
                f.write(fa_css_content)
            print(f"  Created: fa/stories/{slug}/custom.css")
        
        # Create images directories if they don't exist
        (en_dir / "images").mkdir(exist_ok=True)
        (fa_dir / "images").mkdir(exist_ok=True)
    
    print("\nSuccessfully generated all story pages!")
    print("\nTo update the main landing page index, run: python tools/generate_index.py")
    
    return 0

if __name__ == '__main__':
    exit(main())
