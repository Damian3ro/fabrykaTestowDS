from tests.helpers.support_functions import *
from selenium.webdriver.support.select import Select

beanie_product = '//li[contains(@class,"post-46")]'
belt_product = '//li[contains(@class,"post-47")]'
cap_product = '//li[contains(@class,"post-48")]'
hoodie_product = '//li[contains(@class,"post-43")]'
hoodie_with_logo_product = '//li[contains(@class,"post-44")]'
hoodie_with_zipper_product = '//li[contains(@class,"post-51")]'
long_sleeve_tee_product = '//li[contains(@class,"post-52")]'
polo_product = '//li[contains(@class,"post-53")]'
sunglasses_product = '//li[contains(@class,"post-49")]'
t_shirt_product = '//li[contains(@class,"post-45")]'
v_neck_t_shirt_product = '//li[contains(@class,"post-42")]'

search_products_input = 'woocommerce-product-search-field-0'
order_drop_down_list = '//form[contains(@class,"woocommerce-ordering")]/select[@name="orderby" and @class="orderby"]'
results_found_info = '//p[contains(@class,"woocommerce-result-count")]'
no_products_found_info = '//div[contains(@class,"wc-block-components-notice-banner__content")]'
products_table = '//ul[contains(@class,"products columns-4")]'
next_page_button = '//a[contains(@class,"next page-numbers")]'
previous_page_button = '//a[contains(@class,"prev page-numbers")]'

def get_xpath_for_product_name_on_list(product_number):
    elem_xpath = products_table + '/li[' + str(product_number) + ']/a/h2'
    return elem_xpath


def get_xpath_for_product_price_on_list(product_number):
    elem_xpath = products_table + '/li[' + str(product_number) + ']/a/span[contains(@class,"price")]/bdi'
    return elem_xpath


def search_products(driver_instance, product_name):
    elem = driver_instance.find_element(by=By.ID, value=search_products_input)
    elem.send_keys(product_name)
    elem.submit()


def select_ordering_option(driver_instance, option_number):
    elem_list = Select(driver_instance.find_element(by=By.XPATH, value=order_drop_down_list))
    wait_for_visibility_of_element_by_xpath(driver_instance, order_drop_down_list, time_to_wait=1)
    elem_list.select_by_index(option_number)


def get_products_count_found_on_page(driver_instance):
    elem = driver_instance.find_element(by=By.XPATH, value=results_found_info)
    return int(elem.text[-1])


def check_product_on_list(driver_instance, check_by='name', list_item_number=1, last_product=None):
    if list_item_number > 0:
        product_table_length = str(len(driver_instance.find_elements(by=By.XPATH, value=products_table + '/li')))
        if last_product:
            list_item_number = product_table_length
        if check_by == 'price':
            elem_xpath = get_xpath_for_product_price_on_list(list_item_number)
        else:
            elem_xpath = get_xpath_for_product_name_on_list(list_item_number)
        wait_for_visibility_of_element_by_xpath(driver_instance, elem_xpath)
        elem = driver_instance.find_element(by=By.XPATH, value=elem_xpath)
        return elem.text
    else:
        raise ValueError('Incorrect entered list number of item.')


def check_incorrect_product_searching(driver_instance):
    try:
        wait_for_visibility_of_element_by_xpath(driver_instance, no_products_found_info)
        elem = driver_instance.find_element(by=By.XPATH, value=no_products_found_info)
        if 'Nie znaleziono produktów, których szukasz.' in elem.text:
            print('INFO No products found.')
        return elem.is_displayed()
    except NoSuchElementException:
        return False


def move_to_next_page(driver_instance):
    elem = driver_instance.find_element(by=By.XPATH, value=next_page_button)
    elem.click()


def move_to_previous_page(driver_instance):
    elem = driver_instance.find_element(by=By.XPATH, value=previous_page_button)
    elem.click()
