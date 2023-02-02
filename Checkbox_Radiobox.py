import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://suninjuly.github.io/math.html")

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x_element = driver.find_element(By.ID, 'input_value')
x = x_element.text
res = calc(x)




try:
    result = driver.find_element(By.ID, "answer").send_keys(res)

    check = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']").click()
    time.sleep(1)

    rule = driver.find_element(By.ID, "robotsRule").click()
    time.sleep(1)

    button = driver.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(2)

finally:
    time.sleep(2)
    driver.quit()
