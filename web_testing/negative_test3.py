from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(1)

# Zorunlu alanları boş bırakıyoruz
driver.find_element(By.ID, "userName").clear()
driver.find_element(By.ID, "userEmail").clear()
driver.find_element(By.ID, "currentAddress").clear()
driver.find_element(By.ID, "permanentAddress").clear()

# Scroll yap ve JS ile butona tıkla
submit_button = driver.find_element(By.ID, "submit")
driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
driver.execute_script("arguments[0].click();", submit_button)
time.sleep(1)

# Hata mesajı veya herhangi bir engelleme var mı kontrol edelim
error_elements = driver.find_elements(By.CSS_SELECTOR, ".field-error")  # örnek selector, değişebilir
assert len(error_elements) > 0, "Hata mesajı görünmeli, ama görünmüyor."

driver.quit()
