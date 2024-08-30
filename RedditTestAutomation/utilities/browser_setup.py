from selenium import webdriver
import pytest
from pages.home_page import HomePage

@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # Ensure chromedriver is installed and in PATH
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
