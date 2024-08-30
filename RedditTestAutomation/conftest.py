import pytest
from selenium import webdriver
from pages.home_page import HomePage

@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # to retrive chrome driver for browser.
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def user_on_homepage(browser):
    browser.get('https://www.reddit.com/')
    return HomePage(browser)
