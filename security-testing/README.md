Bu proje, bir web formu üzerinde temel güvenlik açıklarını test etmek amacıyla Selenium kullanılarak hazırlanmış örnek scriptleri içerir. Test edilen güvenlik açıkları:

SQL Injection

Cross-Site Scripting (XSS)

CSRF Token kontrolü
 SQL Injection Testi (sql_injection_test.py)
Test Edilen: Kullanıcı adı alanına SQL enjeksiyon payload'u girilerek formun beklenmedik davranış gösterip göstermediği test edilir.
Test Adımları:

userName alanına payload gönderilir

Diğer alanlar doldurulur ve form gönderilir

Formun çıktısı kontrol edilir (beklenmeyen veri gösterimi var mı)


2- XSS (Cross-Site Scripting) Testi (xss_test.py)
Test Edilen: Script etiketli zararlı veri girildiğinde alert() çalışıyor mu, tarayıcı bunu engelliyor mu kontrol edilir.
Test Adımları:

userName alanına XSS payload'u girilir

Form gönderilir

alert() penceresi açılıyor mu gözlemlenir

3-CSRF Token Kontrolü (csrf_token_check.py)
Test Edilen: Sayfanın HTML içeriğinde bir csrf_token olup olmadığı kontrol edilir.

Bu testler demo bir site olan https://demoqa.com/text-box üzerinde çalışır.