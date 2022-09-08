from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    #browser.get("http://suninjuly.github.io/get_attribute.html")
    browser.get('http://suninjuly.github.io/execute_script.html')
    #picture = browser.find_element(By.TAG_NAME, 'img')
    #x = picture.get_attribute('valuex')
    x = browser.find_element(By.ID,'input_value').text
    y = calc(int(x))
    answer_input = browser.find_element(By.TAG_NAME, 'input')
    answer_input.send_keys(y)
    checkbox1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    checkbox1.click()
    radiobutton = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script('return arguments[0].scrollIntoView(true);',radiobutton)
    radiobutton.click()
    sumbit_button = browser.find_element(By.CSS_SELECTOR, '.btn-primary')
    sumbit_button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
