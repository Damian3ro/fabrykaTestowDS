from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from helpers.support_functions import *

iframe_tab = 'iframe-header'
iframe_content = 'iframe-content'
iframe_main = 'iframe'
button1 = 'simpleButton1'
button2 = 'simpleButton2'
message = 'whichButtonIsClickedMessage'


def click_iframe_tab(driver_instance):
    elem = driver_instance.find_element(by=By.ID, value=iframe_tab)
    elem.click()


def iframe_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, iframe_content)
    return elem.is_displayed()


def show_whole_iframe_element(driver_instance):
    elem = driver_instance.find_element(by=By.ID, value=iframe_content)
    delta_y = elem.rect['height']
    scroll_origin = ScrollOrigin.from_element(elem)
    ActionChains(driver_instance).scroll_from_origin(scroll_origin, 0, delta_y).perform()


def click_on_button_inside_iframe(driver_instance, button_number):
    wait_for_visibility_of_element_by_tag_name(driver_instance, iframe_main, time_to_wait=5)
    driver_instance.switch_to.frame(driver_instance.find_element(by=By.TAG_NAME, value='iframe'))
    if button_number == 1:
        driver_instance.find_element(by=By.ID, value=button1).click()
        output = driver_instance.find_element(by=By.ID, value=message).text
        if output == 'Button 1 was clicked!':
            return True
        else:
            return False
    elif button_number == 2:
        driver_instance.find_element(by=By.ID, value=button2).click()
        output = driver_instance.find_element(by=By.ID, value=message).text
        if output == 'Button 2 was clicked!':
            return True
        else:
            return False
