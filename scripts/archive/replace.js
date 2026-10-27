const fs = require('fs');

const htmlContent = fs.readFileSync('index.html', 'utf8');

const newSliderHtml = `      <!-- Part 1: Trainings Slider -->
      <div class="services-slider-wrapper" data-aos="fade-up">
        <div class="slider-container" id="servicesSlider">
          <button class="slider-btn prev-btn" id="sliderPrevBtn"><i class="fas fa-chevron-left"></i></button>
          
          <div class="slider-track" id="sliderTrack">
            <!-- Card 0 -->
            <div class="slider-card" data-index="0" onclick="goToSlide(0)">
              <img src="assets/service_puppy.webp" alt="Yavru Köpek Eğitimi">
              <h3>Yavru Köpek Eğitimi</h3>
              <div class="hidden-desc short-desc">Temel kurallar ve sosyalleşme ile yavrunuzun hayata güvenle adım atmasını sağlıyoruz.</div>
              <div class="hidden-desc long-desc">
                <p><strong>Teknik:</strong> Pozitif pekiştirme ve oyun tabanlı öğrenme yöntemleri kullanılır. Ceza veya zorlama kesinlikle yoktur.</p>
                <p><strong>Süreç:</strong> 2-6 aylık yavrular için karakter analizi, sosyalleşme, tuvalet alışkanlığı ve ev içi kuralların oturtulması. Yavrunuzun dikkat süresine uygun kısa seanslar halinde temel itaat (otur, bekle, gel) adımları işlenir.</p>
              </div>
            </div>
            <!-- Card 1 -->
            <div class="slider-card" data-index="1" onclick="goToSlide(1)">
              <img src="assets/service_basic.webp" alt="Temel İtaat Eğitimi">
              <h3>Temel İtaat Eğitimi</h3>
              <div class="hidden-desc short-desc">Sevk kayışlı kontrol, doğru yürüyüş ve temel komutlarla uyumlu bir dost.</div>
              <div class="hidden-desc long-desc">
                <p><strong>Teknik:</strong> Tıklama (clicker) eğitimi, işaretleme ve ödül odaklı yönlendirmelerle sevk kayışlı (tasmalı) kontrol sağlanır.</p>
                <p><strong>Süreç:</strong> Yaklaşık 4-6 hafta sürer. Köpeğinizin sokakta çekiştirmeden yürümesi, komutları dinlemesi ve dış uyarıcılara karşı sakin kalması hedeflenir. 'Otur, Yat, Bekle, Gel, Takip' gibi komutların tasmalı olarak öğretilmesi ve sokak adaptasyonu sağlanır.</p>
              </div>
            </div>
            <!-- Card 2 -->
            <div class="slider-card" data-index="2" onclick="goToSlide(2)">
              <img src="assets/service_advanced.jpg" alt="İleri İtaat Eğitimi">
              <h3>İleri İtaat Eğitimi</h3>
              <div class="hidden-desc short-desc">Tasmasız tam kontrol ve dış uyarıcılara karşı mükemmel odaklanma.</div>
              <div class="hidden-desc long-desc">
                <p><strong>Teknik:</strong> Ses tonu ve beden dili hakimiyeti, ileri düzey işaret eğitimi ve yüksek motivasyon.</p>
                <p><strong>Süreç:</strong> Temel itaati başarıyla tamamlamış köpekler için uygulanır. Uzaktan komut verme, tasmasız serbest yürüyüş ve zorlu dış uyarıcılar altında mükemmel odaklanma becerileri kazandırılır.</p>
              </div>
            </div>
            <!-- Card 3 -->
            <div class="slider-card" data-index="3" onclick="goToSlide(3)">
              <img src="assets/service_potty.webp" alt="Tuvalet Eğitimi">
              <h3>Tuvalet Eğitimi</h3>
              <div class="hidden-desc short-desc">Ev içi veya dış mekan için kalıcı ve temiz tuvalet alışkanlığı.</div>
              <div class="hidden-desc long-desc">
                <p><strong>Teknik:</strong> Alan sınırlandırma (crate training), zamanlama takibi ve pozitif pekiştirme.</p>
                <p><strong>Süreç:</strong> Köpeğinizin yaşına, ırkına ve sindirim sistemine göre kişiselleştirilmiş bir rutin oluşturulur. Doğru yere tuvaletini yaptığında anında ödüllendirilerek kalıcı ve temiz bir alışkanlık pekiştirilir.</p>
              </div>
            </div>
            <!-- Card 4 -->
            <div class="slider-card" data-index="4" onclick="goToSlide(4)">
              <img src="assets/service_behavior.webp" alt="Davranış Bozukluğu Eğitimi">
              <h3>Davranış Bozukluğu Eğitimi</h3>
              <div class="hidden-desc short-desc">Havlama, ısırma, ayrılık kaygısı ve agresyon sorunlarına kalıcı çözümler.</div>
              <div class="hidden-desc long-desc">
                <p><strong>Teknik:</strong> Davranış modifikasyonu, duyarsızlaştırma (desensitization) ve karşıt koşullanma.</p>
                <p><strong>Süreç:</strong> Sorunun kök nedeni (korku, stres, güvensizlik vb.) detaylıca analiz edilir. Havlama, ısırma, ayrılık kaygısı veya agresyon gibi istenmeyen davranışları tetikleyen unsurlar belirlenip köpeğin kademeli olarak doğru davranışa yönlendirilmesi sağlanır.</p>
              </div>
            </div>
            <!-- Card 5 -->
            <div class="slider-card" data-index="5" onclick="goToSlide(5)">
              <img src="assets/service_area_guard.webp" alt="Alan Koruma Eğitimi">
              <h3>Alan Koruma Eğitimi</h3>
              <div class="hidden-desc short-desc">Evinizi veya iş yerinizi güvenle koruyacak kontrollü bekçilik eğitimi.</div>
              <div class="hidden-desc long-desc">
                <p><strong>Teknik:</strong> Güdü yönlendirme, kontrollü havlama ve doğru tehdit algısı oluşturma.</p>
                <p><strong>Süreç:</strong> Köpeğin genetik yatkınlığı ve özgüveni incelenir. Sadece gerçek tehditlere karşı reaksiyon vermesi, sahte uyarıcılara tepkisiz kalması ve en önemlisi sahibinin 'Bırak/Dur' komutuyla anında sakinleşmesi öğretilir.</p>
              </div>
            </div>
            <!-- Card 6 -->
            <div class="slider-card" data-index="6" onclick="goToSlide(6)">
              <img src="assets/service_personal_guard.jpg" alt="Kişi Koruma Eğitimi">
              <h3>Kişi Koruma Eğitimi</h3>
              <div class="hidden-desc short-desc">Sizi tehlikelere karşı savunacak, komutunuzla harekete geçen koruma eğitimi.</div>
              <div class="hidden-desc long-desc">
                <p><strong>Teknik:</strong> Avlanma ve savunma güdülerinin dengeli kullanımı, senaryo bazlı simülasyonlar.</p>
                <p><strong>Süreç:</strong> Yüksek özgüven ve ileri itaat seviyesi şarttır. Köpek, sahibini veya belirtilen kişiyi tehlike anında aktif olarak korumayı, tehdit ortadan kalktığında veya komut verildiğinde anında eylemi sonlandırmayı öğrenir.</p>
              </div>
            </div>
            <!-- Card 7 -->
            <div class="slider-card" data-index="7" onclick="goToSlide(7)">
              <img src="assets/service_sport.jpg" alt="İş ve Spor Köpekleri Eğitimi">
              <h3>İş ve Spor Köpekleri Eğitimi</h3>
              <div class="hidden-desc short-desc">Enerjisi yüksek köpekler için profesyonel çeviklik (agility) ve koku takibi.</div>
              <div class="hidden-desc long-desc">
                <p><strong>Teknik:</strong> Yüksek motivasyon (drive), oyuncak odaklı çalışma ve ileri düzey fiziksel kondisyon.</p>
                <p><strong>Süreç:</strong> IGP, Agility (çeviklik), K-9 veya arama kurtarma branşlarına yönelik özel antrenmanlar uygulanır. Köpeğin fiziksel sınırlarını, çevikliğini ve iş zekasını maksimum kapasitede kullanmasını sağlayan profesyonel bir süreçtir.</p>
              </div>
            </div>
          </div>
          
          <button class="slider-btn next-btn" id="sliderNextBtn"><i class="fas fa-chevron-right"></i></button>
        </div>
        
        <div class="slider-description-box" id="sliderDescBox">
          <h3 id="descTitle">Yavru Köpek Eğitimi</h3>
          <div class="short-desc" id="descShort">Temel kurallar ve sosyalleşme ile yavrunuzun hayata güvenle adım atmasını sağlıyoruz.</div>
          <div class="long-desc" id="descLong">
             <p><strong>Teknik:</strong> Pozitif pekiştirme ve oyun tabanlı öğrenme yöntemleri kullanılır. Ceza veya zorlama kesinlikle yoktur.</p>
             <p><strong>Süreç:</strong> 2-6 aylık yavrular için karakter analizi, sosyalleşme, tuvalet alışkanlığı ve ev içi kuralların oturtulması. Yavrunuzun dikkat süresine uygun kısa seanslar halinde temel itaat (otur, bekle, gel) adımları işlenir.</p>
          </div>
        </div>
      </div>`;

// Replace the section
const newHtml = htmlContent.replace(/<!-- Part 1: Trainings -->.*?<!-- Part 2: Hotel Service -->/s, newSliderHtml + '\n\n      <!-- Part 2: Hotel Service -->');

// Add script tag before body
const scriptAdded = newHtml.replace('</body>', '  <script src="slider.js"></script>\n</body>');

fs.writeFileSync('index.html', scriptAdded, 'utf8');
console.log('Successfully replaced HTML content');
