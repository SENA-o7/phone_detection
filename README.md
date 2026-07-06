#  Telefon Tespiti ile Ders Çalışma Asistanı (Focus Guardian)

Merhaba! Ben bu projeyi, ders çalışırken telefonuma bakmaktan kendimi alıkoyamadığım için, tamamen kendi ihtiyacımı çözmek amacıyla geliştirdim. Masa başında geçirdiğim vakti daha verimli hale getirmek ve odaklanmamı sağlamak için yapay zeka destekli bir "Telefon Tespit Sistemi" kodladım.

##Projenin Amacı ve Çalışma Mantığı

Ders çalışırken en büyük dikkat dağıtıcımız telefonumuz. Bu proje bilgisayarınızın web kamerasını kullanarak anlık olarak sizi izliyor. Eğer ders çalışırken telefonu elinize alırsanız, sistem bunu YOLOv8 yapay zeka modelini kullanarak tespit ediyor.

Ekranda estetik bir **ilerleme çubuğu** (progress bar) beliriyor ve size telefonu bırakmanız için kısa bir süre tanıyor. Eğer telefonu **5 saniye boyunca** bırakmazsanız, sistem otomatik olarak belirlediğim caydırıcı bir YouTube videosunu açarak sizi uyarıyor. 

## Neler Yaptım? (Özellikler)

Bu projeyi geliştirirken sadece çalışmasına değil, aynı zamanda kullanıcı deneyimine ve esnekliğine de çok dikkat ettim:

*   **YOLOv8 ile Yüksek Başarılı Tespit:** Görüntü işleme ve nesne tespiti konusunda şu anki en gelişmiş modellerden biri olan YOLOv8'in `yolov8s` (Small) versiyonunu kullandım. Bu sayede telefon tespiti çok hızlı ve yüksek doğrulukla gerçekleşiyor.
*   ** Estetik ve Dinamik Arayüz (UI):** Sadece siyah bir ekranda yazı göstermek yerine OpenCV ile özel bir çizim fonksiyonu yazdım. Ekranın sağ üst köşesinde beliren, doldukça renk değiştiren (Sarı  -> Turuncu  -> Kırmızı ) estetik bir dairesel ilerleme çubuğu bulunuyor.
*   **⏱️ Akıllı Tolerans Sistemi (Grace Period):** Telefonu masanın üzerinde hareket ettirirken veya kameranın görüş açısından 1-2 saniyeliğine çıktığında sistemin haksız yere ceza vermemesi için **2 saniyelik bir tolerans süresi (Grace Period)** kodladım. Eğer telefonu elinizden bırakırsanız sayaç anında sıfırlanıyor.
*   ** Otomatik Uyarı Mekanizması:** 5 saniyelik limit dolduğunda Python'un `webbrowser` kütüphanesi tetikleniyor ve otomatik olarak bir uyarı/motivasyon videosu açılıyor.
*   ** Optimize Edilmiş Eşik Değerleri:** Kameranın ortamdaki başka objeleri (kalem kutusu, hesap makinesi vb.) telefon sanmaması için güven oranını (Confidence Score) titizlikle ayarladım (%45-%55 arası optimum değer kullanıldı).

## 🛠️ Kullanılan Teknolojiler

*   **Python:** Projenin çekirdek dili.
*   **OpenCV (`cv2`):** Kameradan canlı görüntü almak, görüntüleri işlemek ve ekrandaki estetik UI elementlerini çizmek için.
*   **Ultralytics (YOLOv8):** Derin öğrenme tabanlı nesne tespiti için.

##  Kurulum ve Çalıştırma

Projeyi kendi bilgisayarınızda çalıştırmak oldukça basit!

### 1. Gerekli Kütüphaneleri Yükleyin
Terminalinizi veya Spyder/VSCode konsolunuzu açıp aşağıdaki komutu çalıştırın:
```bash
pip install opencv-python ultralytics
```

### 2. Projeyi Çalıştırın
Sadece ana Python dosyasını çalıştırmanız yeterli:
```bash
python phone_detector.py
```

> **Not:** Kodu ilk kez çalıştırdığınızda, YOLOv8'in yaklaşık 20 MB boyutundaki ağırlık dosyası (`yolov8s.pt`) otomatik olarak internetten indirilecektir. Projenin boyutunu şişirmemek adına bu ağırlık dosyalarını `.gitignore` içerisine ekledim ve GitHub'a yüklemedim.

## 🤝 Katkıda Bulunma
Bu proje açık kaynaklıdır ve geliştirmeye açıktır. Eğer aklınıza yeni bir özellik gelirse (örneğin sesi kapatma, farklı cezalar ekleme vs.) Pull Request göndermekten çekinmeyin!

Projemi incelediğiniz için teşekkürler! Umarım sizin de odaklanmanıza yardımcı olur. 🎯 Başarılar!
