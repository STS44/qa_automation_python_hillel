from selenium.webdriver.common.by import By


def open_alert(chercher_tech):
    chercher_tech.find_element(By.ID, "alert").click()


def verify_alert_present(chercher_tech):
    alert = chercher_tech.switch_to.alert
    assert "I got opened after 5 secods" in alert.text


def change_text(chercher_tech):
    chercher_tech.find_element(By.ID, "populate-text").click()


def verify_text_changed(chercher_tech):
    selenium_web_driver_elem = chercher_tech.find_element(By.ID, "h2")
    assert "Selenium Webdriver" in selenium_web_driver_elem.text


def display_button(chercher_tech):
    chercher_tech.find_element(By.ID, "display-other-button").click()


def verify_button_displayed(chercher_tech):
    btn = chercher_tech.find_element(By.ID, "hidden")
    assert btn.is_displayed()


def enable_button(chercher_tech):
    chercher_tech.find_element(By.ID, "enable-button").click()


def verify_button_enabled(chercher_tech):
    btn = chercher_tech.find_element(By.ID, "disable")
    assert btn.is_enabled()


def check_checkbox(chercher_tech):
    chercher_tech.find_element(By.ID, "checkbox").click()


def verify_checkbox_checked(chercher_tech):
    checkbox = chercher_tech.find_element(By.ID, "ch")
    assert checkbox.is_selected()
