from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Tarayıcıyı başlat
driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
driver.maximize_window()

# XSS payload
xss_payload = '<script>alert("XSS")</script>'

# Form alanlarını doldur
driver.find_element(By.ID, "userName").send_keys(xss_payload)
driver.find_element(By.ID, "userEmail").send_keys("test@example.com")
driver.find_element(By.ID, "currentAddress").send_keys("Deneme adres")
driver.find_element(By.ID, "permanentAddress").send_keys("Deneme adres")

# Submit butonuna tıkla
submit_button = driver.find_element(By.ID, "submit")
driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
submit_button.click()

# Sayfada alert çıkıyor mu? Gözle kontrol için bekle
time.sleep(5)

# Tarayıcıyı kapat
driver.quit()
