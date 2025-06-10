from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
html = driver.page_source

if 'csrf_token' in html.lower():
    print("Sayfada CSRF token bulundu.")
else:
    print("Sayfada CSRF token bulunamadı.")
driver.quit()