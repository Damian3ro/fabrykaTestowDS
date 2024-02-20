from tests.helpers.support_functions import *

error_info = '//*[@id="post-1565"]/div/p[1]'

def error_info_visible(driver_instance):
    window_after = driver_instance.window_handles[1]
    driver_instance.switch_to.window(window_after)
    try:
        wait_for_visibility_of_element_by_xpath(driver_instance, error_info)
        elem_text_visibility = 'Error 404' in driver_instance.find_element(
            by=By.XPATH, value=error_info).text
        return elem_text_visibility
    except StaleElementReferenceException:
        return False
