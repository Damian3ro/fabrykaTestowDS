from tests.helpers.support_functions import *

item_in_cart = '//tr[contains(@class,"woocommerce-cart-form__cart-item cart_item")][1]'
remove_item_from_cart_button = ('//tr[contains(@class,"woocommerce-cart-form__cart-item cart_item")][1]/'
                                'td[contains(@class,"product-remove")]/a')
undo_removed_item_button = '//div[contains(@class,"wc-block-components-notice-banner__content")]//a[text()="Cofnij?"]'
submit_cart_button = '//div[contains(@class,"wc-proceed-to-checkout")]//a[contains(@class,"checkout-button")]'
bottom_message_info_reject_button = '//a[contains(@class,"woocommerce-store-notice__dismiss-link")]'
empty_cart_info = '//*[@id="post-7"]/div/div/div[2]/div'
total_amount_info = '//tr[@class="cart-subtotal"]//span[contains(@class,"woocommerce-Price-amount")]//bdi'
vat_amount_info = '//tr[contains(@class,"tax-rate")]//span[contains(@class,"woocommerce-Price-amount")]'
total_amount_with_vat_info = '//tr[@class="order-total"]//span[contains(@class,"woocommerce-Price-amount")]//bdi'
item_quantity_input = ('//div[contains(@class,"quantity")]//input[@type="number" and '
                       'contains(@aria-label,"Ilość produktu")]')
update_cart_button = '//td[contains(@class,"actions")]//button[@type="submit" and @name="update_cart"]'


def close_bottom_message_info_panel(driver_instance):
    elem = driver_instance.find_element(by=By.XPATH, value=bottom_message_info_reject_button)
    elem.click()


def check_item_in_cart(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, item_in_cart)
    return elem.is_displayed()


def check_item_not_in_cart(driver_instance):
    try:
        wait_for_visibility_of_element_by_xpath(driver_instance, item_in_cart)
        return True
    except NoSuchElementException:
        return False


def check_empty_cart_info(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, empty_cart_info)
    if 'Twój koszyk aktualnie jest pusty.' in elem.text:
        return True
    else:
        return False


def check_product_quantity_in_cart(driver_instance):
    wait_for_visibility_of_element_by_xpath(driver_instance, item_quantity_input)
    elem = driver_instance.find_element(by=By.XPATH, value=item_quantity_input)
    return elem.get_attribute("value")


def check_cart_total_amount(driver_instance):
    wait_for_visibility_of_element_by_xpath(driver_instance, total_amount_info)
    elem = driver_instance.find_element(by=By.XPATH, value=total_amount_info)
    return elem.text


def check_cart_vat_amount(driver_instance):
    wait_for_visibility_of_element_by_xpath(driver_instance, vat_amount_info)
    elem = driver_instance.find_element(by=By.XPATH, value=vat_amount_info)
    return elem.text


def check_cart_total_amount_with_vat(driver_instance):
    wait_for_visibility_of_element_by_xpath(driver_instance, total_amount_with_vat_info)
    elem = driver_instance.find_element(by=By.XPATH, value=total_amount_with_vat_info)
    return elem.text


def approve_cart(driver_instance):
    elem = driver_instance.find_element(by=By.XPATH, value=submit_cart_button)
    elem.click()


def remove_item_from_cart(driver_instance):
    elem = driver_instance.find_element(by=By.XPATH, value=remove_item_from_cart_button)
    elem.click()


def undo_removed_item_in_cart(driver_instance):
    wait_for_visibility_of_element_by_xpath(driver_instance, undo_removed_item_button)
    elem = driver_instance.find_element(by=By.XPATH, value=undo_removed_item_button)
    elem.click()


def change_product_amount_in_cart(driver_instance, item_amount):
    wait_for_visibility_of_element_by_xpath(driver_instance, item_quantity_input)
    elem = driver_instance.find_element(by=By.XPATH, value=item_quantity_input)
    elem.clear()
    elem.send_keys(item_amount)
    wait_for_element_to_be_clickable_by_xpath(driver_instance, update_cart_button)
    elem1 = driver_instance.find_element(by=By.XPATH, value=update_cart_button)
    elem1.click()
