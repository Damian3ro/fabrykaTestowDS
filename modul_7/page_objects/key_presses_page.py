from tests.helpers.support_functions import *
from selenium.webdriver.common.keys import Keys

key_presses_tab = 'keypresses-header'
key_presses_content = 'keypresses-content'
input = 'target'
message_below_input = 'keyPressResult'


def click_key_presses_tab(driver_instance):
    elem = driver_instance.find_element(by=By.ID, value=key_presses_tab)
    elem.click()


def key_presses_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, key_presses_content)
    return elem.is_displayed()


def press_letter_key_in_input(driver_instance):
    wait_for_visibility_of_element_by_id(driver_instance, input)
    key = 'a'
    press_key_on_element_by_id(driver_instance, input, key)
    release_key_pressed_on_element_by_id(driver_instance, input, key)
    wait_for_visibility_of_element_by_id(driver_instance, message_below_input)
    message_elem = driver_instance.find_element(by=By.ID, value=message_below_input)
    if message_elem.text == f'You entered: {key.capitalize()}':
        return True
    else:
        return False


def press_function_key_in_input(driver_instance):
    wait_for_visibility_of_element_by_id(driver_instance, input)
    key = Keys.ENTER
    value = 'ENTER'
    press_key_on_element_by_id(driver_instance, input, key)
    release_key_pressed_on_element_by_id(driver_instance, input, key)
    wait_for_visibility_of_element_by_id(driver_instance, message_below_input)
    message_elem = driver_instance.find_element(by=By.ID, value=message_below_input)
    if message_elem.text == f'You entered: {value}':
        return True
    else:
        return False
