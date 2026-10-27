import re

# 1. kopegim-neden-beni-takip-ediyor.md
with open('posts/kopegim-neden-beni-takip-ediyor.md', 'r', encoding='utf-8') as f:
    text = f.read()

extra_beni_takip = """
### Güvenli Alan Çalışması ve Zihinsel Bağımsızlık Egzersizleri
Köpeğinizin sizin varlığınıza aşırı bağımlı olmasını engellemenin en etkili yollarından biri, ona kendi başına vakit geçirmeyi ve bundan keyif almayı öğretmektir. Gün içinde köpeğiniz yatağındayken veya sakin bir köşedeyken, onun içine lezzetli ödüller veya fıstık ezmesi doldurulmuş zeka oyuncakları verin. Bu aktivite sırasında kapıyı kapatmadan ama köpeğinizle göz teması kurmadan farklı bir odaya geçin. 

Köpek, sizin odadan çıkışınızı bir felaket olarak değil, tam aksine harika bir ödülün başlangıcı olarak kodlamaya başlayacaktır. Zihinsel yorgunluk, köpeğin sinir sistemini yatıştırır ve sürekli fiziksel olarak peşinizden koşma dürtüsünü doğal yoldan dindirir. İzmir'deki saha eğitimlerimizde bağımsızlık egzersizlerini günlük rutine ekleyen ailelerde, takip davranışının ilk 10 gün içinde yarı yarıya azaldığını gözlemliyoruz.
"""

if "Güvenli Alan Çalışması" not in text:
    text = text.replace("## Sıkça Sorulan Sorular", extra_beni_takip + "\n## Sıkça Sorulan Sorular")
    with open('posts/kopegim-neden-beni-takip-ediyor.md', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated kopegim-neden-beni-takip-ediyor.md")

# 2. kopegim-neden-kuyrugunu-kovaliyor.md
with open('posts/kopegim-neden-kuyrugunu-kovaliyor.md', 'r', encoding='utf-8') as f:
    text = f.read()

extra_kuyruk = """
### Çevresel Zenginleştirme ve Dürtü Kanalizasyonu
Kuyruk yakalama eğiliminde olan köpekler genellikle yüksek av güdüsüne ve yoğun zihinsel kapasiteye sahip ırklardır (Alman Çoban Köpeği, Bull Terrier, Border Collie vb.). Bu köpekler zihinsel olarak meşgul edilmediklerinde, kendi bedenlerini birer av simülasyonuna dönüştürürler. 

Sorunun kalıcı çözümü için köpeğin av güdüsünü kontrollü araçlara yönlendirmeliyiz. 'Flirt pole' (ucunda oyuncak olan uzun olta çubuğu) ile kontrollü yakalama oyunları oynamak, koku takibi egzersizleri yaptırmak ve getirme (fetch) oyunlarında 'bırak' ve 'bekle' komutlarıyla dürtü kontrolü sağlamak harika sonuçlar verir. Enerjisini sahada doğru şekilde akıtan ve zihnini kullanan bir köpeğin evde kendi kuyruğuna takıntı geliştirmesi neredeyse imkansız hale gelir.
"""

if "Çevresel Zenginleştirme" not in text:
    text = text.replace("## Sıkça Sorulan Sorular", extra_kuyruk + "\n## Sıkça Sorulan Sorular")
    with open('posts/kopegim-neden-kuyrugunu-kovaliyor.md', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated kopegim-neden-kuyrugunu-kovaliyor.md")

# 3. kopegim-neden-titriyor.md
with open('posts/kopegim-neden-titriyor.md', 'r', encoding='utf-8') as f:
    text = f.read()

extra_titreme = """
### Heyecan ve Beklenti Titremeleri ile Stres Titremesi Arasındaki Fark
Köpek sahiplerinin en çok karıştırdığı konulardan biri, köpeğin aşırı neşeli bir beklenti anındaki titremesi ile korkudan kaynaklanan titremesidir. Köpeğiniz tasma takılırken, araba yolculuğuna çıkacakken veya sevdiği bir topu fırlatmanızı beklerken heyecandan titreyebilir. Bu tip titremelerde kulaklar dik, kuyruk geniş açıyla sallanır ve beden öne doğru hamle halindedir. 

Korku ve stres kaynaklı titremelerde ise köpek adeta küçülmeye çalışır; ağırlık merkezi arkaya kayar, gözbebekleri büyür ve vücut aşırı kaskatı kesilir. Eğer köpeğiniz heyecandan kontrolsüzce titriyorsa, sakinleşme sinyali alana kadar aktiviteyi başlatmamak (örneğin sakin oturana kadar kapıyı açmamak veya tasmayı takmamak) heyecan titremesini kısa sürede dengeler.
"""

if "Heyecan ve Beklenti Titremeleri" not in text:
    text = text.replace("## Sıkça Sorulan Sorular", extra_titreme + "\n## Sıkça Sorulan Sorular")
    with open('posts/kopegim-neden-titriyor.md', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated kopegim-neden-titriyor.md")

# 4. kopegim-neden-uluyor.md
with open('posts/kopegim-neden-uluyor.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Update title to 50-65 chars
text = re.sub(r'title:\s*"[^"]*"', 'title: "Köpeğim Neden Uluyor? Uluma Nedenleri ve Eğitim Yolları"', text)

extra_uluma = """
### Siren, Ezan ve Müzik Seslerine Karşı Duyarsızlaştırma Çalışması
Ambulans sirenleri, ezan sesi veya belirli müzik enstrümanları köpeklerin atalarından kalan uluma refleksini anında tetikleyebilir. Köpeğinizin bu seslere karşı tepkisini yönetmek için 'karşıt koşullandırma' ve 'duyarsızlaştırma' tekniği uygulanmalıdır.

Siren veya tetikleyici sesin kaydını telefonunuzdan açın, ancak sesi köpeğin henüz tepki vermeyeceği en düşük seviyede tutun. Ses çalarken köpeğinize en sevdiği ödül mamasını verin veya sevdiği bir oyuncağıyla ilgilenmesini sağlayın. Günler içinde ses düzeyini kademe kademe artırırken, köpeğinizin dikkatinin sizde kalmasını sağlayın. Böylece yüksek frekanslı sesler köpek için 'ulunması gereken bir sürü çağrısı' olmaktan çıkıp, 'sakince bekleyince ödül getiren sıradan bir arka plan sesi' haline dönüşecektir.
"""

if "Siren, Ezan ve Müzik Seslerine" not in text:
    text = text.replace("## Sıkça Sorulan Sorular", extra_uluma + "\n## Sıkça Sorulan Sorular")
    with open('posts/kopegim-neden-uluyor.md', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated kopegim-neden-uluyor.md")
