from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = calc(x_element.text)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(x)
    robot = browser.find_element(By.ID, "robotCheckbox")
    robot.click()
    rule = browser.find_element(By.ID, "robotsRule")
    rule.click()
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()