from tests.helpers.support_functions import *
from tests.helpers.DataGenerator import *

forgotten_password_header = '//*[@id="post-9"]/header/h1'
user_login_input = 'user_login'
reset_password_button = ('//button[contains(@class,"woocommerce-Button button") and @type="submit" '
                         'and @value="Zresetuj hasło"]')
sent_email_info = '//div[contains(@class,"wc-block-components-notice-banner__content")]'

def forgotten_password_header_visible(driver_instance):
    try:
        wait_for_visibility_of_element_by_xpath(driver_instance, forgotten_password_header)
        elem_text_visibility = 'Zapomniane hasło' in driver_instance.find_element(
            by=By.XPATH, value=forgotten_password_header).text
        return elem_text_visibility
    except StaleElementReferenceException:
        return False


def reset_password(driver_instance):
    elem = driver_instance.find_element(by=By.ID, value=user_login_input)
    elem.send_keys(DataGenerator.generateProperEmail())
    elem1 = driver_instance.find_element(by=By.XPATH, value=reset_password_button)
    elem1.click()
    wait_for_visibility_of_element_by_xpath(driver_instance, sent_email_info)
    elem2 = driver_instance.find_element(by=By.XPATH, value=sent_email_info)
    if 'Wysłano e-mail do zresetowania hasła.' in elem2.text:
        return True
    else:
        return False
