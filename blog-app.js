document.addEventListener('DOMContentLoaded', () => {
  const searchInput = document.getElementById('blogSearchInput');
  const blogListContainer = document.getElementById('blogListContainer');
  const emptyState = document.getElementById('emptyState');
  const resetBtn = document.getElementById('resetSearchBtn');
  const categoryFilters = document.getElementById('categoryFilters');
  
  if (!searchInput || !blogListContainer) return;

  let allPosts = [];
  let currentCategory = 'Tümü';
  let debounceTimer;

  const normalizeSearchText = (text) => {
    if (!text) return '';
    return text.toLocaleLowerCase('tr-TR')
      .replace(/ğ/g, 'g')
      .replace(/ü/g, 'u')
      .replace(/ş/g, 's')
      .replace(/ı/g, 'i')
      .replace(/ö/g, 'o')
      .replace(/ç/g, 'c');
  };

  const renderCards = (posts) => {
    if (posts.length === 0) {
      blogListContainer.style.display = 'none';
      if (emptyState) emptyState.style.display = 'block';
    } else {
      if (emptyState) emptyState.style.display = 'none';
      blogListContainer.style.display = 'grid';
      
      let html = '';
      posts.forEach(post => {
        const cat = post.category || 'Rehber';
        const date = post.date || 'Ekim 2026';
        const author = post.author || 'Beytullah Çekik';
        const img = post.image || 'assets/blog/ornek-yazi-cover.webp';
        const targetUrl = post.slug === 'ornek-yazi' ? 'blog/ornek-yazi.html' : `blog/${post.slug}.html`;

        html += `
        <article class="blog-card-modern" data-aos="fade-up">
          <div class="blog-card-modern-thumb">
            <span class="blog-card-category-tag">${cat}</span>
            <img src="${img}" alt="${post.title}" loading="lazy">
          </div>
          <div class="blog-card-modern-body">
            <div class="blog-card-meta">
              <span><i class="far fa-calendar-alt"></i> ${date}</span>
              <span>•</span>
              <span><i class="far fa-clock"></i> 4-5 dk</span>
            </div>
            <h3 class="blog-card-modern-title">${post.title}</h3>
            <p class="blog-card-modern-excerpt">${post.summary}</p>
            <div class="blog-card-modern-footer">
              <span class="blog-card-author"><i class="fas fa-user-check"></i> ${author}</span>
              <a href="${targetUrl}" class="blog-card-read-link">Devamını Oku <i class="fas fa-arrow-right"></i></a>
            </div>
          </div>
        </article>`;
      });
      blogListContainer.innerHTML = html;
    }
  };
  
  const renderCategories = () => {
    if (!categoryFilters) return;
    const categories = ['Tümü', ...new Set(allPosts.map(p => p.category).filter(Boolean))];
    let html = '';
    categories.forEach(cat => {
      const activeClass = cat === currentCategory ? 'active' : '';
      html += `<button type="button" class="blog-category-pill ${activeClass}" data-cat="${cat}">${cat}</button>`;
    });
    categoryFilters.innerHTML = html;
    
    categoryFilters.querySelectorAll('button').forEach(btn => {
      btn.addEventListener('click', (e) => {
        categoryFilters.querySelectorAll('button').forEach(b => b.classList.remove('active'));
        const targetBtn = e.currentTarget;
        targetBtn.classList.add('active');
        currentCategory = targetBtn.getAttribute('data-cat');
        filterPosts();
      });
    });
  };

  const filterPosts = () => {
    const query = normalizeSearchText(searchInput.value).trim();
    
    const results = allPosts.filter(post => {
      const matchCat = currentCategory === 'Tümü' || post.category === currentCategory;
      if (!matchCat) return false;
      
      if (!query) return true;
      
      const normTitle = normalizeSearchText(post.title);
      const normSummary = normalizeSearchText(post.summary);
      const normTags = normalizeSearchText(Array.isArray(post.tags) ? post.tags.join(' ') : (post.tags || ''));
      return normTitle.includes(query) || normSummary.includes(query) || normTags.includes(query);
    });
    
    renderCards(results);
  };

  searchInput.addEventListener('input', () => {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(filterPosts, 250);
  });

  if (resetBtn) {
    resetBtn.addEventListener('click', () => {
      searchInput.value = '';
      currentCategory = 'Tümü';
      renderCategories();
      filterPosts();
    });
  }

  fetch('data/blog-index.json')
    .then(res => {
      if (!res.ok) throw new Error('HTTP error ' + res.status);
      return res.json();
    })
    .then(data => {
      allPosts = data;
      // Also ensure ornek-yazi is in the list if not present
      if (!allPosts.some(p => p.slug === 'ornek-yazi')) {
        allPosts.unshift({
          slug: 'ornek-yazi',
          title: 'Pozitif Pekiştirme ile Köpek Eğitimi Nasıl Yapılır?',
          summary: 'Pozitif pekiştirme odaklı köpek eğitimi teknikleri, ödül maması zamanlaması ve köpeğinizle güven dolu bir bağ kurmanın altın kuralları.',
          category: 'Eğitim',
          tags: 'pozitif pekiştirme, ödül maması, eğitim',
          date: '27 Ekim 2026',
          image: 'assets/blog/ornek-yazi-cover.webp',
          author: 'Beytullah Çekik'
        });
      }
      renderCategories();
      renderCards(allPosts);
    })
    .catch(err => {
      console.warn('Veri fetch edilirken veya yerel protokolde:', err);
      // If run locally without a web server or fetch blocked, ensure fallback template card is shown
      if (allPosts.length === 0) {
        allPosts = [
          {
            slug: 'ornek-yazi',
            title: 'Pozitif Pekiştirme ile Köpek Eğitimi Nasıl Yapılır?',
            summary: 'Pozitif pekiştirme odaklı köpek eğitimi teknikleri, ödül maması zamanlaması ve köpeğinizle güven dolu bir bağ kurmanın altın kuralları.',
            category: 'Eğitim',
            tags: 'pozitif pekiştirme, ödül maması, eğitim',
            date: '27 Ekim 2026',
            image: 'assets/blog/ornek-yazi-cover.webp',
            author: 'Beytullah Çekik'
          }
        ];
        renderCategories();
        renderCards(allPosts);
      }
    });
});