from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def sum(a,b):
   return str(int(a)+int(b))

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    a = browser.find_element(By.ID,"num1")
    b = browser.find_element(By.ID,"num2")
    c = sum(a.text,b.text)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(c)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()