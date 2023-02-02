import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import random

driver = webdriver.Chrome()
driver.maximize_window()


try:
    driver.get("https://suninjuly.github.io/find_xpath_form")
    space = driver.find_elements(By.TAG_NAME, "input")
    list = ['Khabibullaev', 'Jasur', 'London', 'United Kingdom']
    for s in space:
        s.send_keys(random.choice(list))

    subm = driver.find_element(By.XPATH, "//button[@type='submit']")
    subm.click()

finally:
    time.sleep(5)
    driver.quit()