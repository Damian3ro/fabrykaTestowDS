import unittest
from selenium import webdriver
from config.test_settings import TestSettings
from tests.page_objects import main_page, shop_page


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_order_by_price_ascending(self):
        main_page.close_bottom_message_info_panel(self.driver)
        main_page.go_to_shop_page(self.driver)
        shop_page.select_ordering_option(self.driver, 4)
        self.assertEqual(shop_page.check_product_on_list(self.driver, list_item_number=1), 'V-Neck T-Shirt')
        shop_page.move_to_next_page(self.driver)
        self.assertEqual(shop_page.check_product_on_list(self.driver, last_product=True),
                         'Sunglasses')

    def test2_order_by_price_descending(self):
        main_page.close_bottom_message_info_panel(self.driver)
        main_page.go_to_shop_page(self.driver)
        shop_page.select_ordering_option(self.driver, 5)
        self.assertEqual(shop_page.check_product_on_list(self.driver, list_item_number=1), 'Sunglasses')
        shop_page.move_to_next_page(self.driver)
        self.assertEqual(shop_page.check_product_on_list(self.driver, last_product=True),
                         'V-Neck T-Shirt')

    def test3_search_correct_product_in_shop(self):
        main_page.close_bottom_message_info_panel(self.driver)
        main_page.go_to_shop_page(self.driver)
        shop_page.search_products(self.driver, 'hoodie')
        self.assertEqual(shop_page.get_products_count_found_on_page(self.driver), 3)
        self.assertEqual(shop_page.check_product_on_list(self.driver, list_item_number=1), 'Hoodie with Zipper')
        self.assertEqual(shop_page.check_product_on_list(self.driver, list_item_number=2), 'Hoodie')
        self.assertEqual(shop_page.check_product_on_list(self.driver, list_item_number=3), 'Hoodie with Logo')

    def test4_search_incorrect_product_in_shop(self):
        main_page.close_bottom_message_info_panel(self.driver)
        main_page.go_to_shop_page(self.driver)
        shop_page.search_products(self.driver, 'test123')
        self.assertTrue(shop_page.check_incorrect_product_searching(self.driver))


if __name__ == '__main__':
    unittest.main()
