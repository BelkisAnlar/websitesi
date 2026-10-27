$htmlFiles = Get-ChildItem -Filter *.html -Exclude @("index_backup.html", "index.html")

$newFooterHTML = @"
  <footer id="footer" class="footer">
    <div class="container">
      <div class="footer-columns">
        <!-- Marka & Sosyal Medya -->
        <div class="footer-col brand-col">
          <a href="index.html" class="logo footer-logo"><i class="fas fa-paw"></i><span>Beytullah Çekik</span></a>
          <p class="footer-about-text">İzmir'de pozitif pekiştirme yöntemleriyle profesyonel köpek eğitimi. Dostunuzla aranızdaki bağı sevgiyle güçlendiriyoruz.</p>
          <div class="footer-socials">
            <a href="#" target="_blank" title="Instagram"><i class="fab fa-instagram"></i></a>
            <a href="#" target="_blank" title="YouTube"><i class="fab fa-youtube"></i></a>
            <a href="#" target="_blank" title="Facebook"><i class="fab fa-facebook-f"></i></a>
          </div>
          <div class="footer-contact-inline">
            <p><i class="fas fa-phone"></i> +90 553 886 02 37</p>
            <p><i class="fas fa-map-marker-alt"></i> Menderes, İzmir</p>
          </div>
        </div>
        
        <!-- Hızlı Menü -->
        <div class="footer-col">
          <h4>Menü</h4>
          <ul>
            <li><a href="index.html">Ana Sayfa</a></li>
            <li><a href="hakkimda.html">Hakkımda</a></li>
            <li><a href="kopek-oteli.html">Köpek Oteli</a></li>
            <li><a href="iletisim.html">İletişim</a></li>
          </ul>
        </div>
        
        <!-- Eğitimlerimiz -->
        <div class="footer-col">
          <h4>Eğitimlerimiz</h4>
          <ul>
            <li><a href="yavru-kopek-egitimi.html">Yavru Köpek Eğitimi</a></li>
            <li><a href="temel-itaat-egitimi.html">Temel İtaat Eğitimi</a></li>
            <li><a href="ileri-itaat-egitimi.html">İleri İtaat Eğitimi</a></li>
            <li><a href="tuvalet-egitimi.html">Tuvalet Eğitimi</a></li>
            <li><a href="davranis-bozuklugu-egitimi.html">Davranış Bozukluğu</a></li>
            <li><a href="alan-koruma-egitimi.html">Alan Koruma</a></li>
            <li><a href="kisi-koruma-egitimi.html">Kişi Koruma</a></li>
            <li><a href="is-ve-spor-kopekleri-egitimi.html">İş ve Spor Köpekleri</a></li>
          </ul>
        </div>

        <!-- Yasal -->
        <div class="footer-col">
          <h4>Yasal</h4>
          <ul>
            <li><a href="#">Gizlilik Politikası</a></li>
            <li><a href="#">Kullanım Koşulları</a></li>
            <li><a href="#">Güvenlik Kuralları</a></li>
            <li><a href="#">Çerez Politikası</a></li>
          </ul>
        </div>
      </div>
      
      <div class="footer-legal-bottom">
        <p>&copy; 2026 Beytullah Çekik Köpek Eğitimi. Tüm hakları saklıdır.</p>
      </div>
    </div>
  </footer>
"@

foreach ($file in $htmlFiles) {
    # We must read as UTF8 to avoid ANSI corruption of existing text
    $content = [System.IO.File]::ReadAllText($file.FullName, [System.Text.Encoding]::UTF8)
    
    # We will replace the entire <footer id="footer" ... </footer> block
    # Note: Regex to match from <footer id="footer" to </footer> including newlines
    $content = $content -replace '(?s)<footer id="footer".*?</footer>', $newFooterHTML
    
    [System.IO.File]::WriteAllText($file.FullName, $content, [System.Text.Encoding]::UTF8)
}

Write-Host "Updated all footers successfully."

