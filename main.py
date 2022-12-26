from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

playing = False
chrome_driver_path = "/Users/qigui/Downloads/chromedriver"

driver = webdriver.Chrome(service=Service(chrome_driver_path))
driver.get("https://orteil.dashnet.org/experiments/cookie/")




item_name = []


items = driver.find_elements(By.CSS_SELECTOR, value="#store div")
for item in items:
    item_name.append(item.get_attribute("id"))

print(item_name)

five_sec = time.time() + 5

count = driver.find_element(By.ID, value="cookie")

while not playing:
    count.click()
    affordable = []
    item_price = []
    if time.time() > five_sec:
        five_sec = time.time() + 5
        money = driver.find_element(By.ID, value="money").text
        store = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        for item in store:
            if item.text != "":
                x = item.text.split("-")
                item_price.append(int(x[1].strip().replace(",","")))
        for price in item_price:
            if int(money.replace(",","")) >= price:
                affordable.append(price)
        higher = max(affordable)
        num_1 = item_price.index(higher)
        print(affordable)
        print(higher)
        print(item_name[num_1])
        product = driver.find_element(By.ID, value=item_name[num_1])
        product.click()




