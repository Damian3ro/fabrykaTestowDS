from tests.helpers.support_functions import *
from selenium.webdriver.common.by import By

drag_and_drop_tab = 'draganddrop-header'
drag_and_drop_content = 'draganddrop-content'
first_column = 'column-a'
second_column = 'column-b'
first_column_text = '//*[@id="column-a"]/header'
second_column_text = '//*[@id="column-b"]/header'


def click_drag_and_drop_tab(driver_instance):
    elem = driver_instance.find_element(by=By.ID, value=drag_and_drop_tab)
    elem.click()


def drag_and_drop_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, drag_and_drop_content)
    return elem.is_displayed()


def move_first_element_on_second_element(driver_instance):
    wait_for_visibility_of_element_by_id(driver_instance, first_column)
    wait_for_visibility_of_element_by_id(driver_instance, second_column)
    drag_and_drop_element_by_id(driver_instance, first_column, second_column)
    elem1 = driver_instance.find_element(by=By.XPATH, value=first_column_text)
    elem2 = driver_instance.find_element(by=By.XPATH, value=second_column_text)
    if elem1.text == 'B' and elem2.text == 'A':
        return True
    else:
        return False


def move_second_element_on_first_element(driver_instance):
    wait_for_visibility_of_element_by_id(driver_instance, first_column)
    wait_for_visibility_of_element_by_id(driver_instance, second_column)
    drag_and_drop_element_by_id(driver_instance, second_column, first_column)
    elem1 = driver_instance.find_element(by=By.XPATH, value=second_column_text)
    elem2 = driver_instance.find_element(by=By.XPATH, value=first_column_text)
    if elem1.text == 'A' and elem2.text == 'B':
        return True
    else:
        return False
