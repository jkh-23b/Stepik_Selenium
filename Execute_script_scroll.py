import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://suninjuly.github.io/execute_script.html")
time.sleep(1)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

number = driver.find_element(By.ID, "input_value")
x = number.text
res = calc(x)

try:
    driver.find_element(By.ID, "answer").send_keys(res)
    time.sleep(1)

    driver.execute_script("window.scrollBy(0, 100);")
    driver.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']").click()
    driver.find_element(By.CSS_SELECTOR, "[for='robotsRule']").click()
    driver.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(3)

finally:
    time.sleep(4)
    driver.quit()