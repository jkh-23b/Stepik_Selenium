import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()

driver.get("https://suninjuly.github.io/selects2.html")
time.sleep(1)

def sums(x, y):
    return str(x + y)
num1 = driver.find_element(By.ID, "num1")
a = num1.text
x = int(a)
num2 = driver.find_element(By.ID, "num2")
b = num2.text
y = int(b)
res = sums(x, y)

try:
    element = Select(driver.find_element(By.XPATH, "//select[@id='dropdown']"))
    element.select_by_visible_text(res)

    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(2)




finally:
    time.sleep(4)
    driver.quit()

