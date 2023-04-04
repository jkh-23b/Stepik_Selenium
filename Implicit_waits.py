from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://suninjuly.github.io/wait1.html")

button = driver.find_element(By.ID, "verify")
button.click()

message = driver.find_element(By.ID, "verify_message")
print(message)
assert "successful" in message.text
