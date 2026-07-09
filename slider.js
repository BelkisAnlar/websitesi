// Services Data Array
const serviceData = [
  {
    index: 0,
    title: "Yavru Köpek Eğitimi",
    longDesc: `<p><strong>Teknik:</strong> Pozitif pekiştirme ve oyun tabanlı öğrenme yöntemleri kullanılır. Ceza veya zorlama kesinlikle yoktur.</p>
               <p><strong>Süreç:</strong> 2-6 aylık yavrular için karakter analizi, sosyalleşme, tuvalet alışkanlığı ve ev içi kuralların oturtulması. Yavrunuzun dikkat süresine uygun kısa seanslar halinde temel itaat (otur, bekle, gel) adımları işlenir.</p>`,
    testimonialText: "Yavru köpeğimiz Lokum eve geldiğinde ne yapacağımızı bilmiyorduk. Beytullah Bey sayesinde tuvalet eğitimini ve ev kurallarını stressiz öğrendik. Şimdi çok uyumlu bir aile üyesiyiz!",
    testimonialAuthor: "Zeynep T. (Lokum'un Sahibi)",
    imageSrc: "assets/service_puppy.webp"
  },
  {
    index: 1,
    title: "Temel İtaat Eğitimi",
    longDesc: `<p><strong>Teknik:</strong> Tıklama (clicker) eğitimi, işaretleme ve ödül odaklı yönlendirmelerle sevk kayışlı (tasmalı) kontrol sağlanır.</p>
               <p><strong>Süreç:</strong> Yaklaşık 4-6 hafta sürer. Köpeğinizin sokakta çekiştirmeden yürümesi, komutları dinlemesi ve dış uyarıcılara karşı sakin kalması hedeflenir. 'Otur, Yat, Bekle, Gel, Takip' gibi komutların tasmalı olarak öğretilmesi ve sokak adaptasyonu sağlanır.</p>`,
    testimonialText: "Tasmasını çekiştirmekten yürüyemediğimiz köpeğimiz Odin, temel itaat eğitiminden sonra yanımızda kuğu gibi yürümeye başladı. Artık sokak yürüyüşlerimiz işkence değil, keyif haline geldi.",
    testimonialAuthor: "Ahmet K. (Odin'in Sahibi)",
    imageSrc: "assets/service_basic.jpg"
  },
  {
    index: 2,
    title: "İleri İtaat Eğitimi",
    longDesc: `<p><strong>Teknik:</strong> Ses tonu ve beden dili hakimiyeti, ileri düzey işaret eğitimi ve yüksek motivasyon.</p>
               <p><strong>Süreç:</strong> Temel itaati başarıyla tamamlamış köpekler için uygulanır. Uzaktan komut verme, tasmasız serbest yürüyüş ve zorlu dış uyarıcılar altında mükemmel odaklanma becerileri kazandırılır.</p>`,
    testimonialText: "Köpeğimizi tasmasız bırakmaya hiç cesaret edemezdik. İleri itaat eğitiminden sonra en kalabalık parklarda bile tek bir sözümüzle yanımıza dönüyor. Özgürlüğün tadını çıkarıyoruz.",
    testimonialAuthor: "Merve Y. (Badi'nin Sahibi)",
    imageSrc: "assets/service_advanced.jpg"
  },
  {
    index: 3,
    title: "Tuvalet Eğitimi",
    longDesc: `<p><strong>Teknik:</strong> Alan sınırlandırma (crate training), zamanlama takibi ve pozitif pekiştirme.</p>
               <p><strong>Süreç:</strong> Köpeğinizin yaşına, ırkına ve sindirim sistemine göre kişiselleştirilmiş bir rutin oluşturulur. Doğru yere tuvaletini yaptığında anında ödüllendirilerek kalıcı ve temiz bir alışkanlık pekiştirilir.</p>`,
    testimonialText: "Yeni sahiplendiğimiz köpeğimizin tuvalet sorunu bizi canımızdan bezdirmişti. Doğru rutin ve yaklaşımla sadece 10 günde problemi tamamen çözdük. Teşekkürler!",
    testimonialAuthor: "Caner B. (Dobby'nin Sahibi)",
    imageSrc: "assets/service_potty.webp"
  },
  {
    index: 4,
    title: "Davranış Bozukluğu Eğitimi",
    longDesc: `<p><strong>Teknik:</strong> Davranış modifikasyonu, duyarsızlaştırma (desensitization) ve karşıt koşullanma.</p>
               <p><strong>Süreç:</strong> Sorunun kök nedeni (korku, stres, güvensizlik vb.) detaylıca analiz edilir. Havlama, ısırma, ayrılık kaygısı veya agresyon gibi istenmeyen davranışları tetikleyen unsurlar belirlenip köpeğin kademeli olarak doğru davranışa yönlendirilmesi sağlanır.</p>`,
    testimonialText: "Misafirlere karşı aşırı agresif ve havlayan köpeğimiz için umudu kesmiştik. Davranış modifikasyonu sayesinde şimdi evimize gelen misafirleri sakince karşılıyor.",
    testimonialAuthor: "Ece D. (Papi'nin Sahibi)",
    imageSrc: "assets/service_behavior.webp"
  },
  {
    index: 5,
    title: "Alan Koruma Eğitimi",
    longDesc: `<p><strong>Teknik:</strong> Güdü yönlendirme, kontrollü havlama ve doğru tehdit algısı oluşturma.</p>
               <p><strong>Süreç:</strong> Köpeğin genetik yatkınlığı ve özgüveni incelenir. Sadece gerçek tehditlere karşı reaksiyon vermesi, sahte uyarıcılara tepkisiz kalması ve en önemlisi sahibinin 'Bırak/Dur' komutuyla anında sakinleşmesi öğretilir.</p>`,
    testimonialText: "Fabrikamızın güvenliği için eğittiğimiz Alman Çoban Köpeğimiz, artık yabancıları anında fark edip uyarıyor ama bizim komutumuzla hemen sakinleşiyor. Harika bir denge!",
    testimonialAuthor: "Selim A. (Fabrika Müdürü)",
    imageSrc: "assets/service_area_guard.webp"
  },
  {
    index: 6,
    title: "Kişi Koruma Eğitimi",
    longDesc: `<p><strong>Teknik:</strong> Avlanma ve savunma güdülerinin dengeli kullanımı, senaryo bazlı simülasyonlar.</p>
               <p><strong>Süreç:</strong> Yüksek özgüven ve ileri itaat seviyesi şarttır. Köpek, sahibini veya belirtilen kişiyi tehlike anında aktif olarak korumayı, tehdit ortadan kalktığında veya komut verildiğinde anında eylemi sonlandırmayı öğrenir.</p>`,
    testimonialText: "Tehdit oluşturabilecek durumlarda köpeğimin beni koruyabileceğini bilmek inanılmaz bir güven veriyor. Üstelik günlük hayatta hala çok uysal ve sevecen.",
    testimonialAuthor: "Hakan S. (İş İnsanı)",
    imageSrc: "assets/service_personal_guard.jpg"
  },
  {
    index: 7,
    title: "İş ve Spor Köpekleri Eğitimi",
    longDesc: `<p><strong>Teknik:</strong> Yüksek motivasyon (drive), oyuncak odaklı çalışma ve ileri düzey fiziksel kondisyon.</p>
               <p><strong>Süreç:</strong> IGP, Agility (çeviklik), K-9 veya arama kurtarma branşlarına yönelik özel antrenmanlar uygulanır. Köpeğin fiziksel sınırlarını, çevikliğini ve iş zekasını maksimum kapasitede kullanmasını sağlayan profesyonel bir süreçtir.</p>`,
    testimonialText: "Sınır tanımayan enerjisiyle baş edemediğimiz köpeğimizle agility sporu yapmaya başladık. Hem onun zihni dengelendi hem de aramızdaki bağ bambaşka bir boyuta taşındı.",
    testimonialAuthor: "Aylin T. (Shadow'un Sahibi)",
    imageSrc: "assets/service_sport.jpg"
  }
];

// Selectors
const serviceCards = document.querySelectorAll('.service-card');
const mobileTabs = document.querySelectorAll('.mobile-tab');
const centerStage = document.querySelector('.services-center-stage');
const centerImage = document.getElementById('centerServiceImage');
const centerTitle = document.getElementById('centerServiceTitle');
const centerLongDesc = document.getElementById('centerServiceLongDesc');
const centerCta = document.getElementById('centerServiceCta');

let currentActiveIndex = 0;

// Update Center Stage function
function updateCenterStage(index) {
  if (index < 0 || index >= serviceData.length) return;
  
  const data = serviceData[index];
  
  // 1. Add changing class to trigger CSS fade-out & translateY transition
  centerStage.classList.add('changing');
  
  // 2. Wait for transition to complete, then update content & fade-in
  setTimeout(() => {
    // Update elements
    centerImage.src = data.imageSrc;
    centerImage.alt = data.title;
    centerTitle.innerText = data.title;
    centerLongDesc.innerHTML = data.longDesc;
    
    // Update WhatsApp CTA Link with dynamic encoded message
    const encodedMessage = encodeURIComponent(`Merhaba, ${data.title} hakkında detaylı bilgi almak istiyorum.`);
    centerCta.href = `https://wa.me/905538860237?text=${encodedMessage}`;
    
    // Remove changing class to trigger fade-in & slide-up animation
    centerStage.classList.remove('changing');
  }, 350); // Matches the CSS transition time of 0.35s
}

// Set Active states for cards and tabs
function setActiveIndex(index) {
  currentActiveIndex = index;
  
  // Update desktop cards active class
  serviceCards.forEach(card => {
    if (parseInt(card.getAttribute('data-index')) === index) {
      card.classList.add('active');
    } else {
      card.classList.remove('active');
    }
  });
  
  // Update mobile tabs active class
  const tabsContainer = document.querySelector('.services-mobile-tabs');
  mobileTabs.forEach(tab => {
    if (parseInt(tab.getAttribute('data-index')) === index) {
      tab.classList.add('active');
      // Custom scroll to prevent page-level horizontal shifting
      if (tabsContainer) {
        const scrollLeft = tab.offsetLeft - (tabsContainer.offsetWidth / 2) + (tab.offsetWidth / 2);
        tabsContainer.scrollTo({ left: scrollLeft, behavior: 'smooth' });
      }
    } else {
      tab.classList.remove('active');
    }
  });
  
  // Update center stage dynamic content
  updateCenterStage(index);
}

// Event Listeners for Desktop Cards
serviceCards.forEach(card => {
  card.addEventListener('click', () => {
    const index = parseInt(card.getAttribute('data-index'));
    if (index !== currentActiveIndex) {
      setActiveIndex(index);
    }
  });
});

// Event Listeners for Mobile Tabs
mobileTabs.forEach(tab => {
  tab.addEventListener('click', () => {
    const index = parseInt(tab.getAttribute('data-index'));
    if (index !== currentActiveIndex) {
      setActiveIndex(index);
    }
  });
});

// Initialize on Load
document.addEventListener('DOMContentLoaded', () => {
  // Check if we already have the DOM loaded
  setActiveIndex(0);
});

// Run immediately as well in case script is loaded deferred or after DOMContentLoaded
if (document.readyState === 'interactive' || document.readyState === 'complete') {
  setActiveIndex(0);
}
