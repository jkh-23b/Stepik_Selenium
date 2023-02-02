import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://suninjuly.github.io/registration2.html")

try:
    first_name = driver.find_element(By.CSS_SELECTOR, "[type='text'].first")
    first_name.send_keys("Jasur")
    time.sleep(1)

    last_name = driver.find_element(By.CSS_SELECTOR, ".first_block input.second")
    last_name.send_keys("Khabibullaev")
    time.sleep(1)

    email = driver.find_element(By.CSS_SELECTOR, "[type='text'].third")
    email.send_keys("test@gmail.com")
    time.sleep(1)

    phone = driver.find_element(By.CSS_SELECTOR, ".second_block input.first")
    phone.send_keys("+998991234567")
    time.sleep(1)

    address = driver.find_element(By.CSS_SELECTOR, ".second_block input.second")
    address.send_keys("Tashkent")
    time.sleep(1)

    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(2)

    welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(2)
    driver.quit()