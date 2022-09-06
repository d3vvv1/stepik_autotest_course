from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(" http://SunInJuly.github.io/execute_script.html")
    num1 = browser.find_element(By.ID, 'num1').text
    num2 = browser.find_element(By.ID, 'num2').text
    x = int(num1) + int(num2)
    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_visible_text(str(x))
    sumbit_button = browser.find_element(By.CSS_SELECTOR, '.btn-default')
    sumbit_button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
