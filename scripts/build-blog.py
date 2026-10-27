import os
import re
import json
import urllib.parse

POSTS_DIR = "posts"
BLOG_DIR = "blog"
DATA_DIR = "data"
INDEX_FILE = os.path.join(DATA_DIR, "blog-index.json")

os.makedirs(BLOG_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)

with open("hakkimda.html", "r", encoding="utf-8") as f:
    base_html = f.read()

# Extract Header & Footer
header_match = re.search(r"(?is)(<!DOCTYPE html>.*?</header>)", base_html)
footer_match = re.search(r"(?is)(<div class=\"custom-shape-divider-top-footer\">.*?</html>)", base_html)

header_html = header_match.group(1) if header_match else ""
footer_html = footer_match.group(1) if footer_match else ""

# Adjust relative paths for /blog/
def adjust_paths(html):
    html = re.sub(r'href="(?!https?://|#|/|\.\./)(.*?\.html)"', r'href="../\1"', html)
    html = re.sub(r'href="style\.css"', r'href="../style.css"', html)
    html = re.sub(r'src="assets/', r'src="../assets/', html)
    html = re.sub(r'href="assets/', r'href="../assets/', html)
    return html

header_html = adjust_paths(header_html)
footer_html = adjust_paths(footer_html)

def parse_markdown(text):
    lines = text.strip().split("\n")
    html_out = []
    in_table = False
    table_rows = []
    in_ul = False
    in_ol = False

    def close_table():
        nonlocal in_table, table_rows
        if in_table and table_rows:
            tbl_html = ['<div class="blog-table-wrapper"><table class="blog-table">']
            header = table_rows[0]
            tbl_html.append("<thead><tr>")
            for cell in header:
                tbl_html.append(f"<th>{inline_format(cell)}</th>")
            tbl_html.append("</tr></thead><tbody>")
            for row in table_rows[1:]:
                tbl_html.append("<tr>")
                for cell in row:
                    tbl_html.append(f"<td>{inline_format(cell)}</td>")
                tbl_html.append("</tr>")
            tbl_html.append("</tbody></table></div>")
            html_out.append("\n".join(tbl_html))
            in_table = False
            table_rows = []

    def close_lists():
        nonlocal in_ul, in_ol
        if in_ul:
            html_out.append("</ul>")
            in_ul = False
        if in_ol:
            html_out.append("</ol>")
            in_ol = False

    for line in lines:
        line_str = line.strip()

        # Check table
        if line_str.startswith("|") and line_str.endswith("|"):
            close_lists()
            cells = [c.strip() for c in line_str.split("|")[1:-1]]
            # separator row like |--|--|
            if all(re.match(r"^:?-+:?$", c) for c in cells):
                continue
            if not in_table:
                in_table = True
                table_rows = [cells]
            else:
                table_rows.append(cells)
            continue
        else:
            close_table()

        if not line_str:
            close_lists()
            continue

        # Headings
        if line_str.startswith("### "):
            close_lists()
            content = inline_format(line_str[4:])
            html_out.append(f"<h3>{content}</h3>")
            continue
        if line_str.startswith("## "):
            close_lists()
            content = inline_format(line_str[3:])
            html_out.append(f"<h2>{content}</h2>")
            continue

        # Blockquote
        if line_str.startswith("> "):
            close_lists()
            content = inline_format(line_str[2:])
            html_out.append(f"<blockquote><p>{content}</p></blockquote>")
            continue

        # Unordered list
        if line_str.startswith("- ") or line_str.startswith("* "):
            if in_ol:
                html_out.append("</ol>")
                in_ol = False
            if not in_ul:
                html_out.append("<ul>")
                in_ul = True
            content = inline_format(line_str[2:])
            html_out.append(f"<li>{content}</li>")
            continue

        # Ordered list
        m_ol = re.match(r"^(\d+)\.\s+(.*)$", line_str)
        if m_ol:
            if in_ul:
                html_out.append("</ul>")
                in_ul = False
            if not in_ol:
                html_out.append("<ol>")
                in_ol = True
            content = inline_format(m_ol.group(2))
            html_out.append(f"<li>{content}</li>")
            continue

        # Paragraph
        close_lists()
        content = inline_format(line_str)
        html_out.append(f"<p>{content}</p>")

    close_table()
    close_lists()
    return "\n".join(html_out)

def inline_format(txt):
    txt = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", txt)
    txt = re.sub(r"\*(.+?)\*", r"<em>\1</em>", txt)
    txt = re.sub(r"`(.+?)`", r"<code>\1</code>", txt)
    txt = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', txt)
    return txt

index_data = []

md_files = [f for f in os.listdir(POSTS_DIR) if f.endswith(".md")]
md_files.sort()

for filename in md_files:
    filepath = os.path.join(POSTS_DIR, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    m = re.match(r"(?s)^---\r?\n(.*?)\r?\n---\r?\n(.*)$", content)
    if not m:
        continue

    fm_raw = m.group(1)
    body_raw = m.group(2)

    meta = {}
    for line in fm_raw.splitlines():
        line = line.strip()
        kv = re.match(r"^([^:]+):\s*(.*)$", line)
        if kv:
            k = kv.group(1).strip()
            v = kv.group(2).strip()
            if (v.startswith('"') and v.endswith('"')) or (v.startswith("'") and v.endswith("'")):
                v = v[1:-1]
            meta[k] = v

    slug = meta.get("slug", os.path.splitext(filename)[0])
    title = meta.get("title", "")
    summary = meta.get("summary", "")
    category = meta.get("category", "Eğitim")
    tags = meta.get("tags", "")
    date = meta.get("date", "2026-10-27")
    image = f"assets/blog/{slug}-cover.webp"
    author = meta.get("author", "Beytullah Çekik")

    index_data.append({
        "slug": slug,
        "title": title,
        "summary": summary,
        "category": category,
        "tags": tags,
        "date": date,
        "image": image,
        "author": author
    })

    html_body = parse_markdown(body_raw)

    post_head = header_html
    post_head = re.sub(r"<title>.*?</title>", f"<title>{title} | Beytullah Çekik Blog</title>", post_head)
    post_head = re.sub(r'<meta name="description" content=".*?"', f'<meta name="description" content="{summary}"', post_head)
    post_head = re.sub(r'<link rel="canonical" href=".*?" />', f'<link rel="canonical" href="https://beytullahcekik.com/blog/{slug}.html" />', post_head)

    hero = f"""
<!-- Hero Section with Organic Wave -->
<section class="post-detail-hero">
  <div class="container">
    <div class="post-breadcrumbs" data-aos="fade-down">
      <a href="../index.html">Ana Sayfa</a>
      <span class="sep"><i class="fas fa-chevron-right"></i></span>
      <a href="../blog.html">Blog</a>
      <span class="sep"><i class="fas fa-chevron-right"></i></span>
      <span>{category}</span>
    </div>
    <h1 data-aos="fade-up">{title}</h1>
    <div class="post-meta-bar" data-aos="fade-up" data-aos-delay="150">
      <span class="post-category-badge">{category}</span>
      <span><i class="far fa-calendar-alt"></i> {date}</span>
      <span><i class="far fa-clock"></i> 5 dk okuma</span>
      <span><i class="fas fa-user-check"></i> {author}</span>
    </div>
  </div>
  <div class="custom-shape-divider-bottom">
    <svg data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" preserveAspectRatio="none">
        <path d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V120H0V95.8C59.71,118.08,130.83,119.3,191.9,106.1,236.4,96.53,279.7,76.51,321.39,56.44Z" class="shape-fill"></path>
    </svg>
  </div>
</section>
"""

    img_base = f"../{image}"
    encoded_title = urllib.parse.quote(title)

    detail_content = f"""
<!-- Main Article Section -->
<main class="post-article-container" data-aos="fade-up">
  <!-- Featured Image -->
  <div class="post-featured-image">
    <picture>
      <source srcset="{img_base} 800w, {img_base} 1200w" type="image/webp" sizes="(max-width: 768px) 100vw, 920px">
      <img src="{img_base}" alt="{title}" loading="lazy">
    </picture>
  </div>

  <!-- Content Card -->
  <article class="post-article-card">
    <div class="post-content-body blog-detail-content">
      {html_body}
    </div>

    <!-- Call To Action -->
    <div class="post-consult-cta">
      <h3>Köpeğiniz İçin Profesyonel Destek Alın</h3>
      <p>İzmir'de yerinde pozitif ve dengeli köpek eğitimi, temel/ileri itaat ve davranış rehabilitasyonu için Beytullah Çekik ile iletişime geçin.</p>
      <a href="https://wa.me/905538860237?text=Merhaba,%20'{encoded_title}'%20yazınızı%20okudum%20ve%20danışmak%20istediğim%20bir%20konu%20var." target="_blank" rel="noopener noreferrer" class="btn-whatsapp-services" style="display: inline-flex; width: auto; padding: 14px 32px; border-radius: 50px;">
        <i class="fab fa-whatsapp"></i> WhatsApp ile Bilgi Al
      </a>
    </div>

    <!-- Bottom Navigation -->
    <div class="post-bottom-nav">
      <a href="../blog.html" class="post-nav-btn-back">
        <i class="fas fa-arrow-left"></i> Tüm Blog Yazılarına Dön
      </a>
      <a href="../index.html#services" class="post-nav-btn-services">
        <i class="fas fa-paw"></i> Eğitimlerimiz
      </a>
    </div>
  </article>
</main>
"""

    final_html = post_head + hero + detail_content + footer_html

    out_path = os.path.join(BLOG_DIR, f"{slug}.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(final_html)

with open(INDEX_FILE, "w", encoding="utf-8") as f:
    json.dump(index_data, f, ensure_ascii=False, indent=2)

print(f"Build script completed successfully! Generated {len(index_data)} posts.")
