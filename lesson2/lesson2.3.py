from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
import os

link = 'http://suninjuly.github.io/alert_accept.html'
link2 = 'http://suninjuly.github.io/redirect_accept.html'
link3 = ' http://suninjuly.github.io/cats.html'
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

'''
try:
    browser = webdriver.Chrome()
    browser.get(link)
    btn1 = browser.find_element(By.CSS_SELECTOR, '.btn-primary').click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = browser.find_element(By.ID, 'input_value').text
    input_form = browser.find_element(By.TAG_NAME, 'input')
    input_form.send_keys(calc(int(x)))
    submit_btn = browser.find_element(By.CSS_SELECTOR, '.btn-primary').click()
'''
try:
    browser = webdriver.Chrome()
    browser.get(link2)
    time.sleep(2)
    btn1 = browser.find_element(By.TAG_NAME, 'button').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element(By.ID, 'input_value').text
    input_form = browser.find_element(By.TAG_NAME, 'input')
    input_form.send_keys(calc(int(x)))
    submit_btn = browser.find_element(By.CSS_SELECTOR, '.btn-primary').click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
