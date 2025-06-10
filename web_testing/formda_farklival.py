from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(1)

driver.find_element(By.ID, "userName").send_keys("Test Kullanıcı")
driver.find_element(By.ID, "userEmail").send_keys("gecersiz-email")  # Hatalı email
driver.find_element(By.ID, "currentAddress").send_keys("Test Adresi")
driver.find_element(By.ID, "permanentAddress").send_keys("Test Adresi")

submit_button = driver.find_element(By.ID, "submit")
driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
driver.execute_script("arguments[0].click();", submit_button)
time.sleep(2)

email_input = driver.find_element(By.ID, "userEmail")
validation_message = driver.execute_script("return arguments[0].validationMessage;", email_input)
print("Validation Message:", validation_message)

driver.quit()
