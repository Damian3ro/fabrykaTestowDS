from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


def hover_over_element_by_id(driver_instance, identity):
    elem = driver_instance.find_element(by=By.ID, value=identity)
    hover = ActionChains(driver_instance).move_to_element(elem)
    hover.perform()


def hover_over_element_by_xpath(driver_instance, xpath):
    elem = driver_instance.find_element(by=By.XPATH, value=xpath)
    hover = ActionChains(driver_instance).move_to_element(elem)
    hover.perform()


def press_key_on_element_by_id(driver_instance, identity, key):
    elem = driver_instance.find_element(by=By.ID, value=identity)
    press_key = ActionChains(driver_instance).key_down(key, elem)
    press_key.perform()


def release_key_pressed_on_element_by_id(driver_instance, identity, key):
    elem = driver_instance.find_element(by=By.ID, value=identity)
    release_key = ActionChains(driver_instance).key_up(key, elem)
    release_key.perform()


def drag_and_drop_element_by_id(driver_instance, draggable, droppable):
    dragging_elem = driver_instance.find_element(by=By.ID, value=draggable)
    dropping_elem = driver_instance.find_element(by=By.ID, value=droppable)
    drag_and_drop = ActionChains(driver_instance).drag_and_drop(dragging_elem, dropping_elem)
    drag_and_drop.perform()


def wait_for_visibility_of_element_by_id(driver_instance, identity, time_to_wait=10):
    try:
        elem = WebDriverWait(driver_instance, time_to_wait).until(EC.visibility_of_element_located((By.ID, identity)))
    except TimeoutException:
        elem = False
    return elem


def wait_for_visibility_of_element_by_tag_name(driver_instance, tag_name, time_to_wait=10):
    try:
        elem = WebDriverWait(driver_instance, time_to_wait).until(
            EC.visibility_of_element_located((By.TAG_NAME, tag_name)))
    except TimeoutException:
        elem = False
    return elem


def wait_for_visibility_of_element_by_xpath(driver_instance, xpath, time_to_wait=10):
    try:
        elem = WebDriverWait(driver_instance, time_to_wait).until(
            EC.visibility_of_element_located((By.XPATH, xpath)))
    except TimeoutException:
        elem = False
    return elem


def wait_for_invisibility_of_element_by_id(inv_driver_instance, identity, time_to_wait=8):
    inv_elem = WebDriverWait(inv_driver_instance, time_to_wait).until(
        EC.invisibility_of_element_located((By.ID, identity)))
    return inv_elem


def wait_for_invisibility_of_element_by_tag_name(inv_driver_instance, tag_name, time_to_wait=8):
    inv_elem = WebDriverWait(inv_driver_instance, time_to_wait).until(
        EC.invisibility_of_element_located((By.TAG_NAME, tag_name)))
    return inv_elem


def wait_for_invisibility_of_element_by_xpath(inv_driver_instance, xpath, time_to_wait=8):
    inv_elem = WebDriverWait(inv_driver_instance, time_to_wait).until(
        EC.invisibility_of_element_located((By.XPATH, xpath)))
    return inv_elem


def wait_for_visibility_of_alert(driver_instance, time_to_wait=8):
    try:
        elem = WebDriverWait(driver_instance, time_to_wait).until(EC.alert_is_present())
    except TimeoutException:
        elem = False
    return elem


def wait_for_presence_of_element_by_id(driver_instance, identity, time_to_wait=10):
    try:
        elem = WebDriverWait(driver_instance, time_to_wait).until(EC.presence_of_element_located((By.ID, identity)))
    except TimeoutException:
        elem = False
    return elem


def wait_for_element_to_be_clickable_by_id(driver_instance, identity, time_to_wait=10):
    try:
        elem = WebDriverWait(driver_instance, time_to_wait).until(EC.element_to_be_clickable((By.ID, identity)))
    except TimeoutException:
        elem = False
    return elem


def wait_for_element_to_be_clickable_by_xpath(driver_instance, xpath, time_to_wait=10):
    try:
        elem = WebDriverWait(driver_instance, time_to_wait).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    except TimeoutException:
        elem = False
    return elem


def wait_for_staleness_of_element_by_id(driver_instance, identity, time_to_wait=10):
    try:
        elem = WebDriverWait(driver_instance, time_to_wait).until(EC.staleness_of(
            driver_instance.find_element(By.ID, identity)))
    except TimeoutException:
        elem = False
    return elem


def wait_for_presence_of_text_in_element_attribute_by_id(driver_instance, identity, attribute, text, time_to_wait=10):
    try:
        elem = WebDriverWait(driver_instance, time_to_wait).until(
            EC.text_to_be_present_in_element_attribute((By.ID, identity),attribute, text))
    except TimeoutException:
        elem = False
    return elem


def wait_for_presence_of_text_in_element_attribute_by_xpath(driver_instance, xpath, attribute, text, time_to_wait=10):
    try:
        elem = WebDriverWait(driver_instance, time_to_wait).until(
            EC.text_to_be_present_in_element_attribute((By.XPATH, xpath), attribute, text))
    except TimeoutException:
        elem = False
    return elem
