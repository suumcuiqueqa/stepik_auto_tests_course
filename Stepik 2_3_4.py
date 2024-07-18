from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_element = browser.find_element(By.ID, "input_value")
    x = calc(x_element.text)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    input = browser.find_element(By.ID, "answer")
    input.send_keys(x)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()