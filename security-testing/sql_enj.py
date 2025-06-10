from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
driver.maximize_window()

# SQL injection payload
payload = "' OR '1'='1"

# Formu doldur
driver.find_element(By.ID, "userName").send_keys(payload)
driver.find_element(By.ID, "userEmail").send_keys("test@example.com")
driver.find_element(By.ID, "currentAddress").send_keys("deneme")
driver.find_element(By.ID, "permanentAddress").send_keys("deneme")

# Submit
submit_button = driver.find_element(By.ID, "submit")
driver.execute_script("arguments[0].click();", submit_button)
time.sleep(2)

# Hata, uyarı, beklenmeyen durum var mı kontrol et
try:
    output = driver.find_element(By.ID, "output")
    print("Form sonucu:", output.text)
except:
    print("Beklenmedik davranış olabilir. Form sonucu bulunamadı.")

driver.quit()
