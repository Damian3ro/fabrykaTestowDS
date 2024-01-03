from tests.helpers.support_functions import *
from datetime import date

date_picker_tab = 'datepicker-header'
date_picker_content = 'datepicker-content'
input = 'start'


def click_date_picker_tab(driver_instance):
    elem = driver_instance.find_element(by=By.ID, value=date_picker_tab)
    elem.click()


def date_picker_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, date_picker_content)
    return elem.is_displayed()


def send_correct_date_to_input(driver_instance):
    wait_for_visibility_of_element_by_xpath(driver_instance, input, time_to_wait=1)
    elem = driver_instance.find_element(by=By.ID, value=input)
    elem.send_keys('07.15.2020')
    value = date(2020, 7, 15)
    min_date = date.fromisoformat(elem.get_attribute('min'))
    max_date = date.fromisoformat(elem.get_attribute('max'))
    if min_date <= value <= max_date:
        return True
    else:
        return False


def send_incorrect_date_to_input(driver_instance):
    wait_for_visibility_of_element_by_xpath(driver_instance, input, time_to_wait=1)
    elem = driver_instance.find_element(by=By.ID, value=input)
    elem.send_keys('01.01.2050')
    value = date(2050, 1, 1)
    min_date = date.fromisoformat(elem.get_attribute('min'))
    max_date = date.fromisoformat(elem.get_attribute('max'))
    if min_date <= value <= max_date:
        return False
    else:
        return True
