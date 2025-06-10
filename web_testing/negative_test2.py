from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(1)

driver.find_element(By.ID, "userName").send_keys("Ali Testçi")
email_input = driver.find_element(By.ID, "userEmail")
email_input.send_keys("ali-example.com")  # Geçersiz e-posta
driver.find_element(By.ID, "currentAddress").send_keys("Bursa, Türkiye")
driver.find_element(By.ID, "permanentAddress").send_keys("Aynı")

submit_button = driver.find_element(By.ID, "submit")

# Form gönderilmeden önce e-posta input valid mi diye JS ile kontrol et
is_valid = driver.execute_script("return arguments[0].checkValidity();", email_input)
print("Email input valid mi?", is_valid)

if is_valid:
    # Valid ise submit et
    submit_button.click()
    time.sleep(2)
    print("Form gönderildi.")
else:
    print("Geçersiz e-posta, form gönderilmedi.")

driver.quit()
