from tests.helpers.support_functions import *

form_tab = 'form-header'
form_content = 'form-content'
first_name_input = 'fname'
last_name_input = 'lname'
submit_button = 'formSubmitButton'


def click_form_tab(driver_instance):
    elem = driver_instance.find_element(by=By.ID, value=form_tab)
    elem.click()


def form_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, form_content)
    return elem.is_displayed()


def submit_form_with_all_inputs_filled(driver_instance):
    wait_for_visibility_of_element_by_id(driver_instance, first_name_input)
    wait_for_visibility_of_element_by_id(driver_instance, last_name_input)
    first_name_elem = driver_instance.find_element(by=By.ID, value=first_name_input)
    last_name_elem = driver_instance.find_element(by=By.ID, value=last_name_input)
    first_name_elem.send_keys('Jan')
    last_name_elem.send_keys('Kowalski')
    driver_instance.find_element(by=By.ID, value=submit_button).click()
    alert_visibility = wait_for_visibility_of_alert(driver_instance, 3)
    return alert_visibility


def submit_form_with_only_one_input_filled(driver_instance, input_number):
    wait_for_visibility_of_element_by_id(driver_instance, first_name_input)
    wait_for_visibility_of_element_by_id(driver_instance, last_name_input)
    if input_number == 1:
        first_name_elem = driver_instance.find_element(by=By.ID, value=first_name_input)
        first_name_elem.send_keys('Hanna')
    elif input_number == 2:
        last_name_elem = driver_instance.find_element(by=By.ID, value=last_name_input)
        last_name_elem.send_keys('Nowak')
    driver_instance.find_element(by=By.ID, value=submit_button).click()
    alert_visibility = wait_for_visibility_of_alert(driver_instance, 3)
    return alert_visibility


def submit_form_with_all_inputs_empty(driver_instance):
    wait_for_visibility_of_element_by_id(driver_instance, first_name_input)
    wait_for_visibility_of_element_by_id(driver_instance, last_name_input)
    driver_instance.find_element(by=By.ID, value=submit_button).click()
    alert_visibility = wait_for_visibility_of_alert(driver_instance, 3)
    return alert_visibility
