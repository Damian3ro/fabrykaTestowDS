from tests.helpers.support_functions import *

basic_auth_tab = 'basicauth-header'
basic_auth_content = 'basicauth-content'
username_input = 'ba_username'
password_input = 'ba_password'
login_button = '//*[@id="content"]/button'
invalid_login_message = 'loginFormMessage'


def click_basic_auth_tab(driver_instance):
    elem = driver_instance.find_element(by=By.ID, value=basic_auth_tab)
    elem.click()


def basic_auth_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, basic_auth_content)
    return elem.is_displayed()


def click_log_in_button(driver_instance):
    login_elem = driver_instance.find_element(by=By.XPATH, value=login_button)
    login_elem.click()


def log_in_with_correct_credentials(driver_instance):
    wait_for_visibility_of_element_by_id(driver_instance, username_input)
    wait_for_visibility_of_element_by_id(driver_instance, password_input)
    username_elem = driver_instance.find_element(by=By.ID, value=username_input)
    password_elem = driver_instance.find_element(by=By.ID, value=password_input)
    username_elem.send_keys('admin')
    password_elem.send_keys('admin')
    click_log_in_button(driver_instance)


def log_in_with_incorrect_credentials(driver_instance):
    wait_for_visibility_of_element_by_id(driver_instance, username_input)
    wait_for_visibility_of_element_by_id(driver_instance, password_input)
    username_elem = driver_instance.find_element(by=By.ID, value=username_input)
    password_elem = driver_instance.find_element(by=By.ID, value=password_input)
    username_elem.send_keys('user12345')
    password_elem.send_keys('abcdefgh123')
    click_log_in_button(driver_instance)
    wait_for_visibility_of_element_by_id(driver_instance, invalid_login_message)
    message_elem = driver_instance.find_element(by=By.ID, value=invalid_login_message)
    if message_elem.text == 'Invalid credentials':
        return True
    else:
        return False
