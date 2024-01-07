from tests.helpers.support_functions import *

hovers_tab = 'hovers-header'
hovers_content = 'hovers-content'
gentleman_pic = '//*[@id="hovers-content"]/div/div[1]/img'
gentleman_link = '//*[@id="hovers-content"]/div/div[1]/div/a'
devil_pic = '//*[@id="hovers-content"]/div/div[2]/img'
devil_link = '//*[@id="hovers-content"]/div/div[2]/div/a'
monk_pic = '//*[@id="hovers-content"]/div/div[3]/img'
monk_link = '//*[@id="hovers-content"]/div/div[3]/div/a'


def click_hovers_tab(driver_instance):
    wait_for_visibility_of_element_by_id(driver_instance, hovers_tab)
    elem = driver_instance.find_element(by=By.ID, value=hovers_tab)
    elem.click()


def hovers_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, hovers_content)
    return elem.is_displayed()


def hover_over_element_and_click(driver_instance, user_number):
    user_pic = ''
    user_link = ''
    if user_number == 1:
        user_pic = gentleman_pic
        user_link = gentleman_link
    elif user_number == 2:
        user_pic = devil_pic
        user_link = devil_link
    elif user_number == 3:
        user_pic = monk_pic
        user_link = monk_link
    hover_over_element_by_xpath(driver_instance, user_pic)
    elem = driver_instance.find_element(by=By.XPATH, value=user_link)
    elem.click()
