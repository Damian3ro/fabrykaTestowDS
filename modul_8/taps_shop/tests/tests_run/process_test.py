import unittest
from selenium import webdriver
from config.test_settings import TestSettings
from tests.page_objects import main_page, cart_page, order_page, order_received_page


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_full_order_process(self):
        self.assertTrue(main_page.taps_logo_visible(self.driver))
        main_page.close_bottom_message_info_panel(self.driver)
        main_page.add_items_to_cart(self.driver, 1)
        main_page.go_to_cart_page_by_button_under_item(self.driver, 3, item_name='hoodie')
        self.assertTrue(cart_page.check_item_in_cart(self.driver))
        cart_page.approve_cart(self.driver)
        order_page.proper_fill_all_form_areas(self.driver)
        order_page.submit_order(self.driver)
        self.assertTrue(order_received_page.order_received_info_visible(self.driver))

    def test2_check_order_summary_details(self):
        self.assertTrue(main_page.taps_logo_visible(self.driver))
        main_page.close_bottom_message_info_panel(self.driver)
        main_page.add_items_to_cart(self.driver, 3)
        main_page.go_to_cart_page_by_button_under_item(self.driver, 3, item_name='hoodie')
        self.assertTrue(cart_page.check_item_in_cart(self.driver))
        cart_page.approve_cart(self.driver)
        order_page.proper_fill_all_form_areas(self.driver)
        order_page.submit_order(self.driver)
        self.assertTrue(order_received_page.order_received_info_visible(self.driver))
        self.assertEqual(order_received_page.check_order_date(self.driver), order_received_page.get_current_date())
        self.assertEqual(order_received_page.check_order_net_amount(self.driver), '€135,00')
        self.assertEqual(order_received_page.check_order_ship_amount(self.driver), '€100,00')
        self.assertEqual(order_received_page.check_order_vat_amount(self.driver), '€54,05')
        self.assertEqual(order_received_page.check_order_total_amount(self.driver), '€289,05')


if __name__ == '__main__':
    unittest.main()
