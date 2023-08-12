import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture()
def chercher_tech(driver):
    driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")
    yield driver
