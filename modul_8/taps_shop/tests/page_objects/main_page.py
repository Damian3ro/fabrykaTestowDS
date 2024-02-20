from tests.helpers.support_functions import *

taps_logo = '//*[@id="masthead"]/div[1]/div[1]/a/img'
my_account_page_header_link = 'menu-item-100'
cart_page_header_link = 'menu-item-99'
shop_page_header_link = 'menu-item-102'
bottom_message_info_reject_button = '//a[contains(@class,"woocommerce-store-notice__dismiss-link")]'

any_product_on_new_products_list = '//div[contains(@data-block-name,"woocommerce/product-new")]/ul/li'
add_to_cart_button_under_item = ('/div[contains(@class,"wc-block-grid__product-add-to-cart")]/'
                                 'a[contains(@class,"add_to_cart_button ajax_add_to_cart")]')
go_to_cart_button_under_item = ('/div[contains(@class,"wc-block-grid__product-add-to-cart")]/'
                                                   'a[contains(@class,"added_to_cart wc-forward")]')
add_hoodie_to_cart_button = ('//div[contains(@class,"wc-block-grid__product-add-to-cart")]/'
                             'a[contains(@data-product_sku,"woo-hoodie-with-zipper")]')
add_glasses_to_cart_button = ('//div[contains(@class,"wc-block-grid__product-add-to-cart")]/'
                             'a[contains(@data-product_sku,"woo-sunglasses")]')

cart_summary_tab_button = 'site-header-cart'
cart_summary_tab_items_number_info = ('//ul[contains(@class,"woocommerce-mini-cart cart_list product_list_widget")]/'
                                      'li[contains(@class,"woocommerce-mini-cart-item")]/span')
cart_summary_tab_see_cart_button = ('//p[contains(@class,"woocommerce-mini-cart__buttons")]/'
                                   'a[contains(@class,"button wc-forward")]')
cart_summary_tab_order_button = ('//p[contains(@class,"woocommerce-mini-cart__buttons")]/'
                                   'a[contains(@class,"button checkout wc-forward")]')
cart_summary_tab_empty_cart_info = '//p[contains(@class,"woocommerce-mini-cart__empty-message")]'
cart_summary_tab_remove_item_button = ('//li[contains(@class,"woocommerce-mini-cart-item")]/'
                                       'a[contains(@class,"remove_from_cart_button")]')
cart_summary_tab_amount = '//p[contains(@class,"woocommerce-mini-cart__total total")]/span/bdi'

def get_xpath_for_add_cart_button_under_item(product_number):
    elem_xpath = any_product_on_new_products_list + '[' + str(product_number) + ']' + go_to_cart_button_under_item
    return elem_xpath


def get_xpath_for_see_cart_button_under_item(product_number):
    elem_xpath = any_product_on_new_products_list + '[' + str(product_number) + ']' + go_to_cart_button_under_item
    return elem_xpath


def taps_logo_visible(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, taps_logo)
    return elem.is_displayed()


def see_summary_button_in_cart_summary_tab_visible(driver_instance):
    hover_over_element_by_id(driver_instance, cart_summary_tab_button)
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, cart_summary_tab_see_cart_button)
    return elem.is_displayed()


def check_item_in_cart_summary_tab(driver_instance):
    hover_over_element_by_id(driver_instance, cart_summary_tab_button)
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, cart_summary_tab_items_number_info)
    return elem.is_displayed()


def check_item_not_in_cart_summary_tab(driver_instance):
    try:
        hover_over_element_by_id(driver_instance, cart_summary_tab_button)
        wait_for_visibility_of_element_by_xpath(driver_instance, cart_summary_tab_items_number_info)
        return True
    except NoSuchElementException:
        return False


def check_empty_cart_info(driver_instance):
    hover_over_element_by_id(driver_instance, cart_summary_tab_button)
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, cart_summary_tab_empty_cart_info)
    if 'Brak produktów w koszyku.' in elem.text:
        return True
    else:
        return False


def check_cart_summary_amount(driver_instance):
    hover_over_element_by_id(driver_instance, cart_summary_tab_button)
    wait_for_visibility_of_element_by_xpath(driver_instance, cart_summary_tab_amount)
    elem = driver_instance.find_element(by=By.XPATH, value=cart_summary_tab_amount)
    return elem.text


def go_to_login_page(driver_instance):
    wait_for_visibility_of_element_by_id(driver_instance, my_account_page_header_link)
    elem = driver_instance.find_element(by=By.ID, value=my_account_page_header_link)
    elem.click()


def go_to_cart_page_by_cart_tab_button(driver_instance):
    wait_for_visibility_of_element_by_id(driver_instance, cart_page_header_link)
    elem = driver_instance.find_element(by=By.ID, value=cart_page_header_link)
    elem.click()


def go_to_cart_page_by_cart_summary_button(driver_instance):
    wait_for_visibility_of_element_by_id(driver_instance, cart_summary_tab_button)
    elem = driver_instance.find_element(by=By.ID, value=cart_summary_tab_button)
    elem.click()


def go_to_cart_page_by_see_cart_button_in_cart_summary_tab(driver_instance):
    wait_for_visibility_of_element_by_xpath(driver_instance, cart_summary_tab_see_cart_button)
    elem = driver_instance.find_element(by=By.XPATH, value=cart_summary_tab_see_cart_button)
    elem.click()


def go_to_cart_page_by_button_under_item(driver_instance, item_number, item_name=None):
    if item_number > 0:
        if item_name == 'hoodie':
            item_number = 3
        elem_xpath = get_xpath_for_see_cart_button_under_item(item_number)
        wait_for_visibility_of_element_by_xpath(driver_instance, elem_xpath)
        elem = driver_instance.find_element(by=By.XPATH, value=elem_xpath)
        elem.click()
    else:
        raise ValueError('Incorrect entered number of items.')


def go_to_shop_page(driver_instance):
    wait_for_visibility_of_element_by_id(driver_instance, shop_page_header_link)
    elem = driver_instance.find_element(by=By.ID, value=shop_page_header_link)
    elem.click()


def close_bottom_message_info_panel(driver_instance):
    hover_over_element_by_id(driver_instance, cart_summary_tab_button)
    elem = driver_instance.find_element(by=By.XPATH, value=bottom_message_info_reject_button)
    elem.click()


def add_items_to_cart(driver_instance, items_number, item_name='hoodie', item_list_number=None):
    if items_number > 0:
        for item in range(items_number):
            if item_name == 'hoodie':
                adding_item = add_hoodie_to_cart_button
            elif item_name == 'glasses':
                adding_item = add_glasses_to_cart_button
            else:
                if item_list_number is not None:
                    adding_item = get_xpath_for_add_cart_button_under_item(item_list_number)
                else:
                    raise ValueError('Incorrect entered list number of item.')
            wait_for_visibility_of_element_by_xpath(driver_instance, adding_item)
            elem = driver_instance.find_element(by=By.XPATH, value=adding_item)
            elem.click()
            wait_for_presence_of_text_in_element_attribute_by_xpath(driver_instance, adding_item, 'class',
                                                                    'added')
    else:
        raise ValueError('Incorrect entered number of items.')


def remove_items_from_cart(driver_instance):
    elem = driver_instance.find_element(by=By.XPATH, value=cart_summary_tab_remove_item_button)
    elem.click()
