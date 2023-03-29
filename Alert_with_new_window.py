import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://suninjuly.github.io/redirect_accept.html")
time.sleep(1)

driver.find_element(By.XPATH, "//button[@type='submit']").click()

driver.switch_to.window(driver.window_handles[1])
time.sleep(1)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

num = driver.find_element(By.ID, "input_value")
x = num.text
res = calc(x)

driver.find_element(By.ID, "answer").send_keys(res)
driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
time.sleep(2)

conf_alerts = driver.switch_to.alert
conf_alerts.accept()
time.sleep(2)

driver.quit()
