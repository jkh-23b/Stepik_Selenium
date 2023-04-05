import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def registration(link):
    try:
        driver = webdriver.Chrome()
        driver.get(link)
        driver.implicitly_wait(2)

        driver.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Jasur")
        driver.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Khabibullaev")
        driver.find_element(By.CSS_SELECTOR, ".third_class .third").send_keys("test@gmail.com")
        driver.find_element(By.CSS_SELECTOR, "button.btn").click()
        w_text = driver.find_element(By.TAG_NAME, "h1")
        text_ = w_text.text
        return text_
    except:
        driver.quit()

def test_link1():
    link = "http://suninjuly.github.io/registration1.html"
    assert registration(link) == "Congratulations! You have successfully registered!", "Test just Failed"

def test_link2():
    link = "http://suninjuly.github.io/registration2.html"
    assert registration(link) == "Congratulations! You have successfully registered!", "Test jurt Failed"