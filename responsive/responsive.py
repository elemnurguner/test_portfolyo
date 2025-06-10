from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def responsive_test_form_submission():
    # Test edilecek farklı ekran boyutları (genişlik, yükseklik)
    screen_sizes = [
        (375, 667),   # Mobil (iPhone 6/7/8)
        (768, 1024),  # Tablet (iPad)
        (1024, 768),  # Küçük dizüstü
        (1366, 768),  # Dizüstü
        (1920, 1080)  # Full HD masaüstü
    ]

    driver = webdriver.Chrome()
    
    for width, height in screen_sizes:
        driver.set_window_size(width, height)
        driver.get("https://demoqa.com/text-box")
        time.sleep(1)  # Sayfanın tam yüklenmesi için bekle

        print(f"Test ediliyor: Ekran boyutu {width}x{height}")

        # Formu doldur
        driver.find_element(By.ID, "userName").clear()
        driver.find_element(By.ID, "userName").send_keys(f"Test Kullanıcı {width}x{height}")
        driver.find_element(By.ID, "userEmail").clear()
        driver.find_element(By.ID, "userEmail").send_keys(f"test{width}x{height}@example.com")
        driver.find_element(By.ID, "currentAddress").clear()
        driver.find_element(By.ID, "currentAddress").send_keys("İstanbul")
        driver.find_element(By.ID, "permanentAddress").clear()
        driver.find_element(By.ID, "permanentAddress").send_keys("İstanbul")

        # Submit butonuna kaydır ve tıkla
        submit_button = driver.find_element(By.ID, "submit")
        driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        driver.execute_script("arguments[0].click();", submit_button)

        time.sleep(2)  # Formun gönderilip sayfanın tepki vermesi için bekle

        # Sonuç çıktılarını veya doğrulama mesajlarını kontrol edebilirsin
        output = driver.find_element(By.ID, "output").text
        print(f"Form gönderim sonucu ({width}x{height}):\n{output}\n{'-'*50}")

    driver.quit()

responsive_test_form_submission()
