from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

link1 = 'http://suninjuly.github.io/registration1.html'
link2 = 'http://suninjuly.github.io/registration2.html'
success_registration_words = "Congratulations! You have successfully registered!"

class TestRegistration(unittest.TestCase):
    def test_registration_page_1(self):
        try:
            browser = webdriver.Chrome()
            browser.get(link1)
            elements = browser.find_elements(By.CSS_SELECTOR, "input:required")
            for el in elements:
                el.send_keys("123")
            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual(success_registration_words, welcome_text, 'Something went wrong')
        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()

    def test_registration_page_2(self):
        try:
            browser = webdriver.Chrome()
            browser.get(link2)
            firstname = browser.find_element(By.CSS_SELECTOR, '.first')
            firstname.send_keys('123')
            secondname = browser.find_element(By.CSS_SELECTOR, 'body > div > form > div.first_block > div.form-group.second_class > input')
            secondname.send_keys('123')
            email = browser.find_element(By.CSS_SELECTOR, '.third')
            email.send_keys('123')
            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual(success_registration_words, welcome_text, 'Something went wrong')
        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()

if __name__=="__main__":
    unittest.main()