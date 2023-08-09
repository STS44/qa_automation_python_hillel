import os

import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.implicitly_wait(10)
    chrome_driver.quit()


@pytest.fixture
def base_link(driver):
    driver.get("http://the-internet.herokuapp.com/?ref=hackernoon.com")
    yield driver
