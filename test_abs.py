import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://suninjuly.github.io/math.html")
time.sleep(2)

element = driver.find_element(By.ID, "input_value")
x = element.text

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)

driver.find_element(By.ID, "answer").send_keys(y)
checked = driver.find_element(By.ID, "peopleRule")
p_checked = checked.get_attribute("checked")
print ("value of people radio: ", p_checked)

