import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = 'https://simpletestsite.fabrykatestow.pl/'
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1(self):
        self.driver.find_element(by=By.ID, value='checkbox-header').click()
        wait = WebDriverWait(self.driver, timeout=2)
        checkbox = self.driver.find_element(by=By.XPATH, value='//*[@id="checkboxes"]/input[2]')
        wait.until(lambda d: checkbox.is_displayed())
        checkbox.click()
        self.driver.save_screenshot('page_screenshot.png')
