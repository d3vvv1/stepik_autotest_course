import pytest
from selenium.webdriver.common.by import By

#@pytest.mark.xfail(strict=True)
@pytest.mark.skip
def test_succeed():
    assert True


#@pytest.mark.xfail()
@pytest.mark.skip
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False

link = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.skip
def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#magic_link")