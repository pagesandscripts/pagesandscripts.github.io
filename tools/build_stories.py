#!/usr/bin/env python3
"""
Complete Build Script - Processes stories and generates all pages
Usage: python tools/build_stories.py
"""

import json
import re
from pathlib import Path
from datetime import datetime

def parse_story_file(file_path):
    """Parse a story text file with frontmatter and content."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract frontmatter
    if not content.startswith('---'):
        raise ValueError(f"Story file {file_path} must start with frontmatter (---)")
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        raise ValueError(f"Invalid frontmatter format in {file_path}")
    
    frontmatter_text = parts[1].strip()
    story_content = parts[2].strip()
    
    # Parse frontmatter
    metadata = {}
    for line in frontmatter_text.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            metadata[key.strip()] = value.strip()
    
    # Convert paragraphs to HTML with italic support
    paragraphs = story_content.split('\n\n')
    html_paragraphs = []
    
    for para in paragraphs:
        if para.strip():
            # Replace *text* with <em>text</em>
            para = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', para)
            html_paragraphs.append(f'<p>{para.strip()}</p>')
    
    metadata['content'] = '\n\n'.join(html_paragraphs)
    
    return metadata

def main():
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    source_dir = repo_root / "stories-source"
    
    print("=" * 60)
    print("Building Stories & Generating Pages")
    print("=" * 60)
    
    # Find all story directories
    story_dirs = [d for d in source_dir.iterdir() if d.is_dir() and d.name != '__pycache__']
    
    if not story_dirs:
        print("No story directories found in stories-source/")
        return 1
    
    print(f"\nFound {len(story_dirs)} story directories")
    
    stories = []
    
    for story_dir in sorted(story_dirs):
        slug = story_dir.name
        
        # Skip template
        if slug == 'story-template':
            continue
        
        print(f"\nProcessing: {slug}")
        
        en_file = story_dir / "story-en.txt"
        fa_file = story_dir / "story-fa.txt"
        
        if not en_file.exists():
            print(f"  Warning: Missing story-en.txt, skipping...")
            continue
        
        if not fa_file.exists():
            print(f"  Warning: Missing story-fa.txt, skipping...")
            continue
        
        try:
            en_data = parse_story_file(en_file)
            fa_data = parse_story_file(fa_file)
            
            story = {
                "slug": slug,
                "en": {
                    "title": en_data.get('title', 'Untitled'),
                    "content": en_data['content']
                },
                "fa": {
                    "title": fa_data.get('title', 'بدون عنوان'),
                    "content": fa_data['content']
                }
            }
            
            stories.append(story)
            print(f"  ✓ Parsed: {en_data.get('title')} / {fa_data.get('title')}")
            
        except Exception as e:
            print(f"  Error parsing {slug}: {e}")
            continue
    
    if not stories:
        print("\nNo valid stories found!")
        return 1
    
    # Create story data JSON
    story_data = {
        "stories": stories,
        "metadata": {
            "generatedAt": datetime.now().isoformat(),
            "storyCount": len(stories)
        }
    }
    
    json_path = repo_root / "docs" / "stories-data.json"
    with open(json_path, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(story_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n✓ Generated docs/stories-data.json with {len(stories)} stories")
    
    # Now run the story and index generators
    print("\n" + "=" * 60)
    print("Generating HTML Pages")
    print("=" * 60)
    
    # Import and run the generators
    import sys
    sys.path.insert(0, str(script_dir))
    
    from generate_stories import main as generate_stories
    from generate_index import main as generate_index
    
    result = generate_stories()
    if result != 0:
        return result
    
    result = generate_index()
    if result != 0:
        return result
    
    print("\n" + "=" * 60)
    print("Build Complete!")
    print("=" * 60)
    print("\nYour website is ready in the docs/ folder")
    print("To preview: start docs\\index.html")
    
    return 0

if __name__ == '__main__':
    exit(main())
