from tests.helpers.support_functions import *

checkboxes_tab = 'checkbox-header'
all_checkboxes = 'checkboxes'
checkbox_1 = '//*[@id="checkboxes"]/input[1]'
checkbox_2 = '//*[@id="checkboxes"]/input[2]'


def click_checkboxes_tab(driver_instance):
    wait_for_visibility_of_element_by_id(driver_instance, checkboxes_tab)
    elem = driver_instance.find_element(by=By.ID, value=checkboxes_tab)
    elem.click()


def checkboxes_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, all_checkboxes)
    return elem.is_displayed()


def click_checkboxes(driver_instance):
    elem1 = driver_instance.find_element(by=By.XPATH, value=checkbox_1)
    elem1.click()
    elem2 = driver_instance.find_element(by=By.XPATH, value=checkbox_2)
    elem2.click()
