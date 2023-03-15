import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
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
        time.sleep(1)

        text_welc = driver.find_element(By.TAG_NAME, "h1").text
        needed_text = "Congratulations! You have successfully registered!"
        self.assertEqual(text_welc, needed_text, 'No text')


    def test_2(self):
        driver.get("https://suninjuly.github.io/registration2.html")
        time.sleep(1)

        driver.find_element(By.CSS_SELECTOR, ".first_block input.first").send_keys("Jasur")
        driver.find_element(By.CSS_SELECTOR, ".first_block input.third").send_keys("testt@gmail.com")
        driver.find_element(By.CSS_SELECTOR, ".second_block input.first").send_keys("+998991112233")
        driver.find_element(By.CSS_SELECTOR, ".second_block input.second").send_keys("Uzbekistan")
        driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        time.sleep(1)

        text_welc2 = driver.find_element(By.TAG_NAME, "h1").text
        needed_text2 = "Congratulations! You have successfully registered!"
        self.assertEqual(text_welc2, needed_text2, 'No text')

if __name__ == "__main__":
    unittest.main()
    print("All passed")


