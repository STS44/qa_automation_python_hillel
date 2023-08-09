import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_navigate_to_base_link(driver):
    driver.get("http://the-internet.herokuapp.com/?ref=hackernoon.com")
    assert "The Internet" in driver.title


def test_checkboxes(base_link):
    base_link.find_element(By.LINK_TEXT, "Checkboxes").click()
    elems = WebDriverWait(base_link, 10).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "input[type=checkbox]"))
    )
    for elem in elems:
        elem.click()

    assert elems[0].is_selected()
    assert not elems[1].is_selected()


def test_context_menu(base_link):
    wait = WebDriverWait(base_link, 10)
    base_link.find_element(By.LINK_TEXT, "Context Menu").click()
    box = wait.until(EC.element_to_be_clickable((By.ID, "hot-spot")))

    action = ActionChains(base_link)
    action.context_click(box).perform()

    try:
        wait.until(EC.alert_is_present())
        alert = base_link.switch_to.alert
        alert.accept()
        print("alert accepted")
    except:
        print("no alert")


def test_dropdown(base_link):
    base_link.find_element(By.LINK_TEXT, "Dropdown").click()

    dropdown = WebDriverWait(base_link, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".example #dropdown"))
    )
    select = Select(dropdown)
    select.select_by_visible_text("Option 2")

    selected_option = base_link.find_element(
        By.CSS_SELECTOR, "#dropdown option:nth-child(3)"
    )

    assert selected_option.is_selected()


def test_entry_ad(base_link):
    wait = WebDriverWait(base_link, 10)

    base_link.find_element(By.LINK_TEXT, "Entry Ad").click()

    modal_close = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div.modal .modal-footer p"))
    )
    modal_close.click()

    restart_ad = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a#restart-ad"))
    )
    restart_ad.click()

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.modal")))
    modal = base_link.find_element(By.CSS_SELECTOR, "div#modal")

    assert modal.is_displayed()


def test_form_authentication(base_link):
    wait = WebDriverWait(base_link, 10)
    base_link.find_element(By.LINK_TEXT, "Form Authentication").click()

    username_field = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
    username_field.clear()  # clear username field to be sure that there is no default text in it
    username_field.send_keys("tomsmith")

    password_field = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
    password_field.clear()  # clear password field to be sure that there is no default text in it
    password_field.send_keys("SuperSecretPassword!")

    login_btn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#login button"))
    )
    login_btn.click()
    result = base_link.find_element(By.ID, "flash")

    assert "You logged into a secure area!" in result.text


def test_frames(base_link):
    wait = WebDriverWait(base_link, 10)
    base_link.find_element(By.LINK_TEXT, "Frames").click()
    iframe_link = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".example ul li:nth-child(2) a"))
    )
    iframe_link.click()

    # cleaning the frame from the default text by creating New document from File in menubar
    file_btn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".tox-menubar button:first-child"))
    )
    file_btn.click()

    new_document = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".tox-collection__group div:only-child")
        )
    )
    new_document.click()

    wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "mce_0_ifr")))
    base_link.find_element(By.ID, "tinymce").send_keys("Te$t1ng !Fr@me")
    result = base_link.find_element(By.CSS_SELECTOR, "#tinymce p")

    assert "Te$t1ng !Fr@me" in result.text


def test_horizontal_slider(base_link):
    wait = WebDriverWait(base_link, 10)
    base_link.find_element(By.LINK_TEXT, "Horizontal Slider").click()
    slider = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".sliderContainer input"))
    )

    action = ActionChains(base_link)
    action.drag_and_drop_by_offset(slider, 50, 0).perform()
    slider.send_keys(Keys.ARROW_LEFT)
    slider.send_keys(Keys.ARROW_LEFT)
    slider.send_keys(Keys.ARROW_LEFT)
    value = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "span#range"))
    )

    assert "3" in value.text


def test_hovers(base_link):
    wait = WebDriverWait(base_link, 10)
    base_link.find_element(By.LINK_TEXT, "Hovers").click()
    image = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".example div:nth-child(4) img")
        )
    )

    action = ActionChains(base_link)
    action.move_to_element(image).perform()

    view_profile_link = wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "View profile"))
    )
    view_profile_link.click()

    result = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

    assert "Not Found" in result.text


def test_inputs(base_link):
    wait = WebDriverWait(base_link, 10)
    base_link.find_element(By.LINK_TEXT, "Inputs").click()

    number_field = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".example input"))
    )
    number_field.clear()  # clear input field to be sure that there is no default text in it
    number_field.send_keys("-123.45")
    result = number_field.get_attribute("value")

    assert "-123.45" in result


def test_key_presses(base_link):
    wait = WebDriverWait(base_link, 10)
    base_link.find_element(By.LINK_TEXT, "Key Presses").click()

    key_field = wait.until(EC.visibility_of_element_located((By.ID, "target")))
    key_field.send_keys(Keys.ESCAPE)

    result = wait.until(EC.visibility_of_element_located((By.ID, "result")))

    assert "ESCAPE" in result.text
