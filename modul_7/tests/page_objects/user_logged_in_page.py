from tests.helpers.support_functions import *

logged_in_info = 'page'
return_button = 'retrun button'


def user_logged_in_page_displayed(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, logged_in_info)
    return elem.is_displayed()


def return_to_home_page(driver_instance):
    wait_for_visibility_of_element_by_id(driver_instance, return_button)
    elem = driver_instance.find_element(by=By.ID, value=return_button)
    elem.click()
