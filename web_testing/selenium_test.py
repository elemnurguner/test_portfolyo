from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_form(driver):
    driver.get("https://demoqa.com/text-box")
    driver.maximize_window()
    time.sleep(1)

    driver.find_element(By.ID, "userName").send_keys("Test Kullanıcısı")
    driver.find_element(By.ID, "userEmail").send_keys("test@example.com")
    driver.find_element(By.ID, "currentAddress").send_keys("İstanbul")
    driver.find_element(By.ID, "permanentAddress").send_keys("İstanbul")

    submit_button = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    driver.execute_script("arguments[0].click();", submit_button)
    time.sleep(1)

    output = driver.find_element(By.ID, "output").text
    assert "Test Kullanıcısı" in output

    driver.quit()

# Chrome ile test
# chrome_driver = webdriver.Chrome()
# test_form(chrome_driver)

# edge
edge = webdriver.Edge()
test_form(edge)
