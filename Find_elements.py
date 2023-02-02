import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    brow = webdriver.Chrome()
    brow.maximize_window()
    brow.get("https://suninjuly.github.io/huge_form.html")
    names = brow.find_elements(By.TAG_NAME, "input")
    for name in names:
        name.send_keys("Мой ответ")

    button = brow.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(2)

finally:
    time.sleep(10)
    brow.quit()
