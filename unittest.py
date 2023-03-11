import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)

class test_class_name(unittest.TestCase):
    def test_1(self):
        driver.get("https://suninjuly.github.io/registration1.html")

        driver.find_element(By.CSS_SELECTOR, ".first_block input.first").send_keys("Jasur")
        driver.find_element(By.CSS_SELECTOR, ".first_block input.second").send_keys("Khabibullaev")
        driver.find_element(By.CSS_SELECTOR, "[type='text'].third").send_keys("test@gmail.com")
        driver.find_element(By.CSS_SELECTOR, ".second_block input.first").send_keys("+998991234567")
        driver.find_element(By.CSS_SELECTOR, ".second_block input.second").send_keys("Uzbekistan")
        driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        time.sleep(2)

        self.assertEqual()


