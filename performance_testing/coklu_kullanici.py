from selenium import webdriver
from selenium.webdriver.common.by import By
import threading
import time

def fill_form(user_index):
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/text-box")
    driver.maximize_window()
    time.sleep(1)

    driver.find_element(By.ID, "userName").send_keys(f"Kullanıcı {user_index}")
    driver.find_element(By.ID, "userEmail").send_keys(f"user{user_index}@example.com")
    driver.find_element(By.ID, "currentAddress").send_keys("İstanbul")
    driver.find_element(By.ID, "permanentAddress").send_keys("İstanbul")

    submit_button = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    driver.execute_script("arguments[0].click();", submit_button)
    time.sleep(2)

    driver.quit()

threads = []
for i in range(5):  # 5 paralel kullanıcı simülasyonu
    t = threading.Thread(target=fill_form, args=(i,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

