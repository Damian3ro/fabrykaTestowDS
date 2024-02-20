import unittest
from selenium import webdriver
from config.test_settings import TestSettings
from tests.page_objects import main_page, login_page, my_account_page, forgotten_password_page, invalid_page


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_main_page_logo_visible(self):
        self.assertTrue(main_page.taps_logo_visible(self.driver))

    def test2_correct_login_credentials_option1(self):
        main_page.go_to_login_page(self.driver)
        login_page.correct_login(self.driver, 1)
        self.assertTrue(my_account_page.my_account_welcome_info_visible(self.driver, login_page.get_username(1)))

    def test3_correct_login_credentials_option2(self):
        main_page.go_to_login_page(self.driver)
        login_page.correct_login(self.driver, 2)
        self.assertTrue(my_account_page.my_account_welcome_info_visible(self.driver, login_page.get_username(2)))

    def test4_correct_login_credentials_option3(self):
        main_page.go_to_login_page(self.driver)
        login_page.correct_login(self.driver, 3)
        self.assertTrue(my_account_page.my_account_welcome_info_visible(self.driver, login_page.get_username(3)))

    def test4_correct_login_credentials_option4(self):
        main_page.go_to_login_page(self.driver)
        login_page.correct_login(self.driver, 4)
        self.assertTrue(my_account_page.my_account_welcome_info_visible(self.driver, login_page.get_username(4)))

    def test5_correct_login_credentials_option5(self):
        main_page.go_to_login_page(self.driver)
        login_page.correct_login(self.driver, 5)
        self.assertTrue(my_account_page.my_account_welcome_info_visible(self.driver, login_page.get_username(5)))

    def test6_incorrect_login_different_logins(self):
        main_page.go_to_login_page(self.driver)
        self.assertTrue(login_page.incorrect_login_different_logins(self.driver))

    def test7_incorrect_login_too_many_attempts(self):
        main_page.go_to_login_page(self.driver)
        self.assertTrue(login_page.incorrect_login_the_same_login_too_many_attempts(self.driver))

    def test8_incorrect_login_empty_login_and_password_inputs(self):
        main_page.go_to_login_page(self.driver)
        self.assertTrue(login_page.incorrect_login_empty_login_and_password_inputs(self.driver))

    def test9_incorrect_login_empty_login_input(self):
        main_page.go_to_login_page(self.driver)
        self.assertTrue(login_page.incorrect_login_only_empty_login_input(self.driver))

    def test10_incorrect_login_empty_password_input(self):
        main_page.go_to_login_page(self.driver)
        self.assertTrue(login_page.incorrect_login_only_empty_password_input(self.driver))

    def test11_forgotten_password(self):
        main_page.go_to_login_page(self.driver)
        login_page.move_to_forgotten_password_page(self.driver)
        self.assertTrue(forgotten_password_page.forgotten_password_header_visible(self.driver))
        self.assertTrue(forgotten_password_page.reset_password(self.driver))

    def test12_correct_register(self):
        main_page.go_to_login_page(self.driver)
        login_page.correct_register(self.driver)
        self.assertTrue(my_account_page.my_account_welcome_info_visible(self.driver,
                            login_page.generated_proper_email.split('@')[0].lower()))

    def test13_incorrect_register_wrong_email(self):
        main_page.go_to_login_page(self.driver)
        self.assertTrue(login_page.incorrect_register_wrong_email(self.driver))

    def test14_incorrect_register_empty_email_input(self):
        main_page.go_to_login_page(self.driver)
        self.assertTrue(login_page.incorrect_register_empty_email_input(self.driver))

    def test15_privacy_policy(self):
        main_page.go_to_login_page(self.driver)
        login_page.open_privacy_policy(self.driver)
        self.assertTrue(invalid_page.error_info_visible(self.driver))


if __name__ == '__main__':
    unittest.main()
