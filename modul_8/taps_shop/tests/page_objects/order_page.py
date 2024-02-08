from tests.helpers.support_functions import *
from selenium.webdriver.support.select import Select
from tests.helpers.DataGenerator import *

name_input = 'billing_first_name'
surname_input = 'billing_last_name'
country_drop_down_list = 'billing_country'
street_input = 'billing_address_1'
postcode_input = 'billing_postcode'
city_input = 'billing_city'
phone_input = 'billing_phone'
email_input = 'billing_email'
payment_part = 'payment'
place_order_button = 'place_order'

valid_postcode = '00-123'
invalid_postcode = 'abc'


def form_add_proper_name(driver_instance):
    elem = driver_instance.find_element(by=By.ID, value=name_input)
    elem.clear()
    elem.send_keys(DataGenerator.generateProperName())


def form_add_wrong_name(driver_instance):
    elem = driver_instance.find_element(by=By.ID, value=name_input)
    elem.clear()
    elem.send_keys(DataGenerator.generateWrongName(DataGenerator()))


def form_add_proper_surname(driver_instance):
    elem = driver_instance.find_element(by=By.ID, value=surname_input)
    elem.clear()
    elem.send_keys(DataGenerator.generateProperName())


def form_add_wrong_surname(driver_instance):
    elem = driver_instance.find_element(by=By.ID, value=surname_input)
    elem.clear()
    elem.send_keys(DataGenerator.generateWrongName(DataGenerator()))


def get_first_dropdown_value(driver_instance):
    elem_list = Select(driver_instance.find_element(by=By.ID, value=country_drop_down_list))
    wait_for_visibility_of_element_by_id(driver_instance, country_drop_down_list, time_to_wait=1)
    elem_list.select_by_index(1)


def form_add_proper_street(driver_instance):
    elem = driver_instance.find_element(by=By.ID, value=street_input)
    elem.clear()
    elem.send_keys(DataGenerator.generateProperName())


def form_add_wrong_street(driver_instance):
    elem = driver_instance.find_element(by=By.ID, value=street_input)
    elem.clear()
    elem.send_keys(DataGenerator.generateWrongName(DataGenerator()))


def form_add_proper_city(driver_instance):
    elem = driver_instance.find_element(by=By.ID, value=city_input)
    elem.clear()
    elem.send_keys(DataGenerator.generateProperName())


def form_add_wrong_city(driver_instance):
    elem = driver_instance.find_element(by=By.ID, value=city_input)
    elem.clear()
    elem.send_keys(DataGenerator.generateWrongName(DataGenerator()))


def form_add_proper_postcode(driver_instance):
    elem = driver_instance.find_element(by=By.ID, value=postcode_input)
    elem.clear()
    elem.send_keys(valid_postcode)


def form_add_wrong_postcode(driver_instance):
    elem = driver_instance.find_element(by=By.ID, value=postcode_input)
    elem.clear()
    elem.send_keys(invalid_postcode)


def form_add_proper_phone(driver_instance):
    elem = driver_instance.find_element(by=By.ID, value=phone_input)
    elem.clear()
    elem.send_keys(DataGenerator.generateProperPhoneNumber(DataGenerator()))


def form_add_wrong_phone(driver_instance):
    elem = driver_instance.find_element(by=By.ID, value=phone_input)
    elem.clear()
    elem.send_keys(DataGenerator.generateWrongPhoneNumber(DataGenerator()))


def form_add_proper_email(driver_instance):
    elem = driver_instance.find_element(by=By.ID, value=email_input)
    elem.clear()
    elem.send_keys(DataGenerator.generateProperEmail())


def form_add_wrong_email(driver_instance):
    elem = driver_instance.find_element(by=By.ID, value=email_input)
    elem.clear()
    elem.send_keys(DataGenerator.generateWrongEmail())


def proper_fill_all_form_areas(driver_instance):
    form_add_proper_name(driver_instance)
    form_add_proper_surname(driver_instance)
    get_first_dropdown_value(driver_instance)
    form_add_proper_street(driver_instance)
    form_add_proper_city(driver_instance)
    form_add_proper_postcode(driver_instance)
    form_add_proper_phone(driver_instance)
    form_add_proper_email(driver_instance)


def submit_order(driver_instance):
    wait_for_presence_of_text_in_element_attribute_by_id(driver_instance, payment_part, 'style', 'static',
                                                         time_to_wait=3)
    elem = driver_instance.find_element(by=By.ID, value=place_order_button)
    elem.click()
