import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://suninjuly.github.io/file_input.html")
time.sleep(1)

driver.find_element(By.XPATH, "//input[@name='firstname']").send_keys("Jasur")
driver.find_element(By.NAME, "lastname").send_keys("Khabibullaev")
driver.find_element(By.NAME, "email").send_keys("test@gmail.com")
time.sleep(1)

current_dir = os.path.abspath(os.path.dirname(__file__))
print(current_dir)
file_path = os.path.join(current_dir, "Execute_script_scroll.py")

driver.find_element(By.XPATH, "//input[@name='file']").send_keys(file_path)
driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
time.sleep(1)

alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)
alert.accept()

time.sleep(2)

driver.quit()
