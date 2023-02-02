import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://suninjuly.github.io/file_input.html")
time.sleep(1)

try:
    driver.find_element(By.NAME, "firstname").send_keys("Jasur")
    driver.find_element(By.NAME, "lastname").send_keys("Khabibullaev")
    driver.find_element(By.NAME, "email").send_keys("test@gmail.com")
    time.sleep(1)


    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test_selenium.txt')
    driver.find_element(By.ID, "file").send_keys(file_path)

    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    time.sleep(1)
finally:
    time.sleep(3)
    driver.quit()