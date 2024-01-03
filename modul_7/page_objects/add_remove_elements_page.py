from tests.helpers.support_functions import *

add_remove_elements_tab = 'addremoveelements-header'
add_remove_elements_content = 'addremoveelements-content'
add_element_button = '//*[@id="addremoveelements-content"]/div/div/button'
added_element = '//*[@id="elements"]/button'


def click_add_remove_elements_tab(driver_instance):
    elem = driver_instance.find_element(by=By.ID, value=add_remove_elements_tab)
    elem.click()


def add_remove_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, add_remove_elements_content)
    return elem.is_displayed()


def add_element(driver_instance):
    elem = driver_instance.find_element(by=By.XPATH, value=add_element_button)
    elem.click()


def add_more_elements(driver_instance, elements_number):
    elem = driver_instance.find_element(by=By.XPATH, value=add_element_button)
    for i in range(0, elements_number):
        elem.click()


def delete_element(driver_instance):
    elem = driver_instance.find_element(by=By.XPATH, value=added_element)
    elem.click()
    wait_for_invisibility_of_element_by_xpath(driver_instance, added_element)


def delete_all_elements(driver_instance):
    total_elements = driver_instance.find_elements(by=By.XPATH, value=added_element)
    for i in range(0, len(total_elements), 1):
        element = added_element + '[1]'
        elem = driver_instance.find_element(by=By.XPATH, value=element)
        elem.click()
    wait_for_invisibility_of_element_by_xpath(driver_instance, added_element)


def element_invisible(driver_instance):
    try:
        wait_for_invisibility_of_element_by_xpath(driver_instance, added_element)
        return True
    except NoSuchElementException:
        return False
