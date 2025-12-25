#!/usr/bin/env python3
"""
Index Page Generator
Generates the main index.html from story data
Usage: python tools/generate_index.py
"""

import json
from pathlib import Path

def main():
    # Setup paths
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    output_root = repo_root / "docs"
    
    data_path = repo_root / "docs" / "stories-data.json"
    template_path = repo_root / "templates" / "index-template.html"
    output_path = output_root / "index.html"
    
    # Load story data
    if not data_path.exists():
        print(f"Error: Story data file not found: {data_path}")
        return 1
    
    print(f"Loading story data from docs/stories-data.json...")
    with open(data_path, 'r', encoding='utf-8') as f:
        story_data = json.load(f)
    
    # Load template
    if not template_path.exists():
        print(f"Error: Index template not found: {template_path}")
        return 1
    
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()
    
    # Generate story lists
    en_list_items = []
    fa_list_items = []
    
    for story in story_data['stories']:
        slug = story['slug']
        
        en_item = f"""          <li>
            <a href="en/stories/{slug}/index.html">
              <span>{story['en']['title']}</span>
            </a>
          </li>"""
        
        fa_item = f"""          <li>
            <a href="fa/stories/{slug}/index.html">
              <span>{story['fa']['title']}</span>
            </a>
          </li>"""
        
        en_list_items.append(en_item)
        fa_list_items.append(fa_item)
    
    en_list = '\n'.join(en_list_items)
    fa_list = '\n'.join(fa_list_items)
    
    # Replace placeholders in template
    index_content = template.replace('{{EN_STORY_LIST}}', en_list)
    index_content = index_content.replace('{{FA_STORY_LIST}}', fa_list)
    
    # Write index.html with proper UTF-8 encoding
    with open(output_path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(index_content)
    
    count = len(story_data['stories'])
    print(f"\nSuccessfully generated index.html with {count} stories!")
    
    return 0

if __name__ == '__main__':
    exit(main())
