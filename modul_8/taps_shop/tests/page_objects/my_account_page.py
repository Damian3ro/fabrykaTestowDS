from tests.helpers.support_functions import *

my_account_header = '//*[@id="post-9"]/header/h1'
my_account_welcome_info = '//div[contains(@class,"woocommerce-MyAccount-content")]/p[1]'

def my_account_welcome_info_visible(driver_instance, username):
    try:
        wait_for_visibility_of_element_by_xpath(driver_instance, my_account_welcome_info)
        elem_text_visibility = f'Witaj {username}' in driver_instance.find_element(
            by=By.XPATH, value=my_account_welcome_info).text
        return elem_text_visibility
    except StaleElementReferenceException:
        return False
