# Stepik_Selenium
Homeworks_for_selenium
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://suninjuly.github.io/redirect_accept.html")
time.sleep(1)

try:
    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    num = driver.find_element(By.ID, "input_value")
    x = num.text
    res = calc(x)

    driver.find_element(By.ID, "answer").send_keys(res)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(2)
finally:
    time.sleep(3)
    driver.quit()
