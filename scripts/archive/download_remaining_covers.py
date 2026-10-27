import os
import urllib.request
from PIL import Image

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

DOWNLOADS = {
    'kopegim-neden-surekli-kokluyor': 'https://images.unsplash.com/photo-1687959258212-7fbd439915e6?auto=format&fit=crop&w=1200&q=80',
    'kopegim-neden-surekli-uzerime-atliyor': 'https://upload.wikimedia.org/wikipedia/commons/4/41/Dog_Standing_Owner.jpg',
    'kopegim-neden-titriyor': 'https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?auto=format&fit=crop&w=1200&q=80',
    'kopegim-neden-uluyor': 'https://upload.wikimedia.org/wikipedia/commons/d/d2/Dog_howling_001.jpg',
    'kopegim-neden-yabancilardan-korkuyor': 'https://upload.wikimedia.org/wikipedia/commons/1/1a/Scared_dog.jpg',
    'kopeklerde-ayrilik-kaygisi': 'https://images.unsplash.com/photo-1655210912171-c53b1b2f95ad?auto=format&fit=crop&w=1200&q=80',
    'ornek-yazi': 'https://upload.wikimedia.org/wikipedia/commons/f/fb/Military_working_dog_rewarded_during_training_%289551982%29.jpg'
}

OUTPUT_DIR = r'assets\blog'
os.makedirs(OUTPUT_DIR, exist_ok=True)

for slug, url in DOWNLOADS.items():
    dst_path = os.path.join(OUTPUT_DIR, f'{slug}-cover.webp')
    tmp_path = os.path.join(OUTPUT_DIR, f'{slug}-temp.jpg')
    print(f'Fetching for {slug}...')
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = resp.read()
        
        with open(tmp_path, 'wb') as f:
            f.write(data)
            
        with Image.open(tmp_path) as img:
            if img.mode != 'RGB':
                img = img.convert('RGB')
            w, h = img.size
            if w > 1200:
                new_h = int(h * (1200 / w))
                img = img.resize((1200, new_h), Image.Resampling.LANCZOS)
                
            q = 85
            while q >= 20:
                img.save(dst_path, 'WEBP', quality=q, optimize=True)
                size_kb = os.path.getsize(dst_path) / 1024
                if size_kb <= 140:
                    break
                q -= 5
                
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
            
        print(f'Successfully saved {slug}-cover.webp: {size_kb:.1f} KB (quality {q})')
    except Exception as e:
        print(f'Error processing {slug}: {e}')
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
