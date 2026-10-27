import os
import json
import urllib.parse

with open("data/blog-index.json", "r", encoding="utf-8") as f:
    blogs_by_slug = {p["slug"]: p for p in json.load(f)}

services_data = [
    {
        "file_name": "yavru-kopek-egitimi.html",
        "meta_title": "Yavru Köpek Eğitimi İzmir | Pozitif Gelişim & Sosyalleşme",
        "meta_desc": "İzmir yavru köpek eğitimi ile tuvalet alışkanlığı, ısırma engelleme, sosyalleşme ve temel ev kuralları. Pozitif pekiştirme ile sağlam bir temel atın.",
        "bg_image": "assets/service_puppy.webp",
        "title": "Yavru Köpek Eğitimi & Karakter İnşası",
        "lead": "2-6 aylık yavrunuzun zihinsel ve sosyal gelişimi için en kritik dönem. Pozitif pekiştirme, sevgi ve doğru sınırlarla ömür boyu uyumlu bir yol arkadaşı yetiştirin.",
        "highlights": [
            {"icon": "fa-baby", "title": "İdeal Yaş", "desc": "2 - 6 Aylık"},
            {"icon": "fa-calendar-check", "title": "Eğitim Süresi", "desc": "3 - 4 Hafta"},
            {"icon": "fa-home", "title": "Uygulama Alanı", "desc": "Ev & Sosyal Çevre"},
            {"icon": "fa-heart", "title": "Metodoloji", "desc": "Pozitif Pekiştirme"}
        ],
        "sec1_title": "Neden Yavru Dönemi Bir Köpeğin En Kritik Evresidir?",
        "sec1_content": """
        <p>Köpeklerin nörolojik ve davranışsal gelişiminin yaklaşık <strong>%80'i yaşamlarının ilk 16 haftasında</strong> tamamlanır. Bu erken evrede dünya ile kurulan ilk temaslar, köpeğin tüm yetişkinlik karakterinin harcını oluşturur. Korkular, güvensizlikler, aşırı reaktif tepkiler veya tam tersine özgüvenli, dengeli ve insan odaklı bir mizaç tam olarak bu dönemde şekillenir.</p>
        <p>Pek çok köpek sahibi <em>"Henüz çok küçük, 6 aylık olsun sonra eğitime başlarız"</em> yanılgısına düşer. Oysa 6. aya kadar evde öğrenilen yanlış alışkanlıklar (elleri ısırma, koltuk kemirme, serbest çiş yapma, kapıdan fırlama), sonradan düzeltilmesi çok daha fazla emek ve sabır gerektiren yerleşik davranış bozukluklarına dönüşür. Yavru köpek eğitimi, komut ezberletmek değil; yavrunun insan dünyasına korkusuzca adapte olmasını sağlayan bir rehberliktir.</p>
        """,
        "curriculum": [
            {"num": "1", "title": "Ev İçi Sınırlar & Tuvalet Düzeni", "desc": "Biyolojik saate uygun beslenme disiplini, tuvalet pedine ve dışarıya alışma rutini. Alan sınırlandırması ile evin güvenli paylaşımı."},
            {"num": "2", "title": "Oyun Isırması & Kemirmeyi Önleme", "desc": "Süt dişlerinin kaşınmasıyla başlayan el-ayak ısırma dürtüsünün doğru oyuncaklara yönlendirilmesi ve net 'Isırma İptali' protokolü."},
            {"num": "3", "title": "Kafes/Yatak Eğitimi & Yalnız Kalma", "desc": "Yavrunun evde yalnız kaldığında paniklememesi, ağlamaması ve ayrılık kaygısına kapılmaması için güvenli alan şartlandırması."},
            {"num": "4", "title": "Sosyal Çevre & Ses Duyarsızlaştırma", "desc": "Trafik sesleri, elektrik süpürgesi, yabancı insanlar, çocuklar ve farklı zeminlerle travmasız, ödül destekli pozitif tanışma."},
            {"num": "5", "title": "Temel İletişim & Odaklanma", "desc": "İsim farkındalığı, göz teması (focus), 'Otur', 'Bekle', 'Gel' ve ağzındakini sakince bırakma ('Bırak') temelleri."},
            {"num": "6", "title": "İlk Sevk Kayışı & Yürüyüş Alışkanlığı", "desc": "Tasmaya karşı direnç göstermeden, sahibini takip ederek güvenle yürüme mekaniğinin oyunla öğretilmesi."}
        ],
        "sec3_title": "Eğitim Sürecimiz Nasıl İlerler?",
        "process": [
            {"step": "1. Aşama", "title": "Ev İçi Değerlendirme & Ortam Düzeni", "desc": "Yavrunun yaşam alanını inceler, yatak, mama ve tuvalet köşelerini doğru kurgular; aile bireylerine ortak bir iletişim dili kazandırırız."},
            {"step": "2. Aşama", "title": "Birebir Uygulama Seansları", "desc": "Haftalık periyotlarla yavrunun dikkat eşiğine uygun (15-20 dakikalık) pozitif seanslar uygular, ödev ve egzersizleri aileyle pratik ederiz."},
            {"step": "3. Aşama", "title": "Dış Mekan & Ömür Boyu Takip", "desc": "Aşı süreci tamamlanan yavruyu gerçek hayat uyarıcılarıyla buluşturur, ergenlik döneminde de rehberliğimizi sürdürürüz."}
        ],
        "faqs": [
            {"q": "Aşıları henüz tamamlanmadı, eğitime başlayabilir miyiz?", "a": "Kesinlikle evet. Yavru eğitiminin ilk ve en kritik aşaması ev içi kurallar, tuvalet rutini ve ısırma engellemedir. Bu aşamalar ev ortamında güvenle tamamlanır; dış mekan çalışmaları ise aşı takvimi biter bitmez başlatılır."},
            {"q": "Yavrum sürekli ellerimizi ısırıyor, bu huyu ne zaman geçer?", "a": "Yavrular dünyayı ağızlarıyla keşfeder ve kardeşleriyle oynarken ısırma şiddetini öğrenirler. Doğru yönlendirme ve sınır koyma adımlarıyla 2-3 hafta içinde elleri ısırmayı bırakıp oyuncaklarına yönelirler."},
            {"q": "Eğitimde ceza veya sert müdahale var mı?", "a": "Asla. Yavru köpeklerin psikolojisi son derece hassastır. Bağırmak, burun sürtmek veya vurmak yavruyu sizden korkan ve ileride savunma amaçlı saldıran bir köpeğe dönüştürür. Eğitimlerimiz %100 pozitif pekiştirme ve güven bağına dayanır."}
        ],
        "related_slugs": ["yavru-kopeklerde-tuvalet-egitimi", "kopegim-neden-isiriyor", "kopegim-neden-esyalara-zarar-veriyor"]
    },
    {
        "file_name": "temel-itaat-egitimi.html",
        "meta_title": "Temel İtaat Eğitimi İzmir | Sevk Kayışlı Kontrol & Yürüyüş",
        "meta_desc": "İzmir temel itaat eğitimi ile çekiştirmeden yürüme, otur, bekle, gel komutları ve sokak adaptasyonu. Pozitif ve dengeli metotlarla uyumlu bir yaşam.",
        "bg_image": "assets/service_basic.webp",
        "title": "Temel İtaat Eğitimi (Tasmalı Kontrol & Şehir Uyumu)",
        "lead": "Yürüyüşlerinizi çekiştirme savaşından keyifli bir dostluk ritüeline dönüştürün. Sevk kayışı üzerinde tam odaklanma, sakinlik ve günlük yaşam disiplini.",
        "highlights": [
            {"icon": "fa-dog", "title": "Uygunluk", "desc": "5 Ay ve Üzeri"},
            {"icon": "fa-clock", "title": "Süre", "desc": "4 Hafta"},
            {"icon": "fa-road", "title": "Ortam", "desc": "Park, Cadde, Sahil"},
            {"icon": "fa-bullseye", "title": "Hedef", "desc": "Gevşek Tasma & Odak"}
        ],
        "sec1_title": "Temel İtaat Neden Sadece 'Komut Ezberletmek' Değildir?",
        "sec1_content": """
        <p>Pek çok insan temel itaati, köpeğe bir sirk hayvanı gibi "Otur", "Pati Ver" yaptırmaktan ibaret sanır. Oysa gerçek temel itaat; köpeğinizin karmaşık ve gürültülü insan dünyasında <strong>size güvenerek sakin kalabilmesi</strong>, uyarıcılar karşısında fevri davranmak yerine sizin rehberliğinizi aramasıdır.</p>
        <p>Gergin, sürekli tasmayı asılan ve karşıdan bir köpek ya da kedi gördüğünde sizi peşinden sürükleyen bir köpekle dışarı çıkmak hem sizin için bir kabus hem de köpeğiniz için yüksek bir stres kaynağıdır. Temel itaat programımızda tasmayı bir pranga olmaktan çıkarıp, aranızdaki görünmez bir <em>iletişim kablosuna</em> dönüştürüyoruz.</p>
        """,
        "curriculum": [
            {"num": "1", "title": "Gevşek Tasmayla Yürüyüş (Heel / Yanımda)", "desc": "Köpeğin sahibinin adım hızına uyum sağlaması, burnuyla yeri koklayıp aniden asılmadan sol/sağ hizada sakin ilerlemesi."},
            {"num": "2", "title": "Sabırlı Bekleme (Otur-Bekle & Yat-Bekle)", "desc": "Bir kafede otururken, veteriner bekleme salonunda veya sokakta biriyle konuşurken köpeğinizin sakinleşip yerinde beklemesi."},
            {"num": "3", "title": "Kusursuz Geri Çağırma (Gel / Recall)", "desc": "Dikkat dağıtıcıların varlığında dahi çağrıldığında tasmayı gerdirmeden doğrudan sahibinin yanına koşarak gelmesi."},
            {"num": "4", "title": "İnsanlara ve Köpeklere Atlama Engelleme", "desc": "Heyecan kontrolü; sevgi gösterisi adı altında üst baş kirleten, tırnaklayan atlama dürtüsünün söndürülmesi."},
            {"num": "5", "title": "Kapı ve Kaldırım Kuralları", "desc": "Açılan ev ya da araba kapısından fırlamama, yaya geçitlerinde ve kaldırım kenarlarında izin komutu olmadan yola adım atmama."},
            {"num": "6", "title": "Yerden Çöp / Zehirli Yem Yememe (Bırak / Hayır)", "desc": "Sokakta bulunan zararlı yiyeceklere ve yabancı maddelere dokunmadan, sahibin tek uyarısıyla hedeften vazgeçme disiplini."}
        ],
        "sec3_title": "Eğitim Metodolojimiz",
        "process": [
            {"step": "1. Hafta", "title": "Motivasyon & Odak İnşası", "desc": "Köpeğin ödül mekanizması ve çalışma arzusu çözülür. Sakin ortamda doğru vücut dili ve sevk kayışı tutuş mekaniği oturtulur."},
            {"step": "2. & 3. Hafta", "title": "Çeldiriciler Altında Pratik", "desc": "İzmir'in parklarında, diğer köpeklerin, çocukların ve bisikletlerin geçtiği alanlarda komutların kalıcılığı test edilir."},
            {"step": "4. Hafta", "title": "Sahip Yönetimi & Şehir Sınavı", "desc": "Tüm kontrol tamamen köpek sahibine devredilir. Sahip, köpeğini kalabalık cadde ve kafelerde tek başına sorunsuz yönetir hale gelir."}
        ],
        "faqs": [
            {"q": "Köpeğim 3 yaşında, temel itaat için çok mu geç?", "a": "Kesinlikle hayır. 'Ağaç yaşken eğilir' sözü köpekler için geçerli değildir. Sağlıklı her yaştaki köpek, doğru liderlik ve net kurallarla yeni davranış kalıplarını hızla benimser."},
            {"q": "Eğitim bittikten sonra köpeğim komutları unutur mu?", "a": "Eğitim sürecinde sadece köpeği değil, sizi de eğitiyoruz. Günlük hayatınızda öğrendiğiniz basit iletişim kurallarını sürdürdüğünüz sürece köpeğiniz bu disiplini ömür boyu korur."},
            {"q": "Göğüs tasması mı yoksa boyun tasması mı kullanıyorsunuz?", "a": "Göğüs tasması çekme dürtüsünü tetiklediği için eğitim sürecinde düz ve ergonomik boyun tasmalarıyla hassas yönlendirme yapılır."}
        ],
        "related_slugs": ["ornek-yazi", "kopegim-neden-surekli-uzerime-atliyor", "kopegim-neden-beni-takip-ediyor"]
    },
    {
        "file_name": "ileri-itaat-egitimi.html",
        "meta_title": "İleri İtaat Eğitimi İzmir | Tasmasız Kontrol & Kusursuz Odak",
        "meta_desc": "İzmir ileri itaat eğitimi ile sevk kayışı olmadan tam odak, uzaktan komutlar ve yüksek çeldiriciler altında kontrol. Profesyonel köpek eğitimi.",
        "bg_image": "assets/service_advanced.jpg",
        "title": "İleri İtaat Eğitimi (Tasmasız Kontrol & Yüksek Odak)",
        "lead": "Tasma olmadan, en zorlu dış uyarıcılar altında dahi dostunuza %100 güvenebilmenin huzuru. Zihinsel odaklanmanın ve koşulsuz itaatin zirvesi.",
        "highlights": [
            {"icon": "fa-check-double", "title": "Ön Koşul", "desc": "Temel İtaat Başarısı"},
            {"icon": "fa-stopwatch", "title": "Süre", "desc": "4 - 6 Hafta"},
            {"icon": "fa-tree", "title": "Ortam", "desc": "Açık Alan & Doğa"},
            {"icon": "fa-award", "title": "Sonuç", "desc": "%100 Tasmasız Güven"}
        ],
        "sec1_title": "İleri İtaat: Özgürlüğün ve Karşılıklı Güvenin Zirvesi",
        "sec1_content": """
        <p>İleri İtaat eğitimi, köpeği bir şov figürüne çevirmek değil; ona şehir hayatında ve doğada <strong>en üst düzey özgürlüğü güvenle tanıyabilmektir</strong>. Tasmasız yürüyebilen bir köpek, boynundaki fiziksel bir kayışla değil, zihnindeki görünmez sadakat ve odak bağıyla sahibine bağlıdır.</p>
        <p>Önünden bir kedi fırladığında, karşıdan serbest bir köpek koştuğunda veya uzaktan bir top yuvarlandığında dahi komutta kalabilmek yüksek düzeyde dürtü kontrolü (impulse control) gerektirir. Bu program, temel itaatini eksiksiz tamamlamış köpeklerin zihinsel kapasitelerini en üst seviyeye taşır.</p>
        """,
        "curriculum": [
            {"num": "1", "title": "Tasmasız Yanımda Takip (Off-Leash Heel)", "desc": "Sevk kayışı olmaksızın, adımlarınız hızlandığında koşan, durduğunuzda otomatik oturan kusursuz adımlama."},
            {"num": "2", "title": "Uzaktan ve Hareket Halinde Komutlar", "desc": "Köpek sizden 30-50 metre uzaktayken veya tam hızla koşarken verilen tek bir 'Yat' veya 'Dur' komutuyla anında çakılması."},
            {"num": "3", "title": "Görsel ve El İşaretleriyle İtaat (Silent Commands)", "desc": "Sesli komut kullanmadan, sadece beden dili ve el işaretleriyle yönlendirme kabiliyeti."},
            {"num": "4", "title": "Aşırı Çeldiriciler Altında Bekleme", "desc": "Çevresinde koşan diğer köpekler, atılan toplar veya yemek kokuları varken sahibinin izni olmadan kıpırdamama."},
            {"num": "5", "title": "Acil Durum Geri Çağırma (Emergency Recall)", "desc": "Her koşulda, hangi hedefe koşuyor olursa olsun çağrıldığı anda 180 derece dönüp sahibinin önüne gelme garantisi."},
            {"num": "6", "title": "Yönlendirmeli Alan Araması & Gönderim", "desc": "Köpeği belirli bir noktaya ('Yerine Geç', 'İleri') el işaretiyle yönlendirme ve orada kalmasını sağlama."}
        ],
        "sec3_title": "Eğitim Adımları ve Güvenlik Protokolü",
        "process": [
            {"step": "1. Aşama", "title": "15 Metrelik Güvenlik Kordonu (Long Line)", "desc": "Köpek asla doğrudan serbest bırakılmaz. Uzun güvenlik ipiyle mesafeler 5, 10, 20 metreye kademeli olarak çıkarılır."},
            {"step": "2. Aşama", "title": "Çeldirici Kademelendirmesi (Proofing)", "desc": "Komutlar kontrollü uyarıcılar (ses kayıtları, kontrollü eğitim köpekleri, hareketli nesneler) eşliğinde pekiştirilir."},
            {"step": "3. Aşama", "title": "Gerçek Dünyada Tasmasız Doğrulama", "desc": "Fiziksel ip tamamen çıkarılır ve geniş sahil şeritleri, açık doğa alanlarında bağımsız testler uygulanır."}
        ],
        "faqs": [
            {"q": "Her köpek ileri itaat eğitimi alabilir mi?", "a": "Temel itaati tam oturmuş ve sahip odaklılığı yüksek her sağlıklı köpek bu eğitimi alabilir. Ancak temel itaati eksik olan köpekler doğrudan ileri itaat programına kabul edilmez."},
            {"q": "Şehir içinde tasmasız gezdirmek yasal mıdır?", "a": "Köpeğiniz %100 söz dinlese dahi trafiğe açık alanlarda yasal mevzuat ve çevre güvenliği gereği tasma takılmalıdır. Bu eğitimin asıl amacı; tasmayı çıkardığınız plaj, park, orman ve bahçe gibi alanlarda sınırsız bir özgürlük ve güvenlik sağlamaktır."},
            {"q": "Dürtüsü çok yüksek av veya çoban ırklarında sonuç alınır mı?", "a": "Evet, bu ırkların çalışma arzusu yüksektir. Doğru kanalize edildiğinde ileri itaatte en başarılı sonuçlar bu ırklardan elde edilir."}
        ],
        "related_slugs": ["kopegim-neden-diger-kopeklere-saldiriyor", "ornek-yazi", "kopegim-neden-surekli-kokluyor"]
    },
    {
        "file_name": "tuvalet-egitimi.html",
        "meta_title": "Köpek Tuvalet Eğitimi İzmir | Ev İçi & Dış Mekan Çözümleri",
        "meta_desc": "İzmir köpek tuvalet eğitimi ile halılara çiş yapma, ped şaşırma ve gece kaçırma sorunlarına bilimsel son. Yerinde profesyonel tuvalet alışkanlığı.",
        "bg_image": "assets/service_potty.webp",
        "title": "Köpek Tuvalet Eğitimi (Kalıcı Rutin & Mekan Algısı)",
        "lead": "Sürekli halı yıkatmaktan ve eve geldiğinizde kötü sürprizlerle karşılaşmaktan kurtulun. Biyolojik saat yönetimi ve mekan algısıyla garantili tuvalet düzeni.",
        "highlights": [
            {"icon": "fa-toilet", "title": "Kapsam", "desc": "Ped & Dış Mekan"},
            {"icon": "fa-hourglass-half", "title": "Süre", "desc": "2 - 3 Hafta"},
            {"icon": "fa-home", "title": "Ortam", "desc": "Kendi Yaşam Alanınız"},
            {"icon": "fa-chart-line", "title": "Başarı", "desc": "Kalıcı Davranış"}
        ],
        "sec1_title": "Köpeğiniz Asla 'İntikam Almak İçin' Eve Çiş Yapmaz!",
        "sec1_content": """
        <p>Köpek sahiplerinin en sık yaptığı yorum: <em>"Bana kızdığı için bilerek yatağıma yaptı"</em> veya <em>"Onu evde bıraktım diye intikam alıyor"</em> şeklindedir. Oysa köpekler intikam, kin veya suçluluk gibi karmaşık insan duygularıyla hareket etmezler. Tuvalet kaçırmanın arkasında yalnızca <strong>eksik mekan algısı, düzensiz beslenme biyolojisi, stres veya yanlış temizlik kalıntıları</strong> yatar.</p>
        <p>Burun sürtmek, bağırmak ya da saatler sonra eve gelip yerdeki çişi göstererek köpeğe ceza vermek sorunu çözmez; tam aksine köpeğin siz varken tuvaletini tutmasına ve koltuk arkalarına gizlice yapmasına sebep olur. Profesyonel tuvalet eğitimi sistemimiz, köpeğin doğal temizlik içgüdüsünü tetikleyerek kesin çözüm üretir.</p>
        """,
        "curriculum": [
            {"num": "1", "title": "Mekan ve Alan Ayrımı (Denning Instinct)", "desc": "Köpekler uyudukları ve beslendikleri yeri kirletmezler. Yaşam alanını daraltıp kademeli genişleterek doğru mekan bilincinin oturtulması."},
            {"num": "2", "title": "Saatli Beslenme & Biyolojik Takvim", "desc": "Önünde 24 saat mama duran köpeğin tuvalet saati tahmin edilemez. Saatli beslenme ile sindirim döngüsünün dakikası dakikasına programlanması."},
            {"num": "3", "title": "Dış Mekan Şartlandırması & Tetikleyici Komut", "desc": "Dışarı çıkıldığında sadece gezip eve gelince çiş yapma hatasının engellenmesi; 'Çiş Yap' komutuyla tuvaletin hızlandırılması."},
            {"num": "4", "title": "Enzimatik Temizlik ve Koku Nötralizasyonu", "desc": "Halı altlarına ve derz aralarına sinen idrar tuzlarının temizlenerek köpeğin burnunu yanıltan koku izlerinin tamamen silinmesi."},
            {"num": "5", "title": "Gece Çiş Kaçırmalarının Önlenmesi", "desc": "Gece su tüketimi düzenlemesi ve sabah ilk uyanma anındaki kritik 5 dakikalık tahliye protokolü."},
            {"num": "6", "title": "Pedden Dışarıya Geçiş Metodolojisi", "desc": "Sürekli eve ped aramak istemeyen sahipler için pedi santim santim kapıya taşıyıp tamamen dışarı aktarma süreci."}
        ],
        "sec3_title": "Yerinde Tuvalet Eğitimi Süreci",
        "process": [
            {"step": "1. Gün", "title": "Ev Ziyareti & Alan Analizi", "desc": "Evinizin yerleşim planını, zemin tiplerini inceler; köpeğin biyolojik ritmine uygun tuvalet haritasını çıkarırız."},
            {"step": "1. Hafta", "title": "Sıkı Rutin & Ödül Protokolü", "desc": "Beslenme, su ve dışarı çıkış saatleri dakik olarak uygulanır; doğru yere yapılan her tuvalet anında yüksek değerle ödüllendirilir."},
            {"step": "2. & 3. Hafta", "title": "Serbestlik & Kalıcı Davranış", "desc": "Alan sınırlandırması kademeli olarak kaldırılır; köpek evin her köşesini kendi yaşam alanı olarak kodlar ve asla pisletmez."}
        ],
        "faqs": [
            {"q": "Yetişkin köpek tuvalet eğitimi alabilir mi?", "a": "Kesinlikle evet! Hatta yetişkin köpeklerin kas ve mesane kontrolü yavrulardan çok daha güçlü olduğu için, doğru rutin kurulduğunda yavrulara kıyasla çok daha hızlı sonuç verirler."},
            {"q": "Evde ped eğitimi mi yoksa doğrudan dışarısı mı?", "a": "Günde en az 3-4 kez dışarı çıkarabilme imkanınız varsa doğrudan dış mekan eğitimi en sağlıklısıdır. Yoğun çalışan veya küçük ırk sahipleri için ise ev içi ped alanı ve dışarısı kombine edilebilir."},
            {"q": "Çiş yaptığı yere çamaşır suyu döküyorum, doğru mu?", "a": "Kesinlikle hayır! Çamaşır suyu ve amonyaklı temizleyiciler idrar kokusunu taklit eder ve köpeğe 'Burası bir tuvalet alanı' mesajı verir. Mutlaka enzimatik temizleyiciler veya beyaz sirke solüsyonu kullanılmalıdır."}
        ],
        "related_slugs": ["yavru-kopeklerde-tuvalet-egitimi", "kopegim-neden-gece-havliyor", "kopegim-neden-kaziyor"]
    },
    {
        "file_name": "davranis-bozuklugu-egitimi.html",
        "meta_title": "Köpek Davranış Bozukluğu Eğitimi İzmir | Agresyon & Rehabilitasyon",
        "meta_desc": "İzmir köpek davranış bozukluğu tedavisi. Tasma reaktivitesi, agresyon, ayrılık kaygısı, aşırı korku ve travma rehabilitasyonu. Uzman köpek eğitmeni.",
        "bg_image": "assets/service_behavior.webp",
        "title": "Köpek Davranış Bozukluğu & Psikolojik Rehabilitasyon",
        "lead": "Agresyon, ayrılık kaygısı, travmalar veya aşırı reaktivite... Çaresiz değilsiniz. Köpeğinizin iç dünyasını anlayarak kök nedenleri bilimsel metotlarla dönüştürüyoruz.",
        "highlights": [
            {"icon": "fa-brain", "title": "Yaklaşım", "desc": "Kök Neden Tedavisi"},
            {"icon": "fa-shield-virus", "title": "Uzmanlık", "desc": "Agresyon & Korku"},
            {"icon": "fa-user-nurse", "title": "Program", "desc": "Bireysel Protokol"},
            {"icon": "fa-smile-beam", "title": "Sonuç", "desc": "İç Huzur & Güven"}
        ],
        "sec1_title": "Belirtiyi Bastırmak Değil, Kök Nedeni İyileştirmek",
        "sec1_content": """
        <p>Havlamak, ısırmak, parçalamak veya diğer köpeklere saldırmak birer 'kötülük' değil, köpeğin iç dünyasındaki <strong>korku, çaresizlik, aşırı stres veya bariyer frustrasyonunun</strong> dışavurumudur. Bu tepkileri sadece ceza vererek ya da boynunu sıkarak bastırmaya çalışmak, düdüklü tencerenin kapağını zorla kapatmaya benzer; patlama anı sadece ertelenir ve daha şiddetli hale gelir.</p>
        <p>Davranış rehabilitasyonu programımızda köpeği yargılamadan, nörolojik ve psikolojik eşik değerlerini analiz ediyoruz. <em>Karşıt Koşullandırma (Counter-Conditioning)</em> ve <em>Sistematik Duyarsızlaştırma</em> teknikleriyle köpeğin tehdit olarak algıladığı uyarıcıları (diğer köpekler, insanlar, sesler, yalnız kalma) pozitif ve güvenli hislerle yeniden eşleştiriyoruz.</p>
        """,
        "curriculum": [
            {"num": "1", "title": "Tasma Reaktivitesi & Diğer Köpeklere Agresyon", "desc": "Karşıdan bir köpek gördüğünde şaha kalkma, hırlama ve nefes nefese kalma krizlerinin eşik yönetimiyle sakinliğe dönüştürülmesi."},
            {"num": "2", "title": "Ayrılık Kaygısı (Separation Anxiety)", "desc": "Sahibi evden çıktığında kapıları kemirme, aralıksız uluma ve çiş kaçırma nöbetlerinin kademeli güven protokolüyle tedavisi."},
            {"num": "3", "title": "Kaynak Koruma (Resource Guarding)", "desc": "Mama kabı, kemik, oyuncak veya sahibin yatağını koruyup aile bireylerine dahi diş gösterme probleminin kalıcı çözümü."},
            {"num": "4", "title": "İnsan & Yabancı Reaktivitesi", "desc": "Eve gelen misafirlere, sokakta koşan çocuklara veya kuryelere karşı duyulan aşırı güvensizlik ve havlama tepkilerinin söndürülmesi."},
            {"num": "5", "title": "Fobi & Travma İyileştirmesi", "desc": "Şimşek, gök gürültüsü, havai fişek veya geçmişte şiddet görmüş kurtarma (barınak) köpeklerinin özgüven inşası."},
            {"num": "6", "title": "Kompulsif Takıntılar (Gölge/Kuyruk Kovalama)", "desc": "Zihinsel aşırı uyarılma ve stres kaynaklı kendi kendine zarar verme döngülerinin kırılması."}
        ],
        "sec3_title": "Rehabilitasyon Yol Haritası",
        "process": [
            {"step": "1. Aşama", "title": "Detaylı Davranış Analizi & Eşik Tespiti", "desc": "Köpeğinizin tetikleyici unsurlarını ve patlama yaşadığı kritik mesafe eşiğini yerinde gözlemler, risk haritasını çıkarırız."},
            {"step": "2. Aşama", "title": "Nötr Zihin Hali & Karşıt Şartlandırma", "desc": "Köpeğin beynindeki korku/öfke bağlantısını keser, tetikleyiciyi gördüğünde sahibine dönüp sakinleşme refleksi kazandırırız."},
            {"step": "3. Aşama", "title": "Gerçek Hayat Entegrasyonu", "desc": "Sahada, İzmir sokaklarında gerçek uyarıcılarla kademeli karşılaşmalar organize eder, sahibe kriz anı yönetimini öğretiriz."}
        ],
        "faqs": [
            {"q": "Agresif bir köpek gerçekten tamamen sakinleşebilir mi?", "a": "Evet. Agresyonun altında yatan kök neden (korku, liderlik eksikliği, yanlış tasma gerginliği) doğru tespit edilip giderildiğinde köpeklerin çok büyük bir kısmı sakin, yönetilebilir ve sosyal bireylere dönüşür."},
            {"q": "Rehabilitasyonda ilaç ya da sakinleştirici kullanıyor musunuz?", "a": "Hayır. Bizim uzmanlık alanımız davranışsal rehabilitasyondur. Çok nadir, ileri derece nörolojik vakalarda veteriner hekim gözetiminde destek alınabilir; ancak temel başarı zihinsel eğitimle sağlanır."},
            {"q": "Kaç seans süreceğini önceden bilebilir miyiz?", "a": "Davranış bozuklukları mekanik bir komut eğitimi değildir. Köpeğin travmasının derinliğine ve ailenin tutarlılığına bağlıdır. Ön değerlendirme seansımızda net bir takvim öngörüsü paylaşılır."}
        ],
        "related_slugs": ["kopeklerde-ayrilik-kaygisi", "kopegim-neden-diger-kopeklere-saldiriyor", "kopegim-neden-yabancilardan-korkuyor"]
    },
    {
        "file_name": "alan-koruma-egitimi.html",
        "meta_title": "Alan Koruma Eğitimi İzmir | Bahçe, Villa & Tesis Koruma",
        "meta_desc": "İzmir alan ve mülk koruma köpeği eğitimi. Sınır devriyesi, caydırıcılık, zehirli yem yememe ve komutla müdahale. Güvenilir bekçi köpekleri.",
        "bg_image": "assets/service_area_guard.webp",
        "title": "Alan ve Mülk Koruma Köpeği Eğitimi",
        "lead": "Evinizi, bahçenizi, villanızı veya ticari tesisinizi güvenle emanet edebileceğiniz; dost ile düşmanı ayırt edebilen, yüksek caydırıcılığa sahip koruma köpekleri.",
        "highlights": [
            {"icon": "fa-warehouse", "title": "Kapsam", "desc": "Villa, Çiftlik, Tesis"},
            {"icon": "fa-user-shield", "title": "Ön Koşul", "desc": "Karakter Testi"},
            {"icon": "fa-ban", "title": "Özel Ders", "desc": "Zehir Yem Reddi"},
            {"icon": "fa-lock", "title": "Sonuç", "desc": "Tam Güvenlik"}
        ],
        "sec1_title": "Bilinçli Koruma vs. Kontrolsüz Saldırganlık",
        "sec1_content": """
        <p>Gerçek bir alan koruma köpeği, kapının önünden geçen her yayaya, kediye veya kuryeye çılgınlar gibi havlayan bir köpek <strong>değildir</strong>. Gereksiz havlayan köpek hem komşuları rahatsız eder hem de gerçek bir tehlike anında sahibinin durumu ciddiye almamasına yol açar.</p>
        <p>Profesyonel alan koruma eğitimi; köpeğin mülk sınırlarını net olarak kavraması, çit arkasından geçen normal hareketlerle mülke izinsiz girmeye çalışan tehditleri ayırt edebilmesi ve en önemlisi <strong>sahibinin tek bir emriyle anında sakinleşebilmesi</strong> üzerine kuruludur.</p>
        """,
        "curriculum": [
            {"num": "1", "title": "Mülk Sınır Farkındalığı & Devriye Disiplini", "desc": "Bahçe çitleri, kapı eşikleri ve duvar sınırlarının köpeğin zihnine güvenli bölge olarak kodlanması; açık kapıdan dışarı fırlamama."},
            {"num": "2", "title": "Tehdit Teşhisi ve Caydırıcı Havlama", "desc": "Normal sokak hareketliliğine duyarsız kalırken, telleri tırmanan veya izinsiz giriş yapmaya çalışan kişilere karşı sert ve kararlı duruş."},
            {"num": "3", "title": "Yabancıdan Yiyecek Yememe (Zehir Yem Reddi)", "desc": "Mülk dışından içeri atılan et, mama veya yabancıların elinden uzatılan yiyeceklere asla dokunmama; zehirlenme tuzaklarını bertaraf etme."},
            {"num": "4", "title": "Komutla Havlama & Komutla Susma (Speak & Quiet)", "desc": "Sahibinin 'Uyar' emriyle caydırıcılık başlatması, 'Tamam / Yanımda' emriyle salisesinde normal moda dönmesi."},
            {"num": "5", "title": "Gece Algısı ve Ses Hassasiyeti", "desc": "Karanlık saatlerde mülk çevresindeki olağandışı hareketleri ve sessiz sızma girişimlerini anında fark edip alarm verme."},
            {"num": "6", "title": "Müdahale ve Alanı Savunma Mekaniği", "desc": "Karakteri uygun ırklarda, fiziksel saldırı durumunda mülke giren şahsı etkisiz hale getirme ve sahibin emrine kadar sabitleme."}
        ],
        "sec3_title": "Eğitim ve Güvenlik Standartlarımız",
        "process": [
            {"step": "1. Aşama", "title": "Mizaç ve Karakter Testi", "desc": "Her köpek koruma için uygun değildir. Korkak veya aşırı panik karakterli köpekler korumaya alınmaz; sağlam sinir sistemine sahip köpekler seçilir."},
            {"step": "2. Aşama", "title": "Yerinde (Mülkte) Senaryo Çalışmaları", "desc": "Eğitim köpek otelinde değil, köpeğin koruyacağı gerçek arazide özel koruma ekipmanları (dekoy) eşliğinde uygulanır."},
            {"step": "3. Aşama", "title": "Aile İçi Güvenlik Entegrasyonu", "desc": "Köpeğin koruma modundayken bile aile bireylerine, çocuklara ve davetli misafirlere karşı son derece nazik olması garanti edilir."}
        ],
        "faqs": [
            {"q": "Koruma eğitimi alan köpeğim ailemiz için bir tehlike oluşturur mu?", "a": "Asla. Profesyonel eğitim köpeği saldırganlaştırmaz; tam tersine dürtülerini kontrol altına alır. Eğitimsiz bir bekçi köpeği kontrolsüzdür; eğitimli bir koruma köpeği ise sadece emrinizle hareket eden güvenilir bir kalkan gibidir."},
            {"q": "Hangi ırklar alan koruma için uygundur?", "a": "Kangal, Akbaş, Kafkas Çoban, Alman Çoban Köpeği, Rottweiler, Doberman, Cane Corso ve Presa Canario gibi genetik koruma dürtüsü güçlü ırklar en ideal adaylardır."},
            {"q": "Zehir yem yememe eğitimi gerçekten işe yarıyor mu?", "a": "Evet. Köpeğe sadece kendi kabından ve sadece sahibinin izin kelimesiyle yemek yeme şartlandırması yapılarak yerdeki ve dışarıdan atılan yabancı yiyecekler birer tabu haline getirilir."}
        ],
        "related_slugs": ["kopegim-neden-insanlara-havliyor", "kopegim-neden-surekli-havliyor", "kopegim-neden-uluyor"]
    },
    {
        "file_name": "kisi-koruma-egitimi.html",
        "meta_title": "Kişi Koruma Eğitimi İzmir | Yakın Koruma & Bodyguard Köpek",
        "meta_desc": "İzmir kişi ve aile koruma köpeği eğitimi. Yakın koruma, tehdit karşılama, komutla bırakma ve aile içi sosyal denge. Profesyonel K9 eğitimi.",
        "bg_image": "assets/service_personal_guard.jpg",
        "title": "Kişi Koruma Köpeği Eğitimi (Personal Protection)",
        "lead": "Sizi ve ailenizi her an gölge gibi takip eden, tehlike anında saniyeler içinde devreye giren ve tek bir emrinizle anında duran sadık ve güçlü bir koruma kalkanı.",
        "highlights": [
            {"icon": "fa-user-shield", "title": "Hedef", "desc": "Kişi & Aile Güvenliği"},
            {"icon": "fa-medal", "title": "Düzey", "desc": "Üst Düzey Disiplin"},
            {"icon": "fa-stopwatch-20", "title": "Tepki", "desc": "Saliselik İtaat"},
            {"icon": "fa-shield-alt", "title": "Felsefe", "desc": "Kontrollü Güç"}
        ],
        "sec1_title": "Kişi Koruma Köpeği: Ruhsatlı Bir Güvence",
        "sec1_content": """
        <p>Kişi koruma köpeği (Personal Protection Dog), eğitim dünyasındaki en yüksek sorumluluk gerektiren branştır. Bu köpekler gündelik hayatta bir kafede ayağınızın dibinde masumca uyuyan, çocuklarınızla oyun oynayan sevecen bir aile ferdiyken; size yönelen fiziksel bir tehdit, gasp veya darp girişiminde saniyeler içinde <strong>aşılmaz bir kalkana</strong> dönüşürler.</p>
        <p>Buradaki en kritik nokta köpeğin ısırması değil; <strong>ısırmayı tek bir fısıltıyla bırakabilmesidir (Out)</strong>. Karakteri oturmamış, sinir sistemi zayıf veya temel itaati kusursuz olmayan hiçbir köpek kişi koruma eğitimine kabul edilmez.</p>
        """,
        "curriculum": [
            {"num": "1", "title": "Yakın Koruma Yürüyüşü ve Çevre Taraması", "desc": "Sahibinin yanında yürürken çevredeki ani hareketleri, arkadan yaklaşan şüpheli şahısları sezme ve tetikte durma bilinci."},
            {"num": "2", "title": "Tehdit Analizi (Normal İnsan vs. Saldırgan)", "desc": "Yolda el sıkan veya konuşan biriyle, elinde sopa/bıçak olan veya sahibine fiziksel temasla saldıran kişiyi kusursuz ayırt etme."},
            {"num": "3", "title": "Kararlı Isırma Mekaniği ve Tutuş Gücü", "desc": "Profesyonel ısırma tulumu ve kollukla, hedefin kolunu veya bacağını tam kavrayıp sarsarak saldırganı eylemsiz bırakma."},
            {"num": "4", "title": "Saliselik Bırakma Komutu (Out)", "desc": "Adrenalin en yüksek seviyedeyken dahi sahibinin tek bir 'Bırak' emriyle hedefi serbest bırakıp nöbet pozisyonuna geçme."},
            {"num": "5", "title": "Silah, Sopa ve Patlama Seslerine Direnç", "desc": "Ani bağırmalar, sopa darbeleri veya patlama sesleri altında korkup kaçmadan sahibinin önünde siper olma disiplini."},
            {"num": "6", "title": "Araç İçi ve Seyahat Koruması", "desc": "Araba kullanırken yan camdan veya kapıdan yapılabilecek gasp ve saldırı girişimlerine anında karşı koyma."}
        ],
        "sec3_title": "Eğitim Kriterlerimiz",
        "process": [
            {"step": "1. Aşama", "title": "Karakter & Dürtü Analizi", "desc": "Av dürtüsü, savunma dürtüsü ve kavga dürtüsü (prey/defense/fight drive) dengesi test edilir. Korku agresyonu gösteren köpekler elenir."},
            {"step": "2. Aşama", "title": "Dekoy ve Kolluk Çalışmaları", "desc": "Profesyonel yardımcı eğitmen (dekoy) eşliğinde köpeğe özgüven aşılanır, doğru ısırma ve bırakma refleksleri kas hafızasına kazınır."},
            {"step": "3. Aşama", "title": "Gerçek Yaşam Senaryoları & Sahip İdaresi", "desc": "Gece yürüyüşleri, ATM önü simülasyonları ve araç içi savunma senaryoları çalışılarak sistem sahibin kontrolüne teslim edilir."}
        ],
        "faqs": [
            {"q": "Köpeğim kişi koruma eğitimi alırsa arkadaşlarıma saldırır mı?", "a": "Asla. Kişi koruma köpeği sadece sizin açık emrinizle veya size yönelik bariz bir fiziksel saldırı anında devreye girer. Sizin sakin olduğunuz ve el sıktığınız her insana karşı tamamen tarafsız ve sakindir."},
            {"q": "Hangi ırklar kişi koruma için uygundur?", "a": "Belçika Malinois, Alman Çoban Köpeği, Doberman, Rottweiler, Hollanda Çoban Köpeği ve Dev Schnauzer bu eğitimin dünya standartlarındaki başlıca ırklarıdır."},
            {"q": "Temel itaat eğitimi olmadan kişi korumaya başlanabilir mi?", "a": "Kesinlikle hayır. Kusursuz bir sevk kayışı ve tasmasız kontrolü olmayan bir köpeğe koruma eğitimi vermek hem yasal hem de vicdani olarak büyük bir risktir. Temel ve ileri itaat şarttır."}
        ],
        "related_slugs": ["kopegim-neden-insanlara-havliyor", "kopegim-neden-diger-kopeklere-saldiriyor", "ornek-yazi"]
    },
    {
        "file_name": "is-ve-spor-kopekleri-egitimi.html",
        "meta_title": "İş ve Spor Köpekleri Eğitimi İzmir | K9, IGP, Koku Takibi",
        "meta_desc": "İzmir iş ve spor köpekleri eğitimi. IGP, K9 kondisyon, koku takibi (mantrailing) ve çeviklik (agility). Yüksek enerjili ırklar için zihinsel zirve.",
        "bg_image": "assets/service_sport.jpg",
        "title": "İş ve Spor Köpekleri Eğitimi (K9, IGP, Koku Takibi)",
        "lead": "Yüksek enerjili, genetik potansiyeli tavan yapmış iş köpekleri için zihinsel ve fiziksel tatmin. Koku takibi, çeviklik, itaat ve spor branşlarıyla köpeğinizin zirvesini keşfedin.",
        "highlights": [
            {"icon": "fa-running", "title": "Branşlar", "desc": "IGP, Koku, Çeviklik"},
            {"icon": "fa-fire", "title": "Hedef Kitle", "desc": "Yüksek Enerjili Irklar"},
            {"icon": "fa-dumbbell", "title": "Gelişim", "desc": "Fiziksel & Zihinsel"},
            {"icon": "fa-trophy", "title": "Seviye", "desc": "Profesyonel Spor"}
        ],
        "sec1_title": "Çalışmak İçin Doğan Köpekleri Koltukta Oturtamazsınız",
        "sec1_content": """
        <p>Belçika Malinois, Border Collie, Alman Kurdu, Jack Russell veya Av köpekleri gibi ırklar binlerce yıldır insanla birlikte aktif görev yapmak üzere üretilmiştir. Bu köpeklerin sahip olduğu devasa zihinsel ve fiziksel enerjiyi günde sadece 20 dakika mahallede yürüyerek boşaltamazsınız. Enerjisini boşaltamayan bir iş köpeği, bu gücü <strong>evi kemirerek, duvarları kazıyarak, takıntılar geliştirerek ya da agresyona yönelerek</strong> harcar.</p>
        <p>İş ve spor köpekleri programımız, bu muazzam potansiyeli spora, koku çalışmalarına ve üst düzey odak disiplinine dönüştürür. 15 dakikalık odaklı bir burun çalışması veya çeviklik parkuru, köpeğin beynini 3 saatlik koşudan çok daha derin bir huzurla sakinleştirir.</p>
        """,
        "curriculum": [
            {"num": "1", "title": "Koku Takibi & Arama Çalışmaları (Mantrailing & Tracking)", "desc": "Toprak ve çimende insan veya hedef nesne ayak izini koklayarak metrelerce takip etme yeteneğinin geliştirilmesi."},
            {"num": "2", "title": "IGP / Schutzhund Spor Temelleri", "desc": "Uluslararası standartlarda İz Sürme (Tracking), İtaat (Obedience) ve Koruma (Protection) fazlarının teknik inşası."},
            {"num": "3", "title": "Engel Parkuru & Çeviklik (Agility)", "desc": "Tüneller, atlama çıtaları, A-rampa ve slalom çubuklarında koordinasyon, esneklik ve yönlendirme yetisi."},
            {"num": "4", "title": "Oyuncak ve Isırma Dürtüsü Yönetimi (Ball / Tug Drive)", "desc": "Oyuncağı en yüksek ödül mekanizması haline getirerek patlayıcı bir motivasyonla komuta kilitlenme."},
            {"num": "5", "title": "Kondisyon, Güç ve Propriosepsiyon", "desc": "Kas gelişimi, denge tahtaları, arka ayak farkındalığı ve sakatlanmaları önleyici sporcu köpek fizyoterapisi temelleri."},
            {"num": "6", "title": "Zihinsel Sakinleşme & 'Off' Düğmesi", "desc": "Yüksek uyarılma düzeyindeki (High Drive) bir köpeğin iş bittiğinde anında sakinleşip ev moduna geçebilme disiplini."}
        ],
        "sec3_title": "Antrenman ve Gelişim Süreci",
        "process": [
            {"step": "1. Aşama", "title": "Dürtü ve İlgi Alanı Testi", "desc": "Köpeğin burun odaklı mı, oyuncak odaklı mı yoksa hareket odaklı mı çalıştığı analiz edilir; en uygun branş seçilir."},
            {"step": "2. Aşama", "title": "Teknik Modül Antrenmanları", "desc": "Haftalık periyotlarla özel engel parkurunda ve doğal arazilerde pozitif şekillendirme (shaping) teknikleriyle çalışılır."},
            {"step": "3. Aşama", "title": "Sahip ile Takım Uyumu", "desc": "Köpek sporları bir ikili yarışıdır. Sahip, köpeğini vücut diliyle milimetrik olarak nasıl yöneteceğini öğrenir."}
        ],
        "faqs": [
            {"q": "Sadece yarışmalara katılacak köpekler mi bu eğitimi alabilir?", "a": "Kesinlikle hayır! Evinde enerjisini atamayan, eşyaları kemiren veya hiperaktif iş ırkı besleyen her köpek sahibi bu eğitimle köpeğine harika bir yaşam kalitesi ve iç huzur kazandırabilir."},
            {"q": "Kaç yaşından itibaren spor eğitimine başlanabilir?", "a": "Oyun tabanlı koku ve takip çalışmaları 3 aylıktan itibaren başlatılabilir. Ağır fiziksel atlamalar ve eklemleri zorlayıcı engel parkurları ise kemik gelişimi tamamlandıktan sonra (12-14 ay) devreye girer."},
            {"q": "Köpeğimin çok yorulması agresyonunu azaltır mı?", "a": "Sadece fiziksel yorgunluk köpeğin kondisyonunu artırır ve onu daha fit yapar ama zihnini sakinleştirmez. Burun ve itaat odaklı zihinsel yorgunluk ise köpeğin iç dengesini sağlayarak tüm davranış sorunlarını minimize eder."}
        ],
        "related_slugs": ["kopegim-neden-kuyrugunu-kovaliyor", "kopegim-neden-surekli-kokluyor", "kopegim-neden-kaziyor"]
    }
]

def render_page(data):
    file_name = data["file_name"]
    meta_title = data["meta_title"]
    meta_desc = data["meta_desc"]
    bg_image = data["bg_image"]
    title = data["title"]
    lead = data["lead"]
    highlights = data["highlights"]
    sec1_title = data["sec1_title"]
    sec1_content = data["sec1_content"]
    curriculum = data["curriculum"]
    sec3_title = data["sec3_title"]
    process = data["process"]
    faqs = data["faqs"]
    related_slugs = data["related_slugs"]

    # WhatsApp Encoded Link
    wa_text = urllib.parse.quote(f"Merhaba, '{title}' hakkında detaylı bilgi ve randevu almak istiyorum.")
    wa_url = f"https://wa.me/905538860237?text={wa_text}"

    # Highlights HTML
    hl_html = []
    for hl in highlights:
        hl_html.append(f"""
        <div class="service-highlight-card" data-aos="fade-up">
          <i class="fas {hl['icon']}"></i>
          <h4>{hl['title']}</h4>
          <p>{hl['desc']}</p>
        </div>
        """)
    highlights_block = "".join(hl_html)

    # Curriculum HTML
    curr_html = []
    for c in curriculum:
        curr_html.append(f"""
        <div class="curriculum-item" data-aos="fade-up">
          <span class="curriculum-num">{c['num']}</span>
          <h3>{c['title']}</h3>
          <p>{c['desc']}</p>
        </div>
        """)
    curriculum_block = "".join(curr_html)

    # Process HTML
    proc_html = []
    for pr in process:
        proc_html.append(f"""
        <div class="process-step-box" data-aos="fade-up">
          <span class="step-badge">{pr['step']}</span>
          <h3>{pr['title']}</h3>
          <p>{pr['desc']}</p>
        </div>
        """)
    process_block = "".join(proc_html)

    # FAQs HTML
    faq_html = []
    for faq in faqs:
        faq_html.append(f"""
        <div class="service-faq-card" data-aos="fade-up">
          <h4><i class="fas fa-question-circle"></i> {faq['q']}</h4>
          <p>{faq['a']}</p>
        </div>
        """)
    faqs_block = "".join(faq_html)

    # Related Blogs HTML
    blog_cards_html = []
    for r_slug in related_slugs:
        p = blogs_by_slug.get(r_slug)
        if not p:
            continue
        p_title = p["title"]
        p_summary = p["summary"]
        p_category = p["category"]
        p_image = p["image"]

        blog_cards_html.append(f"""
        <a href="blog/{r_slug}.html" class="related-blog-card" data-aos="fade-up">
          <div class="related-blog-img-wrap">
            <img src="{p_image}" alt="{p_title}" loading="lazy">
            <span class="related-blog-badge">{p_category}</span>
          </div>
          <div class="related-blog-body">
            <h3>{p_title}</h3>
            <p>{p_summary}</p>
            <span class="related-blog-link">Rehberi Oku <i class="fas fa-arrow-right"></i></span>
          </div>
        </a>
        """)
    related_blogs_block = "".join(blog_cards_html)

    # Assemble Full HTML
    page_html = f"""<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{meta_title}</title>
  <meta name="description" content="{meta_desc}">
  <link rel="canonical" href="https://beytullahcekik.com/{file_name}" />
  <link rel="stylesheet" href="style.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
  <link rel="icon" href="assets/favicon.ico" type="image/x-icon">
  <link rel="apple-touch-icon" href="assets/favicon-192x192.png">
</head>
<body>
  <!-- Header -->
  <header class="main-header">
    <div class="container header-container">
      <a href="index.html" class="logo">
        <i class="fas fa-paw"></i>
        <span>Beytullah Çekik</span>
      </a>
      <nav class="main-nav">
        <ul>
          <li><a href="index.html">Ana Sayfa</a></li>
          <li><a href="hakkimda.html">Hakkımda</a></li>
          <li class="dropdown">
            <a href="javascript:void(0)" class="active">Eğitimlerimiz</a>
            <div class="dropdown-content">
              <a href="yavru-kopek-egitimi.html">Yavru Köpek Eğitimi</a>
              <a href="temel-itaat-egitimi.html">Temel İtaat Eğitimi</a>
              <a href="ileri-itaat-egitimi.html">İleri İtaat Eğitimi</a>
              <a href="tuvalet-egitimi.html">Tuvalet Eğitimi</a>
              <a href="davranis-bozuklugu-egitimi.html">Davranış Bozukluğu Eğitimi</a>
              <a href="alan-koruma-egitimi.html">Alan Koruma Eğitimi</a>
              <a href="kisi-koruma-egitimi.html">Kişi Koruma Eğitimi</a>
              <a href="is-ve-spor-kopekleri-egitimi.html">İş ve Spor Köpekleri Eğitimi</a>
            </div>
          </li>
          <li><a href="kopek-oteli.html">Otel</a></li>
          <li><a href="blog.html">Blog</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="service-page-hero" style="background-image: url('{bg_image}');">
    <div class="service-hero-overlay"></div>
    <div class="container">
      <div class="service-breadcrumbs" data-aos="fade-down">
        <a href="index.html">Ana Sayfa</a>
        <span class="sep"><i class="fas fa-chevron-right"></i></span>
        <span>Eğitimlerimiz</span>
        <span class="sep"><i class="fas fa-chevron-right"></i></span>
        <span>{title}</span>
      </div>
      <h1 data-aos="fade-up">{title}</h1>
      <p class="service-hero-lead" data-aos="fade-up" data-aos-delay="150">{lead}</p>
      <a href="{wa_url}" target="_blank" rel="noopener noreferrer" class="service-hero-cta" data-aos="fade-up" data-aos-delay="300">
        <i class="fab fa-whatsapp"></i> Birebir Bilgi & Randevu Al
      </a>
    </div>
  </section>

  <!-- Highlights Bar -->
  <div class="service-highlights-grid">
    {highlights_block}
  </div>

  <!-- Main Content Body -->
  <main class="service-main-wrapper">
    <!-- Section 1: Overview & Philosophy -->
    <article class="service-content-card" data-aos="fade-up">
      <h2><i class="fas fa-paw"></i> {sec1_title}</h2>
      {sec1_content}
    </article>

    <!-- Section 2: Curriculum & Program Modules -->
    <article class="service-content-card" data-aos="fade-up">
      <h2><i class="fas fa-clipboard-list"></i> Kapsamlı Eğitim Müfredatı ve Kazanımlar</h2>
      <p>Bu eğitim programı boyunca köpeğinizle adım adım işleyeceğimiz temel modüller ve kazandırılacak davranış kalıpları:</p>
      <div class="service-curriculum-grid">
        {curriculum_block}
      </div>
    </article>

    <!-- Section 3: Step by Step Process -->
    <article class="service-content-card" data-aos="fade-up">
      <h2><i class="fas fa-route"></i> {sec3_title}</h2>
      <p>Eğitim sürecimiz köpeğinizi strese sokmadan, gerçek yaşam şartlarına adım adım entegre eden planlı bir yöntemle yürütülür:</p>
      <div class="service-process-steps">
        {process_block}
      </div>
    </article>

    <!-- Section 4: FAQs -->
    <article class="service-content-card" data-aos="fade-up">
      <h2><i class="fas fa-comments"></i> Sıkça Sorulan Sorular</h2>
      <p>Bu eğitim hakkında köpek sahiplerinden en sık aldığımız sorular ve uzman yanıtlarımız:</p>
      <div class="service-faq-container">
        {faqs_block}
      </div>
    </article>

    <!-- Related Blogs Section -->
    <section class="service-related-section" data-aos="fade-up">
      <div class="service-related-header">
        <h2>Bu Eğitimle İlgili Uzman Blog Yazılarımız</h2>
        <p>Köpeğinizin davranışlarını, psikolojisini ve eğitim metotlarını daha yakından tanımanız için hazırladığımız rehberler.</p>
      </div>
      <div class="related-blogs-grid">
        {related_blogs_block}
      </div>
    </section>

    <!-- Bottom Call To Action Banner -->
    <div class="service-cta-banner" data-aos="zoom-in">
      <h2>Köpeğiniz İçin Ücretsiz Ön Değerlendirme Alın</h2>
      <p>İzmir'de yerinde eğitim ve profesyonel davranış analizi için Beytullah Çekik ile doğrudan iletişime geçin. Dostunuza en uygun programı birlikte belirleyelim.</p>
      <a href="{wa_url}" target="_blank" rel="noopener noreferrer" class="btn-cta-whatsapp">
        <i class="fab fa-whatsapp"></i> WhatsApp ile Hemen İletişime Geç
      </a>
    </div>
  </main>

  <!-- Footer Wave -->
  <div class="custom-shape-divider-top-footer">
    <svg data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" preserveAspectRatio="none">
        <path d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V120H0V95.8C59.71,118.08,130.83,119.3,191.9,106.1,236.4,96.53,279.7,76.51,321.39,56.44Z" class="shape-fill-footer"></path>
    </svg>
  </div>

  <!-- Footer -->
  <footer id="footer" class="footer">
    <div class="container">
      <div class="footer-columns" style="margin-top: 60px;">
        <div class="footer-col brand-col">
          <a href="index.html" class="logo footer-logo"><i class="fas fa-paw"></i><span>Beytullah Çekik</span></a>
          <p class="footer-about-text">İzmir'de pozitif pekiştirme ve bilimsel metotlarla profesyonel köpek eğitimi. Dostunuzla aranızdaki bağı teknikle güçlendiriyoruz.</p>
          <div class="footer-socials">
            <a href="https://instagram.com" target="_blank" rel="noopener noreferrer" title="Instagram"><i class="fab fa-instagram"></i></a>
          </div>
          <div class="footer-contact-inline">
            <p><i class="fas fa-phone"></i> +90 553 886 02 37</p>
            <p><i class="fas fa-map-marker-alt"></i> Menderes, İzmir</p>
          </div>
        </div>
        
        <div class="footer-col">
          <h4>Menü</h4>
          <ul>
            <li><a href="index.html">Ana Sayfa</a></li>
            <li><a href="hakkimda.html">Hakkımda</a></li>
            <li><a href="kopek-oteli.html">Köpek Oteli</a></li>
            <li><a href="blog.html">Blog</a></li>
          </ul>
        </div>
        
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

        <div class="footer-col">
          <h4>Yasal</h4>
          <ul>
            <li><a href="gizlilik-politikasi.html">Gizlilik Politikası</a></li>
            <li><a href="kullanim-kosullari.html">Kullanım Koşulları</a></li>
            <li><a href="guvenlik-kurallari.html">Güvenlik Kuralları</a></li>
            <li><a href="cerez-politikasi.html">Çerez Politikası</a></li>
          </ul>
        </div>
      </div>
      
      <div class="footer-legal-bottom">
        <p>&copy; 2026 Beytullah Çekik Köpek Eğitimi. Tüm hakları saklıdır.</p>
      </div>
    </div>
  </footer>

  <!-- Floating WhatsApp Button -->
  <a href="https://wa.me/905538860237" class="whatsapp-btn" target="_blank" rel="noopener noreferrer" data-aos="zoom-in" data-aos-delay="500">
    <i class="fab fa-whatsapp"></i> İletişime Geç
  </a>

  <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
  <script src="nav-dropdown.js"></script>
  <script>
    AOS.init({{ duration: 800, once: true, offset: 100 }});
  </script>
</body>
</html>
"""
    return page_html

for s in services_data:
    rendered = render_page(s)
    with open(s["file_name"], "w", encoding="utf-8") as out:
        out.write(rendered)
    print(f"Generated {s['file_name']} successfully with related blogs: {s['related_slugs']}")

print("All 8 education pages generated successfully!")
