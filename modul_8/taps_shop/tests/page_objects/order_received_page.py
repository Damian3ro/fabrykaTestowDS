from tests.helpers.support_functions import *
from datetime import date, datetime

order_received_info = '//div[contains(@class,"woocommerce-order")]/p[contains(@class,"thankyou-order-received")]'
order_date = '//ul[contains(@class,"woocommerce-thankyou-order-details order_details")]/li[2]/strong'
order_amount = ('//ul[contains(@class,"woocommerce-thankyou-order-details order_details")]/li[3]/'
                'span[contains(@class,"woocommerce-Price-amount amount")]/bdi')
product_name = '//td[contains(@class,"woocommerce-table__product-name product-name")]/a'
product_quantity = ('//td[contains(@class,"woocommerce-table__product-name product-name")]/'
                    'strong[contains(@class,"product-quantity")]')
order_net_amount = '//table[contains(@class,"shop_table order_details")]/tfoot/tr[1]/td/span'
order_ship_amount = '//table[contains(@class,"shop_table order_details")]/tfoot/tr[2]/td/span'
order_vat_amount = '//table[contains(@class,"shop_table order_details")]/tfoot/tr[3]/td/span'
order_sum_amount = '//table[contains(@class,"shop_table order_details")]/tfoot/tr[5]/td/span'

def order_received_info_visible(driver_instance):
    try:
        wait_for_visibility_of_element_by_xpath(driver_instance, order_received_info)
        elem_text_visibility = 'Otrzymaliśmy Twoje zamówienie' in driver_instance.find_element(
            by=By.XPATH, value=order_received_info).text
        return elem_text_visibility
    except StaleElementReferenceException:
        return False


def convert_month(month):
    converted_month = ''
    if 'sty' in month:
        converted_month = '1'
    if 'lut' in month:
        converted_month = '2'
    if 'mar' in month:
        converted_month = '3'
    if 'kwi' in month:
        converted_month = '4'
    if 'maj' in month:
        converted_month = '5'
    if 'czerw' in month:
        converted_month = '6'
    if 'lip' in month:
        converted_month = '7'
    if 'sier' in month:
        converted_month = '8'
    if 'wrz' in month:
        converted_month = '9'
    if 'paź' in month:
        converted_month = '10'
    if 'lis' in month:
        converted_month = '11'
    if 'gru' in month:
        converted_month = '12'
    return converted_month


def convert_date(date_to_convert):
    first_space_index = date_to_convert.find(' ')
    order_year = date_to_convert[-4:]
    if first_space_index == 1:
        index = 1
    else:
        index = 2
    order_day = date_to_convert[:index]
    order_month = date_to_convert[index+1:-6]
    formatted_date = f'{order_year}-{convert_month(order_month)}-{order_day}'
    current_date = datetime.strptime(formatted_date, '%Y-%m-%d').strftime('%Y-%m-%d')
    return current_date


def get_current_date():
    current_date = date.today()
    return current_date.strftime('%Y-%m-%d')


def check_order_date(driver_instance):
    wait_for_visibility_of_element_by_xpath(driver_instance, order_date)
    elem = driver_instance.find_element(by=By.XPATH, value=order_date)
    return convert_date(elem.text)


def check_order_net_amount(driver_instance):
    wait_for_visibility_of_element_by_xpath(driver_instance, order_net_amount)
    elem = driver_instance.find_element(by=By.XPATH, value=order_net_amount)
    return elem.text


def check_order_ship_amount(driver_instance):
    wait_for_visibility_of_element_by_xpath(driver_instance, order_ship_amount)
    elem = driver_instance.find_element(by=By.XPATH, value=order_ship_amount)
    return elem.text


def check_order_vat_amount(driver_instance):
    wait_for_visibility_of_element_by_xpath(driver_instance, order_vat_amount)
    elem = driver_instance.find_element(by=By.XPATH, value=order_vat_amount)
    return elem.text


def check_order_total_amount(driver_instance):
    wait_for_visibility_of_element_by_xpath(driver_instance, order_sum_amount)
    elem = driver_instance.find_element(by=By.XPATH, value=order_sum_amount)
    return elem.text
