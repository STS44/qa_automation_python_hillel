from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.steps import (
    open_alert,
    verify_alert_present,
    change_text,
    verify_text_changed,
    display_button,
    verify_button_displayed,
    enable_button,
    verify_button_enabled,
    check_checkbox,
    verify_checkbox_checked,
)


def test_navigate_to_url(driver):
    driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")
    assert "ExplicitlyWait" in driver.title


def test_wait_alert(chercher_tech):
    wait = WebDriverWait(chercher_tech, 10)
    wait.until(EC.element_to_be_clickable((By.ID, "alert")))
    open_alert(chercher_tech)
    wait.until(EC.alert_is_present())
    verify_alert_present(chercher_tech)


def test_wait_change_text(chercher_tech):
    wait = WebDriverWait(chercher_tech, 15)
    wait.until(EC.element_to_be_clickable((By.ID, "populate-text")))
    change_text(chercher_tech)
    wait.until(EC.text_to_be_present_in_element((By.ID, "h2"), "Selenium Webdriver"))
    verify_text_changed(chercher_tech)


def test_wait_display_button(chercher_tech):
    wait = WebDriverWait(chercher_tech, 15)
    wait.until(EC.element_to_be_clickable((By.ID, "display-other-button")))
    display_button(chercher_tech)
    wait.until(EC.visibility_of_element_located((By.ID, "hidden")))
    verify_button_displayed(chercher_tech)


def test_wait_enable_button(chercher_tech):
    wait = WebDriverWait(chercher_tech, 15)
    wait.until(EC.element_to_be_clickable((By.ID, "enable-button")))
    enable_button(chercher_tech)
    wait.until(EC.element_to_be_clickable((By.ID, "disable")))
    verify_button_enabled(chercher_tech)


def test_wait_check_checkbox(chercher_tech):
    wait = WebDriverWait(chercher_tech, 15)
    wait.until(EC.element_to_be_clickable((By.ID, "checkbox")))
    check_checkbox(chercher_tech)
    wait.until(lambda ch: ch.find_element(By.ID, "ch").is_selected())
    verify_checkbox_checked(chercher_tech)
