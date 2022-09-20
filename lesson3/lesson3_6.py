import pytest
import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

links = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
]


@pytest.mark.parametrize('link',links)
def test_correct_feedback(browser,link):
    browser.get(link)
    browser.implicitly_wait(8)
    input_area = browser.find_element(By.TAG_NAME, 'textarea')
    answer = math.log(int(time.time()))
    input_area.send_keys(str(answer))
    submit_button = browser.find_element(By.CSS_SELECTOR,'.submit-submission')
    submit_button.click()
    feedback_text_area = WebDriverWait(browser,5).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'.smart-hints')))
    feedback_text = feedback_text_area.text
    assert feedback_text == 'Correct!', 'Something went wrong! Check your answer!'

