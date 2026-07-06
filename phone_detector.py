import cv2
import time
import webbrowser
import math

try:
    from ultralytics import YOLO
except ImportError:
    print("YOLO kütüphanesi bulunamadı!")
    print("Lütfen Spyder konsoluna şunu yazıp çalıştırın: !pip install ultralytics")
    import sys
    sys.exit()

def draw_circular_progress(frame, center, radius, progress, color, text_inside, thickness=6):
    """Ekrana estetik ve yuvarlak bir ilerleme çubuğu çizer"""
    # Arka plan dairesi (yarı saydam veya koyu gri)
    cv2.circle(frame, center, radius, (60, 60, 60), thickness)
    
    # İlerleme yayı
    angle = progress * 360
    # Başlangıç açısı -90 derece (en tepe)
    cv2.ellipse(frame, center, (radius, radius), -90, 0, angle, color, thickness)
    
    # Ortasına yazıyı ekle
    font = cv2.FONT_HERSHEY_SIMPLEX
    text_size = cv2.getTextSize(text_inside, font, 0.6, 2)[0]
    text_x = center[0] - text_size[0] // 2
    text_y = center[1] + text_size[1] // 2
    cv2.putText(frame, text_inside, (text_x, text_y), font, 0.6, color, 2)

def main():
    print("Sistem başlatılıyor...")
    # Daha iyi tespit için yolov8s (Small) modeli kullanıyoruz
    model = YOLO("yolov8s.pt") 
    
    cap = cv2.VideoCapture(0)
    
    # Zamanlayıcı değişkenleri
    phone_detected_start_time = None
    last_seen_time = None
    last_conf = 0.0
    
    ALARM_THRESHOLD = 5.0  # Süre 5 saniyeye düşürüldü
    GRACE_PERIOD = 2.0    # Telefon anlık ekrandan çıkarsa 2 saniye tolerans tanı (Sıfırlama!)
    
    YOUTUBE_LINK = "https://www.youtube.com/shorts/KhdECw7tG3g" 
    video_opened_this_session = False 
    
    print("Kamera açıldı! Estetik mod aktif.")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        frame = cv2.flip(frame, 1)
        h, w = frame.shape[:2]
            
        # Telefonun tespiti için emin olma eşiği (confidence) %55 (0.55) yapıldı
        results = model(frame, stream=True, verbose=False, conf=0.45)
        
        phone_in_frame = False
        max_conf = 0.0
        
        for r in results:
            boxes = r.boxes
            for box in boxes:
                cls = int(box.cls[0])
                if cls == 67: # Cell phone
                    phone_in_frame = True
                    conf = float(box.conf[0])
                    if conf > max_conf:
                        max_conf = conf
                    
                    # mor dikdörtgen çiz (BGR: 255, 105, 180)
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 105, 180), 3) 
                    cv2.putText(frame, "TELEFON", (x1, max(20, y1 - 10)), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 105, 180), 2)
                        
        if phone_in_frame:
            last_conf = max_conf
        
        current_time = time.time()
        
        # Zamanlayıcı ve Tolerans Mantığı
        if phone_in_frame:
            # Telefonu gördük, son görülme anını güncelle
            last_seen_time = current_time
            if phone_detected_start_time is None:
                phone_detected_start_time = current_time
                video_opened_this_session = False
        else:
            # Telefonu anlık göremedik, tolerans süresi doldu mu?
            if last_seen_time is not None:
                if current_time - last_seen_time > GRACE_PERIOD:
                    # Tolerans süresi bitti, gerçekten telefonu kaldırmış
                    phone_detected_start_time = None
                    last_seen_time = None
        
        # Yuvarlak ilerleme (progress) çubuğunu çiz
        if phone_detected_start_time is not None and not video_opened_this_session:
            elapsed_time = current_time - phone_detected_start_time
            progress = min(1.0, elapsed_time / ALARM_THRESHOLD)
            
            # Renkler: Başta yeşil -> Sarı -> Sona yaklaşınca Kırmızı
            if progress > 0.8:
                color = (0, 0, 255) # Kırmızı
            elif progress > 0.5:
                color = (0, 165, 255) # Turuncu
            else:
                color = (0, 255, 255) # Sarı
                
            # Süreyi 1, 2, 3, 4, 5 şeklinde yazdır
            elapsed_sec = int(elapsed_time) + 1
            if elapsed_sec > 5: elapsed_sec = 5
            text_inside = f"{elapsed_sec} sn"
            
            # Sağ üst köşeye yuvarlak menüyü çiz (Merkez x, y ve yarıçap)
            center_x = w - 80
            center_y = 80
            draw_circular_progress(frame, (center_x, center_y), 45, progress, color, text_inside, thickness=8)
            
            # Ufak estetik uyarı yazısı
            cv2.putText(frame, "Odaklan...", (center_x - 35, center_y + 70), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
            
            # Telefon Benzerlik (Eminlik) yüzdesi
            cv2.putText(frame, f"Eminlik: %{int(last_conf * 100)}", (center_x - 45, center_y + 90), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)
            
            # 5 saniye dolduysa ve video açılmadıysa
            if elapsed_time >= ALARM_THRESHOLD:
                print("5 Saniye doldu! Video açılıyor...")
                webbrowser.open(YOUTUBE_LINK)
                video_opened_this_session = True
                phone_detected_start_time = None 
                last_seen_time = None
                
        # Ekrana yansıt
        cv2.imshow("Ders Takip Sistemi - Estetik Mod", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
