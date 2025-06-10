# Performance Testing
Bu klasör, bir web formu (https://demoqa.com/text-box) üzerinde yapılan çeşitli performans testi senaryolarını içermektedir. Amaç, form sayfasının eş zamanlı kullanıcılar tarafından nasıl işlendiğini ve sistemin bu yüke verdiği tepkiyi değerlendirmektir.

# Kullanılan Teknolojiler
Python

Selenium WebDriver

Locust

Threading / ThreadPoolExecutor

# Proje Listesi
1️⃣ Paralel Form Doldurma (Zaman Ölçümü ile) – performance_test_1.py
Amaç: 5 farklı kullanıcıyı aynı anda simüle ederek formu doldurup gönderme süresini ölçmek.

Teknoloji: Selenium + Threading

Açıklama: Her thread bir kullanıcıyı temsil eder. Tarayıcı başlatılır, form doldurulur, gönderilir ve süre hesaplanır.

Avantaj: Test süresinin ölçülmesi ile sistemin yük altında yanıt süresi analiz edilebilir.

2️⃣ Basit Paralel Form Doldurma – performance_test_2.py
Amaç: Formun paralel olarak 5 kullanıcı ile doldurulması.

Teknoloji: Selenium + Threading

Açıklama: Zaman ölçümü yapılmadan sadece eş zamanlı kullanım testi gerçekleştirilir.

Avantaj: Basit senaryolarla performans testine giriş için idealdir.

3️⃣ Kullanıcı Verisiyle Eşzamanlı Test – performance_test_3.py
Amaç: Gerçekçi kullanıcı verileriyle (isim, e-posta, adres) paralel form doldurma testi yapmak.

Teknoloji: Selenium + ThreadPoolExecutor

Açıklama: Her kullanıcı özgün veri ile formu doldurur. Çıktı konsola yazdırılır.

Avantaj: Test çıktısı okunabilir, hata var mı kontrol edilebilir. Performans ve doğruluk beraber test edilir.

4️⃣ Locust ile Yük Testi – locustfile.py
Amaç: Yük altında sayfanın cevap süresini ölçmek.

Teknoloji: Locust

Açıklama: Locust üzerinden yapılan /text-box GET isteğiyle form sayfasının yük altında yanıt süresi analiz edilir.

Avantaj: Yük testi için endüstride yaygın olarak kullanılan bir araç olan Locust ile profesyonel test yapılabilir.

# Kurulum ve  Kullanım 
Selenium Testleri için 
Terminalde:
pip install selenium  yazılmalı 

Locust Testi için:
Terminalde :
pip install locust
Örnek Kullanım Senaryosu:
cd "C:\Users\USER\Desktop\test\test_pertfolyo\performance_testing"
python -m locust -f locustfile.py
 http://localhost:8089,

Açılan  pencerede   test edeceğin sayfanın hostunu da girmelesin:
https://demoqa.com ben  bunu test ettim.