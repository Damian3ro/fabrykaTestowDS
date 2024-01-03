from tests.helpers.support_functions import *

home_page_tab = 'test-header'
home_page_content = 'test-content'


def home_page_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, home_page_content)
    return elem.is_displayed()
