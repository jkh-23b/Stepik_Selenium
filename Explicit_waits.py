
import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.get("https://suninjuly.github.io/explicit_wait2.html")

try:
    price = WebDriverWait(driver, 12).until(
        ec.text_to_be_present_in_element((By.ID, "price"), '$100'))


    driver.execute_script("window.scrollBy(0, 100);")
    book = driver.find_element(By.CSS_SELECTOR, "[onclick='checkPrice();'")
    book.click()
    time.sleep(2)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    num = driver.find_element(By.ID, "input_value")
    x = num.text
    res = calc(x)

    driver.find_element(By.ID, "answer").send_keys(res)
    driver.find_element(By.ID, "solve").click()

finally:
    time.sleep(5)
    driver.quit()
