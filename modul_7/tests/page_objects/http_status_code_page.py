from tests.helpers.support_functions import *

status_info = '/html/body/pre'


def check_status_code(driver_instance, code_number):
    wait_for_visibility_of_element_by_xpath(driver_instance, status_info)
    code_value = ''
    if code_number == 200:
        code_value = f'{code_number} OK'
    elif code_number == 305:
        code_value = f'{code_number} Use Proxy'
    elif code_number == 404:
        code_value = f'{code_number} Not Found'
    elif code_number == 500:
        code_value = f'{code_number} Internal Server Error'

    elem = driver_instance.find_element(by=By.XPATH, value=status_info)
    if elem.text == code_value:
        return True
    else:
        return False
