from tests.helpers.support_functions import *

error_info = 'container'


def error_info_visible(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, error_info)
    return elem.is_displayed()
