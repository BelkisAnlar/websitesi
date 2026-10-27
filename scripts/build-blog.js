const fs = require('fs');
const path = require('path');

const POSTS_DIR = path.join(__dirname, '..', 'posts');
const BLOG_DIR = path.join(__dirname, '..', 'blog');
const DATA_DIR = path.join(__dirname, '..', 'data');
const INDEX_FILE = path.join(DATA_DIR, 'blog-index.json');
const BASE_HTML_FILE = path.join(__dirname, '..', 'hakkimda.html');

if (!fs.existsSync(BLOG_DIR)) fs.mkdirSync(BLOG_DIR, { recursive: true });
if (!fs.existsSync(DATA_DIR)) fs.mkdirSync(DATA_DIR, { recursive: true });

const baseHtml = fs.readFileSync(BASE_HTML_FILE, 'utf8');

const headerMatch = baseHtml.match(/(<!DOCTYPE html>[\s\S]*?<\/header>)/i);
const footerMatch = baseHtml.match(/(<div class="custom-shape-divider-top-footer">[\s\S]*?<\/html>)/i);

let headerHtml = headerMatch ? headerMatch[1] : '';
let footerHtml = footerMatch ? footerMatch[1] : '';

function adjustPaths(html) {
  return html
    .replace(/href="(?!https?:\/\/|#|\/|\.\.\/)(.*?\.html)"/g, 'href="../$1"')
    .replace(/href="style\.css"/g, 'href="../style.css"')
    .replace(/src="assets\//g, 'src="../assets/')
    .replace(/href="assets\//g, 'href="../assets/');
}

headerHtml = adjustPaths(headerHtml);
footerHtml = adjustPaths(footerHtml);

function inlineFormat(txt) {
  return txt
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    .replace(/\*(.+?)\*/g, '<em>$1</em>')
    .replace(/`(.+?)`/g, '<code>$1</code>')
    .replace(/\[(.+?)\]\((.+?)\)/g, '<a href="$2">$1</a>');
}

function parseMarkdown(text) {
  const lines = text.trim().split(/\r?\n/);
  const htmlOut = [];
  let inTable = false;
  let tableRows = [];
  let inUl = false;
  let inOl = false;

  function closeTable() {
    if (inTable && tableRows.length) {
      const tbl = ['<div class="blog-table-wrapper"><table class="blog-table">'];
      const header = tableRows[0];
      tbl.push('<thead><tr>' + header.map(c => `<th>${inlineFormat(c)}</th>`).join('') + '</tr></thead><tbody>');
      for (let i = 1; i < tableRows.length; i++) {
        tbl.push('<tr>' + tableRows[i].map(c => `<td>${inlineFormat(c)}</td>`).join('') + '</tr>');
      }
      tbl.push('</tbody></table></div>');
      htmlOut.push(tbl.join('\n'));
      inTable = false;
      tableRows = [];
    }
  }

  function closeLists() {
    if (inUl) { htmlOut.push('</ul>'); inUl = false; }
    if (inOl) { htmlOut.push('</ol>'); inOl = false; }
  }

  for (const rawLine of lines) {
    const line = rawLine.trim();

    if (line.startsWith('|') && line.endsWith('|')) {
      closeLists();
      const cells = line.split('|').slice(1, -1).map(c => c.trim());
      if (cells.every(c => /^:?-+:?$/.test(c))) continue;
      if (!inTable) {
        inTable = true;
        tableRows = [cells];
      } else {
        tableRows.push(cells);
      }
      continue;
    } else {
      closeTable();
    }

    if (!line) {
      closeLists();
      continue;
    }

    if (line.startsWith('### ')) {
      closeLists();
      htmlOut.push(`<h3>${inlineFormat(line.slice(4))}</h3>`);
      continue;
    }
    if (line.startsWith('## ')) {
      closeLists();
      htmlOut.push(`<h2>${inlineFormat(line.slice(3))}</h2>`);
      continue;
    }
    if (line.startsWith('> ')) {
      closeLists();
      htmlOut.push(`<blockquote><p>${inlineFormat(line.slice(2))}</p></blockquote>`);
      continue;
    }
    if (line.startsWith('- ') || line.startsWith('* ')) {
      if (inOl) { htmlOut.push('</ol>'); inOl = false; }
      if (!inUl) { htmlOut.push('<ul>'); inUl = true; }
      htmlOut.push(`<li>${inlineFormat(line.slice(2))}</li>`);
      continue;
    }
    const olMatch = line.match(/^(\d+)\.\s+(.*)$/);
    if (olMatch) {
      if (inUl) { htmlOut.push('</ul>'); inUl = false; }
      if (!inOl) { htmlOut.push('<ol>'); inOl = true; }
      htmlOut.push(`<li>${inlineFormat(olMatch[2])}</li>`);
      continue;
    }

    closeLists();
    htmlOut.push(`<p>${inlineFormat(line)}</p>`);
  }

  closeTable();
  closeLists();
  return htmlOut.join('\n');
}

const mdFiles = fs.readdirSync(POSTS_DIR).filter(f => f.endsWith('.md')).sort();
const indexData = [];

for (const filename of mdFiles) {
  const content = fs.readFileSync(path.join(POSTS_DIR, filename), 'utf8');
  const match = content.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n([\s\S]*)$/);
  if (!match) continue;

  const fmRaw = match[1];
  const bodyRaw = match[2];

  const meta = {};
  for (const line of fmRaw.split(/\r?\n/)) {
    const kv = line.match(/^([^:]+):\s*(.*)$/);
    if (kv) {
      const k = kv[1].trim();
      let v = kv[2].trim();
      if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) {
        v = v.slice(1, -1);
      }
      meta[k] = v;
    }
  }

  const slug = meta.slug || path.basename(filename, '.md');
  const title = meta.title || '';
  const summary = meta.summary || '';
  const category = meta.category || 'Eğitim';
  const tags = meta.tags || '';
  const date = meta.date || '2026-10-27';
  const image = `assets/blog/${slug}-cover.webp`;
  const author = meta.author || 'Beytullah Çekik';

  indexData.push({ slug, title, summary, category, tags, date, image, author });

  const htmlBody = parseMarkdown(bodyRaw);

  let postHead = headerHtml
    .replace(/<title>.*?<\/title>/i, `<title>${title} | Beytullah Çekik Blog</title>`)
    .replace(/<meta name="description" content=".*?"/i, `<meta name="description" content="${summary}"`)
    .replace(/<link rel="canonical" href=".*?" \/>/i, `<link rel="canonical" href="https://beytullahcekik.com/blog/${slug}.html" />`);

  const hero = `
<!-- Hero Section with Organic Wave -->
<section class="post-detail-hero">
  <div class="container">
    <div class="post-breadcrumbs" data-aos="fade-down">
      <a href="../index.html">Ana Sayfa</a>
      <span class="sep"><i class="fas fa-chevron-right"></i></span>
      <a href="../blog.html">Blog</a>
      <span class="sep"><i class="fas fa-chevron-right"></i></span>
      <span>${category}</span>
    </div>
    <h1 data-aos="fade-up">${title}</h1>
    <div class="post-meta-bar" data-aos="fade-up" data-aos-delay="150">
      <span class="post-category-badge">${category}</span>
      <span><i class="far fa-calendar-alt"></i> ${date}</span>
      <span><i class="far fa-clock"></i> 5 dk okuma</span>
      <span><i class="fas fa-user-check"></i> ${author}</span>
    </div>
  </div>
  <div class="custom-shape-divider-bottom">
    <svg data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" preserveAspectRatio="none">
        <path d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V120H0V95.8C59.71,118.08,130.83,119.3,191.9,106.1,236.4,96.53,279.7,76.51,321.39,56.44Z" class="shape-fill"></path>
    </svg>
  </div>
</section>
`;

  const imgBase = `../${image}`;
  const encodedTitle = encodeURIComponent(title);

  const detailContent = `
<!-- Main Article Section -->
<main class="post-article-container" data-aos="fade-up">
  <!-- Featured Image -->
  <div class="post-featured-image">
    <picture>
      <source srcset="${imgBase} 800w, ${imgBase} 1200w" type="image/webp" sizes="(max-width: 768px) 100vw, 920px">
      <img src="${imgBase}" alt="${title}" loading="lazy">
    </picture>
  </div>

  <!-- Content Card -->
  <article class="post-article-card">
    <div class="post-content-body blog-detail-content">
      ${htmlBody}
    </div>

    <!-- Call To Action -->
    <div class="post-consult-cta">
      <h3>Köpeğiniz İçin Profesyonel Destek Alın</h3>
      <p>İzmir'de yerinde pozitif ve dengeli köpek eğitimi, temel/ileri itaat ve davranış rehabilitasyonu için Beytullah Çekik ile iletişime geçin.</p>
      <a href="https://wa.me/905538860237?text=Merhaba,%20'${encodedTitle}'%20yazınızı%20okudum%20ve%20danışmak%20istediğim%20bir%20konu%20var." target="_blank" rel="noopener noreferrer" class="btn-whatsapp-services" style="display: inline-flex; width: auto; padding: 14px 32px; border-radius: 50px;">
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
`;

  const finalHtml = postHead + hero + detailContent + footerHtml;
  fs.writeFileSync(path.join(BLOG_DIR, `${slug}.html`), finalHtml, 'utf8');
}

fs.writeFileSync(INDEX_FILE, JSON.stringify(indexData, null, 2), 'utf8');
console.log(`Build script completed successfully! Generated ${indexData.length} posts.`);
