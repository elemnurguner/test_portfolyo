from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from concurrent.futures import ThreadPoolExecutor

def fill_form(user_data):
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/text-box")
    driver.maximize_window()
    time.sleep(1)

    driver.find_element(By.ID, "userName").send_keys(user_data["name"])
    driver.find_element(By.ID, "userEmail").send_keys(user_data["email"])
    driver.find_element(By.ID, "currentAddress").send_keys(user_data["currentAddress"])
    driver.find_element(By.ID, "permanentAddress").send_keys(user_data["permanentAddress"])

    submit_button = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    driver.execute_script("arguments[0].click();", submit_button)
    time.sleep(2)

    output = driver.find_element(By.ID, "output").text
    print(f"User {user_data['name']} submission output:\n{output}\n")

    driver.quit()

users = [
    {"name": "Ali Testçi", "email": "ali@example.com", "currentAddress": "Bursa, Türkiye", "permanentAddress": "Aynı"},
    {"name": "Ayşe Kullanıcı", "email": "ayse@example.com", "currentAddress": "İstanbul, Türkiye", "permanentAddress": "Farklı"},
    {"name": "Mehmet Örnek", "email": "mehmet@example.com", "currentAddress": "Ankara, Türkiye", "permanentAddress": "Aynı"},
    {"name": "Fatma Deneme", "email": "fatma@example.com", "currentAddress": "İzmir, Türkiye", "permanentAddress": "Farklı"},
    {"name": "Can Test", "email": "can@example.com", "currentAddress": "Adana, Türkiye", "permanentAddress": "Aynı"},
]

with ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(fill_form, users)

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from concurrent.futures import ThreadPoolExecutor

def fill_form(user_data):
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/text-box")
    driver.maximize_window()
    time.sleep(1)

    driver.find_element(By.ID, "userName").send_keys(user_data["name"])
    driver.find_element(By.ID, "userEmail").send_keys(user_data["email"])
    driver.find_element(By.ID, "currentAddress").send_keys(user_data["currentAddress"])
    driver.find_element(By.ID, "permanentAddress").send_keys(user_data["permanentAddress"])

    submit_button = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    driver.execute_script("arguments[0].click();", submit_button)
    time.sleep(2)

    output = driver.find_element(By.ID, "output").text
    print(f"User {user_data['name']} submission output:\n{output}\n")

    driver.quit()

users = [
    {"name": "Ali Testçi", "email": "ali@example.com", "currentAddress": "Bursa, Türkiye", "permanentAddress": "Aynı"},
    {"name": "Ayşe Kullanıcı", "email": "ayse@example.com", "currentAddress": "İstanbul, Türkiye", "permanentAddress": "Farklı"},
    {"name": "Mehmet Örnek", "email": "mehmet@example.com", "currentAddress": "Ankara, Türkiye", "permanentAddress": "Aynı"},
    {"name": "Fatma Deneme", "email": "fatma@example.com", "currentAddress": "İzmir, Türkiye", "permanentAddress": "Farklı"},
    {"name": "Can Test", "email": "can@example.com", "currentAddress": "Adana, Türkiye", "permanentAddress": "Aynı"},
]

with ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(fill_form, users)
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from concurrent.futures import ThreadPoolExecutor

def fill_form(user_data):
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/text-box")
    driver.maximize_window()
    time.sleep(1)

    driver.find_element(By.ID, "userName").send_keys(user_data["name"])
    driver.find_element(By.ID, "userEmail").send_keys(user_data["email"])
    driver.find_element(By.ID, "currentAddress").send_keys(user_data["currentAddress"])
    driver.find_element(By.ID, "permanentAddress").send_keys(user_data["permanentAddress"])

    submit_button = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    driver.execute_script("arguments[0].click();", submit_button)
    time.sleep(2)

    output = driver.find_element(By.ID, "output").text
    print(f"User {user_data['name']} submission output:\n{output}\n")

    driver.quit()

users = [
    {"name": "Ali Testçi", "email": "ali@example.com", "currentAddress": "Bursa, Türkiye", "permanentAddress": "Aynı"},
    {"name": "Ayşe Kullanıcı", "email": "ayse@example.com", "currentAddress": "İstanbul, Türkiye", "permanentAddress": "Farklı"},
    {"name": "Mehmet Örnek", "email": "mehmet@example.com", "currentAddress": "Ankara, Türkiye", "permanentAddress": "Aynı"},
    {"name": "Fatma Deneme", "email": "fatma@example.com", "currentAddress": "İzmir, Türkiye", "permanentAddress": "Farklı"},
    {"name": "Can Test", "email": "can@example.com", "currentAddress": "Adana, Türkiye", "permanentAddress": "Aynı"},
]

with ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(fill_form, users)