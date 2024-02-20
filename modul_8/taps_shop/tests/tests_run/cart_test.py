import unittest
from selenium import webdriver
from config.test_settings import TestSettings
from tests.page_objects import main_page, cart_page


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_add_item_to_cart_checked_on_cart_page(self):
        main_page.close_bottom_message_info_panel(self.driver)
        main_page.add_items_to_cart(self.driver, 1)
        main_page.go_to_cart_page_by_button_under_item(self.driver, 3, item_name='hoodie')
        self.assertTrue(cart_page.check_item_in_cart(self.driver))

    def test2_add_item_to_cart_checked_on_main_page_in_cart_summary_tab(self):
        main_page.close_bottom_message_info_panel(self.driver)
        main_page.add_items_to_cart(self.driver, 1)
        self.assertTrue(main_page.check_item_in_cart_summary_tab(self.driver))

    def test3_remove_item_from_cart_on_cart_page(self):
        main_page.close_bottom_message_info_panel(self.driver)
        main_page.add_items_to_cart(self.driver, 1)
        main_page.go_to_cart_page_by_button_under_item(self.driver, 3, item_name='hoodie')
        self.assertTrue(cart_page.check_item_in_cart(self.driver))
        cart_page.remove_item_from_cart(self.driver)
        self.assertTrue(cart_page.check_item_not_in_cart(self.driver))

    def test4_remove_item_from_cart_on_main_page_in_cart_summary_tab(self):
        main_page.close_bottom_message_info_panel(self.driver)
        main_page.add_items_to_cart(self.driver, 1)
        main_page.see_summary_button_in_cart_summary_tab_visible(self.driver)
        self.assertTrue(main_page.check_item_in_cart_summary_tab(self.driver))
        main_page.remove_items_from_cart(self.driver)
        self.assertTrue(main_page.check_item_not_in_cart_summary_tab(self.driver))

    def test5_undo_removed_item_from_cart_on_cart_page(self):
        main_page.close_bottom_message_info_panel(self.driver)
        main_page.add_items_to_cart(self.driver, 1)
        main_page.go_to_cart_page_by_button_under_item(self.driver, 3, item_name='hoodie')
        self.assertTrue(cart_page.check_item_in_cart(self.driver))
        cart_page.remove_item_from_cart(self.driver)
        self.assertTrue(cart_page.check_item_not_in_cart(self.driver))
        cart_page.undo_removed_item_in_cart(self.driver)
        self.assertTrue(cart_page.check_item_in_cart(self.driver))

    def test6_check_empty_cart_on_cart_page(self):
        main_page.close_bottom_message_info_panel(self.driver)
        main_page.go_to_cart_page_by_cart_tab_button(self.driver)
        self.assertTrue(cart_page.check_empty_cart_info(self.driver))

    def test7_check_empty_cart_on_main_page_in_cart_summary_tab(self):
        main_page.close_bottom_message_info_panel(self.driver)
        self.assertTrue(main_page.check_empty_cart_info(self.driver))

    def test8_check_proper_order_net_value_on_cart_page(self):
        main_page.close_bottom_message_info_panel(self.driver)
        main_page.add_items_to_cart(self.driver, 3, item_name='hoodie')
        main_page.add_items_to_cart(self.driver, 2, item_name='glasses')
        main_page.go_to_cart_page_by_cart_tab_button(self.driver)
        self.assertEqual(cart_page.check_cart_total_amount(self.driver), '€315,00')

    def test9_check_proper_order_net_value_on_main_page_in_cart_summary_tab(self):
        main_page.close_bottom_message_info_panel(self.driver)
        main_page.add_items_to_cart(self.driver, 4, item_name='hoodie')
        main_page.add_items_to_cart(self.driver, 1, item_name='glasses')
        self.assertEqual(main_page.check_cart_summary_amount(self.driver), '€270,00')

    def test10_check_proper_order_vat_value_on_cart_page(self):
        main_page.close_bottom_message_info_panel(self.driver)
        main_page.add_items_to_cart(self.driver, 5, item_name='hoodie')
        main_page.add_items_to_cart(self.driver, 1, item_name='glasses')
        main_page.go_to_cart_page_by_cart_tab_button(self.driver)
        self.assertEqual(cart_page.check_cart_vat_amount(self.driver), '€73,60')

    def test11_check_proper_order_total_value_on_cart_page(self):
        main_page.close_bottom_message_info_panel(self.driver)
        main_page.add_items_to_cart(self.driver, 2, item_name='hoodie')
        main_page.add_items_to_cart(self.driver, 3, item_name='glasses')
        main_page.go_to_cart_page_by_cart_tab_button(self.driver)
        self.assertEqual(cart_page.check_cart_total_amount_with_vat(self.driver), '€448,95')

    def test12_check_changed_amount_of_product_on_cart_page(self):
        main_page.close_bottom_message_info_panel(self.driver)
        main_page.add_items_to_cart(self.driver, 1, item_name='glasses')
        main_page.go_to_cart_page_by_cart_tab_button(self.driver)
        cart_page.change_product_amount_in_cart(self.driver, 15)
        self.assertEqual(cart_page.check_product_quantity_in_cart(self.driver), '15')


if __name__ == '__main__':
    unittest.main()
