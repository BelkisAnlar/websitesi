import os
from PIL import Image

ASSETS_DIR = r"assets"
BLOG_ASSETS_DIR = r"assets\blog"

os.makedirs(BLOG_ASSETS_DIR, exist_ok=True)

MAPPINGS = {
    "kopegim-neden-beni-takip-ediyor": "promo_hug_colored.jpg",
    "kopegim-neden-diger-kopeklere-saldiriyor": "service_personal_guard.jpg",
    "kopegim-neden-elimi-yaliyor": "trainer_about.jpg",
    "kopegim-neden-esyalara-zarar-veriyor": "service_behavior.webp",
    "kopegim-neden-gece-havliyor": "about_bg.jpg",
    "kopegim-neden-insanlara-havliyor": "service_area_guard.webp",
    "kopegim-neden-isiriyor": "service_sport.jpg",
    "kopegim-neden-kaziyor": "trainers.jpg",
    "kopegim-neden-kendi-patisini-yaliyor": "service_basic.webp",
    "kopegim-neden-kuyrugunu-kovaliyor": "service_puppy.webp",
    "kopegim-neden-saklaniyor": "service_behavior.webp",
    "kopegim-neden-surekli-havliyor": "service_area_guard.webp",
    "kopegim-neden-surekli-kokluyor": "trainers.jpg",
    "kopegim-neden-surekli-uzerime-atliyor": "service_advanced.jpg",
    "kopegim-neden-titriyor": "service_behavior.webp",
    "kopegim-neden-uluyor": "service_area_guard.webp",
    "kopegim-neden-yabancilardan-korkuyor": "trainer_about.jpg",
    "kopeklerde-ayrilik-kaygisi": "promo_hug_colored.jpg",
    "ornek-yazi": "service_puppy.webp",
    "yavru-kopeklerde-tuvalet-egitimi": "service_potty.webp",
}

for slug, src_name in MAPPINGS.items():
    src_path = os.path.join(ASSETS_DIR, src_name)
    dest_path = os.path.join(BLOG_ASSETS_DIR, f"{slug}-cover.webp")
    
    if not os.path.exists(src_path):
        print(f"Warning: {src_path} not found!")
        continue
        
    with Image.open(src_path) as img:
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
            
        w, h = img.size
        if w > 1200:
            new_h = int(h * (1200 / w))
            img = img.resize((1200, new_h), Image.Resampling.LANCZOS)
            
        quality = 85
        while quality >= 20:
            img.save(dest_path, "WEBP", quality=quality, optimize=True)
            size_kb = os.path.getsize(dest_path) / 1024
            if size_kb <= 145:
                break
            quality -= 5
            
        print(f"Generated {os.path.basename(dest_path)}: {size_kb:.1f} KB (quality: {quality})")

print("All covers processed successfully!")
