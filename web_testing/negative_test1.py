from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(1)

# Yanlış email yaz
driver.find_element(By.ID, "userName").send_keys("Ali Testçi")
driver.find_element(By.ID, "userEmail").send_keys("ali-example.com")  # geçersiz email (yok @)
driver.find_element(By.ID, "currentAddress").send_keys("Bursa, Türkiye")
driver.find_element(By.ID, "permanentAddress").send_keys("Aynı")

# Submit butonunu JS ile tıkla
submit_button = driver.find_element(By.ID, "submit")
driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
driver.execute_script("arguments[0].click();", submit_button)
time.sleep(2)

# Hata mesajı var mı kontrol et
error_elements = driver.find_elements(By.CSS_SELECTOR, "input:invalid")
if error_elements:
    print("Geçersiz input var, form doğrulama çalışıyor.")
else:
    print("Hata mesajı yok, form doğrulama görünür değil.")

driver.quit()
