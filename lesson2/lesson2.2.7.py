from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
import os

link = 'http://suninjuly.github.io/file_input.html'
cur_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(cur_dir, 'file.txt')
try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("Smolensk")
    upload_btn = browser.find_element(By.ID, "file")
    upload_btn.send_keys(file_path)
    sumbit_btn = browser.find_element(By.CSS_SELECTOR, '.btn-primary')
    sumbit_btn.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
