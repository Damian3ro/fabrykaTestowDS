from tests.helpers.support_functions import *
from tests.helpers.DataGenerator import *

username = 'username'
password = 'password'
login_button = '//button[contains(@class,"woocommerce-form-login__submit") and @type="submit" and @name="login"]'
forgotten_password_button = '//p[contains(@class,"woocommerce-LostPassword lost_password")]/a'
email_register_input = 'reg_email'
register_button = ('//button[contains(@class,"woocommerce-form-register__submit") and @type="submit" '
                        'and @name="register"]')
policy_link = '//a[contains(@class,"woocommerce-privacy-policy-link")]'
error_info = '//div[contains(@class,"wc-block-components-notice-banner__content")]'
bottom_message_info_reject_button = '//a[contains(@class,"woocommerce-store-notice__dismiss-link")]'

random_credential = 'test'

proper_email1 = 'cotaga1249@maillei.net'
proper_password1 = 'VRrMhK8MqFyd'

proper_email2 = 'wowen49501@maillei.net'
proper_password2 = 'lxsg#GAqH$Ke'

proper_email3 = 'bomineg967@onmail3.com'
proper_password3 = 'zedvu@##)CZy'

proper_email4 = 'wacog70401@tinkmail.net'
proper_password4 = 'Lk*3Q9&am3zL'

proper_email5 = 'calose2528@maillei.net'
proper_password5 = 'lkSb&SAJwLWo'

generated_proper_email = DataGenerator.generateProperEmail()

def get_username(option_number):
    correct_email = ''
    if option_number == 1:
        correct_email = proper_email1
    elif option_number == 2:
        correct_email = proper_email2
    elif option_number == 3:
        correct_email = proper_email3
    elif option_number == 4:
        correct_email = proper_email4
    elif option_number == 5:
        correct_email = proper_email5
    user_name = correct_email.split('@')[0]
    return user_name


def form_add_proper_username(driver_instance, correct_email):
    elem = driver_instance.find_element(by=By.ID, value=username)
    elem.clear()
    elem.send_keys(correct_email)


def form_add_wrong_username(driver_instance, credential=None):
    elem = driver_instance.find_element(by=By.ID, value=username)
    elem.clear()
    if credential is None:
        elem.send_keys(DataGenerator.generateWrongEmail())
    else:
        elem.send_keys(credential)


def form_add_proper_password(driver_instance, correct_password):
    elem = driver_instance.find_element(by=By.ID, value=password)
    elem.clear()
    elem.send_keys(correct_password)


def form_add_wrong_password(driver_instance, credential=None):
    elem = driver_instance.find_element(by=By.ID, value=password)
    elem.clear()
    if credential is None:
        elem.send_keys(DataGenerator.generateWrongName(DataGenerator()))
    else:
        elem.send_keys(credential)


def form_add_proper_email(driver_instance):
    elem = driver_instance.find_element(by=By.ID, value=email_register_input)
    elem.clear()
    elem.send_keys(generated_proper_email)


def form_add_wrong_email(driver_instance):
    elem = driver_instance.find_element(by=By.ID, value=email_register_input)
    elem.clear()
    elem.send_keys(DataGenerator.generateWrongEmail())


def click_on_log_in_button(driver_instance):
    elem = driver_instance.find_element(by=By.XPATH, value=login_button)
    elem.click()


def open_privacy_policy(driver_instance):
    close_bottom_message_info_panel(driver_instance)
    elem = driver_instance.find_element(by=By.XPATH, value=policy_link)
    elem.click()


def click_on_register_button(driver_instance):
    elem = driver_instance.find_element(by=By.XPATH, value=register_button)
    elem.click()


def close_bottom_message_info_panel(driver_instance):
    elem = driver_instance.find_element(by=By.XPATH, value=bottom_message_info_reject_button)
    elem.click()


def correct_login(driver_instance, option_number):
    correct_email = ''
    correct_password = ''
    if option_number == 1:
        correct_email = proper_email1
        correct_password = proper_email1
    elif option_number == 2:
        correct_email = proper_email2
        correct_password = proper_email2
    elif option_number == 3:
        correct_email = proper_email3
        correct_password = proper_email3
    elif option_number == 4:
        correct_email = proper_email4
        correct_password = proper_email4
    elif option_number == 5:
        correct_email = proper_email5
        correct_password = proper_email5
    close_bottom_message_info_panel(driver_instance)
    form_add_proper_username(driver_instance, correct_email)
    form_add_proper_password(driver_instance, correct_password)
    click_on_log_in_button(driver_instance)


def check_incorrect_log_in_or_register(driver_instance, message_to_check, printed_message):
    try:
        wait_for_visibility_of_element_by_xpath(driver_instance, error_info)
        elem = driver_instance.find_element(by=By.XPATH, value=error_info)
        if message_to_check in elem.text:
            print(printed_message)
        return elem.is_displayed()
    except NoSuchElementException:
        return False


def incorrect_login_different_logins(driver_instance):
    close_bottom_message_info_panel(driver_instance)
    form_add_wrong_username(driver_instance)
    form_add_wrong_password(driver_instance, credential=random_credential)
    click_on_log_in_button(driver_instance)
    return check_incorrect_log_in_or_register(driver_instance, 'nieprawidłowa nazwa użytkownika lub hasło.',
                                       'ERROR Wrong user/password')


def incorrect_login_the_same_login_too_many_attempts(driver_instance):
    close_bottom_message_info_panel(driver_instance)
    for i in range(3):
        wait_for_visibility_of_element_by_id(driver_instance, username)
        wait_for_visibility_of_element_by_id(driver_instance, password)
        wait_for_visibility_of_element_by_xpath(driver_instance, login_button)
        form_add_wrong_username(driver_instance, credential=random_credential)
        form_add_wrong_password(driver_instance, credential=random_credential)
        click_on_log_in_button(driver_instance)
    return check_incorrect_log_in_or_register(driver_instance, 'zbyt wiele nieudanych prób logowania',
                                       'ERROR Too many login attempts')


def incorrect_login_only_empty_password_input(driver_instance):
    close_bottom_message_info_panel(driver_instance)
    elem = driver_instance.find_element(by=By.ID, value=username)
    elem.send_keys(DataGenerator.generateWrongEmail())
    click_on_log_in_button(driver_instance)
    return check_incorrect_log_in_or_register(driver_instance, 'pole hasła jest puste',
                                       'ERROR Empty password input')


def incorrect_login_only_empty_login_input(driver_instance):
    close_bottom_message_info_panel(driver_instance)
    elem = driver_instance.find_element(by=By.ID, value=password)
    elem.send_keys(random_credential)
    click_on_log_in_button(driver_instance)
    return check_incorrect_log_in_or_register(driver_instance, 'Nazwa użytkownika jest wymagana.',
                                       'ERROR Empty login input')


def incorrect_login_empty_login_and_password_inputs(driver_instance):
    close_bottom_message_info_panel(driver_instance)
    click_on_log_in_button(driver_instance)
    return check_incorrect_log_in_or_register(driver_instance, 'Nazwa użytkownika jest wymagana.',
                                       'ERROR Empty login and password inputs')


def move_to_forgotten_password_page(driver_instance):
    close_bottom_message_info_panel(driver_instance)
    elem = driver_instance.find_element(by=By.XPATH, value=forgotten_password_button)
    elem.click()


def correct_register(driver_instance):
    close_bottom_message_info_panel(driver_instance)
    form_add_proper_email(driver_instance)
    click_on_register_button(driver_instance)


def incorrect_register_wrong_email(driver_instance):
    close_bottom_message_info_panel(driver_instance)
    form_add_wrong_email(driver_instance)
    click_on_register_button(driver_instance)
    return check_incorrect_log_in_or_register(driver_instance, 'Proszę podać poprawny adres e-mail.',
                                       'ERROR Empty email input')


def incorrect_register_empty_email_input(driver_instance):
    close_bottom_message_info_panel(driver_instance)
    click_on_register_button(driver_instance)
    return check_incorrect_log_in_or_register(driver_instance, 'Proszę podać poprawny adres e-mail.',
                                       'ERROR Empty email input')
