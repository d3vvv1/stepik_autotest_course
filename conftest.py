import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store',default='chrome', help='Choose browser: chrome or firefox')

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser_name')
    browser = None
    if browser_name == 'chrome':
        print("\nstart Chrome browser for test...")
        browser = webdriver.Chrome()
    elif browser_name == 'firefox':
        print('\nstart Firefox browser for test...')
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_nem should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
