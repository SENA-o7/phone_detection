# Telefon Tespiti ile Ders Çalışma Asistanı 📚🚫📱

Merhaba! Ben bu projeyi ders çalışırken telefonuma bakmaktan kendimi alıkoyamadığım için geliştirdim. Ders çalışırken odaklanmamı sağlamak için yapay zeka destekli bir "Telefon Tespit Sistemi" yaptım.

## Proje Ne İşe Yarıyor? 🤔
Ders çalışırken eğer telefonumu elime alırsam, kameram bunu tespit ediyor. Ekranda estetik bir ilerleme çubuğu beliriyor ve eğer telefonu **5 saniye** boyunca bırakmazsam otomatik olarak beni uyaracak bir video açılıyor. (Küçük bir tolerans payı da ekledim, eğer telefonu anlık olarak ekrandan çekersem sayaç sıfırlanıyor.)

## Kullanılan Teknolojiler 🛠️
*   **Python:** Projenin ana dili.
*   **OpenCV (cv2):** Kameradan görüntü almak ve ekrana estetik yuvarlak ilerleme çubuğunu çizmek için.
*   **YOLOv8 (Ultralytics):** Görüntüdeki telefonu anlık ve yüksek doğrulukla tespit etmek için YOLOv8'in hafif ve hızlı olan `yolov8s` (Small) modelini kullandım.

## Özellikler ✨
*   **Gerçek Zamanlı Tespit:** YOLOv8 ile kameradan canlı olarak telefon tespiti.
*   **Estetik Arayüz:** Sadece dümdüz yazılar değil, ekranda beliren, doldukça renk değiştiren (sarı -> turuncu -> kırmızı) yuvarlak bir ilerleme çubuğu ekledim.
*   **Tolerans Sistemi:** Telefonu 1-2 saniyeliğine görüp kaybetmesi durumunda hemen ceza vermemesi için 2 saniyelik bir `GRACE_PERIOD` (tolerans süresi) tanımladım.
*   **Otomatik Uyarı:** 5 saniye dolduğunda otomatik olarak belirlediğim bir YouTube videosu açılıyor.

## Nasıl Çalıştırılır? 🚀

1.  Öncelikle gerekli kütüphaneleri yüklemeniz gerekiyor. Terminalinize (veya Spyder konsolunuza) şu komutu yazabilirsiniz:
    ```bash
    pip install opencv-python ultralytics
    ```
2.  `phone_detector.py` dosyasını çalıştırın.
3.  İlk çalıştırdığınızda `yolov8s.pt` ağırlık dosyası otomatik olarak inecektir. (Bu yüzden `.gitignore` içerisine `.pt` dosyalarını ekledim ki Github'ı gereksiz yere doldurmasın.)
4.  Kamera açılacak ve sistem çalışmaya başlayacaktır!

Projemi incelediğiniz için teşekkürler! Umarım sizin de odaklanmanıza yardımcı olur. 🎯
