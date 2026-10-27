import os, glob, re

posts_dir = 'posts'
files = glob.glob(os.path.join(posts_dir, '*.md'))
print(f'Total posts found: {len(files)}')

errors = []
stats = []

for f in sorted(files):
    name = os.path.basename(f)
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    # Check frontmatter
    fm_match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', content, re.DOTALL)
    if not fm_match:
        errors.append(f'{name}: Frontmatter missing or malformed')
        continue
    
    fm_raw = fm_match.group(1)
    body = fm_match.group(2)
    
    meta = {}
    for line in fm_raw.splitlines():
        if ':' in line:
            k, v = line.split(':', 1)
            meta[k.strip()] = v.strip().strip('"\'')
            
    title = meta.get('title', '')
    slug = meta.get('slug', '')
    summary = meta.get('summary', '')
    category = meta.get('category', '')
    tags = meta.get('tags', '')
    date = meta.get('date', '')
    image = meta.get('image', '')
    author = meta.get('author', '')
    
    expected_slug = name.replace('.md', '')
    if slug != expected_slug:
        errors.append(f'{name}: slug is "{slug}", expected "{expected_slug}"')
        
    expected_img = f'assets/blog/{slug}-cover.webp'
    if image != expected_img:
        errors.append(f'{name}: image is "{image}", expected "{expected_img}"')
        
    if not os.path.exists(image):
        errors.append(f'{name}: image file "{image}" does not exist on disk!')
        
    # Check H1 in body
    if re.search(r'(?m)^#\s+[^#]', body):
        errors.append(f'{name}: Contains H1 in markdown body!')
        
    # Check word count
    words = len(re.findall(r'\b\w+\b', body))
    if words < 900 or words > 1350:
        errors.append(f'{name}: Word count {words} outside target range (900-1300)')
        
    stats.append({
        'name': name,
        'title': title,
        'title_len': len(title),
        'summary_len': len(summary),
        'words': words,
        'category': category,
        'author': author,
        'date': date
    })

print(f'\nVerification results ({len(stats)} files):')
for s in stats:
    print(f"- {s['name']}: {s['words']} words | Title({s['title_len']}): {s['title']} | Cat: {s['category']}")

if errors:
    print('\nERRORS FOUND:')
    for e in errors:
        print('  ERROR:', e)
else:
    print('\nALL POSTS PASSED VALIDATION PERFECTLY!')

