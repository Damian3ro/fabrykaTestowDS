from tests.helpers.support_functions import *

status_codes_tab = 'statuscodes-header'
status_codes_content = 'statuscodes-content'
code_200 = '200siteAnchor'
code_305 = '305siteAnchor'
code_404 = '404siteAnchor'
code_500 = '500siteAnchor'


def click_status_codes_tab(driver_instance):
    elem = driver_instance.find_element(by=By.ID, value=status_codes_tab)
    elem.click()


def status_codes_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, status_codes_content)
    return elem.is_displayed()


def click_on_code_link(driver_instance, code_number):
    link = ''
    code_value = ''
    if code_number == 200:
        link = code_200
        code_value = f'{code_number} OK'
    elif code_number == 305:
        link = code_305
        code_value = f'{code_number} Use Proxy'
    elif code_number == 404:
        link = code_404
        code_value = f'{code_number} Not Found'
    elif code_number == 500:
        link = code_500
        code_value = f'{code_number} Internal Server Error'
    wait_for_visibility_of_element_by_id(driver_instance, link)
    elem = driver_instance.find_element(by=By.ID, value=link)
    elem.click()
