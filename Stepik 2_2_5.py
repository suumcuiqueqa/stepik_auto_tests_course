from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = calc(x_element.text)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(x)
    robot = browser.find_element(By.ID, "robotCheckbox")
    robot.click()
    browser.execute_script("window.scrollBy(0, 100);")
    rule = browser.find_element(By.ID, "robotsRule")
    rule.click()

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(30)
    browser.quit()