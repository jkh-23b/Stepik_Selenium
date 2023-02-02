import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://suninjuly.github.io/alert_accept.html")
time.sleep(1)

try:
    driver.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(1)
    confirm = driver.switch_to.alert
    confirm.accept()


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    num = driver.find_element(By.ID, "input_value")
    x = num.text
    res = calc(x)

    driver.find_element(By.ID, "answer").send_keys(res)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

finally:
    time.sleep(4)
    driver.quit()