from tests.helpers.support_functions import *
from selenium.webdriver.support.select import Select

dropdown_list_tab = 'dropdownlist-header'
dropdown_list_content = 'dropdownlist-content'
dropdown_list = 'dropdown'
default_option = '//*[@id="dropdown"]/option[1]'
option1 = '//*[@id="dropdown"]/option[2]'
option2 = '//*[@id="dropdown"]/option[3]'


def click_dropdown_tab(driver_instance):
    elem = driver_instance.find_element(by=By.ID, value=dropdown_list_tab)
    elem.click()


def dropdown_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, dropdown_list_content)
    return elem.is_displayed()


def get_dropdown_list_value(driver_instance, option_number):
    elem_list = Select(driver_instance.find_element(by=By.ID, value=dropdown_list))
    wait_for_visibility_of_element_by_id(driver_instance, dropdown_list, time_to_wait=1)
    option_selected = ''
    if option_number == 0:
        option_selected = default_option
    elif option_number == 1:
        option_selected = option1
    elif option_number == 2:
        option_selected = option2
    elem_list.select_by_index(option_number)
    elem_selected = driver_instance.find_element(by=By.XPATH, value=option_selected)
    if elem_selected.get_property('selected'):
        return True
    else:
        return False

