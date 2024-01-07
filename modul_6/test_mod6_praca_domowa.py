import unittest
from selenium import webdriver
from pages import iframe_page


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://simpletestsite.fabrykatestow.pl/')
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_iframe_visible(self):
        iframe_page.click_iframe_tab(self.driver)
        self.assertTrue(iframe_page.iframe_content_visible(self.driver))

    def test2_iframe_click_first_button(self):
        iframe_page.click_iframe_tab(self.driver)
        iframe_page.show_whole_iframe_element(self.driver)
        self.assertTrue(iframe_page.click_on_button_inside_iframe(self.driver, 1))
        self.driver.save_screenshot('iframe_found_screenshot.png')
