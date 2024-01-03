import unittest
from selenium import webdriver
from config.test_settings import TestSettings
from tests.page_objects import (home_page, checkboxes_page, date_picker_page, hovers_page, users_page, inputs_page,
                                basic_auth_page, user_logged_in_page, form_page, dropdown_list_page, key_presses_page,
                                drag_and_drop_page, add_remove_elements_page, status_codes_page, http_status_code_page,
                                iframe_page)


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_home_page_content_visibility(self):
        self.assertTrue(home_page.home_page_content_visible(self.driver))

    def test2_checkboxes(self):
        checkboxes_page.click_checkboxes_tab(self.driver)
        self.assertTrue(checkboxes_page.checkboxes_content_visible(self.driver))
        checkboxes_page.click_checkboxes(self.driver)

    def test3_date_picker_visibility(self):
        date_picker_page.click_date_picker_tab(self.driver)
        self.assertTrue(date_picker_page.date_picker_content_visible(self.driver))

    def test4_date_picker_correct_input(self):
        date_picker_page.click_date_picker_tab(self.driver)
        self.assertTrue(date_picker_page.send_correct_date_to_input(self.driver))

    def test5_date_picker_incorrect_input(self):
        date_picker_page.click_date_picker_tab(self.driver)
        self.assertTrue(date_picker_page.send_incorrect_date_to_input(self.driver))

    def test6_hovers_visibility(self):
        hovers_page.click_hovers_tab(self.driver)
        self.assertTrue(hovers_page.hovers_content_visible(self.driver))

    def test7_hovers_first_link_click(self):
        hovers_page.click_hovers_tab(self.driver)
        hovers_page.hover_over_element_and_click(self.driver, 1)
        self.assertTrue(users_page.error_info_visible(self.driver))

    def test8_hovers_second_link_click(self):
        hovers_page.click_hovers_tab(self.driver)
        hovers_page.hover_over_element_and_click(self.driver, 2)
        self.assertTrue(users_page.error_info_visible(self.driver))

    def test9_hovers_third_link_click(self):
        hovers_page.click_hovers_tab(self.driver)
        hovers_page.hover_over_element_and_click(self.driver, 3)
        self.assertTrue(users_page.error_info_visible(self.driver))

    def test10_inputs_visibility(self):
        inputs_page.click_inputs_tab(self.driver)
        self.assertTrue(inputs_page.input_content_visible(self.driver))

    def test11_inputs_correct_input(self):
        inputs_page.click_inputs_tab(self.driver)
        self.assertTrue(inputs_page.send_correct_chars_to_input(self.driver))

    def test12_inputs_incorrect_input(self):
        inputs_page.click_inputs_tab(self.driver)
        self.assertTrue(inputs_page.send_incorrect_chars_to_input(self.driver))

    def test13_basic_auth_visibility(self):
        basic_auth_page.click_basic_auth_tab(self.driver)
        self.assertTrue(basic_auth_page.basic_auth_content_visible(self.driver))

    def test14_basic_auth_correct_login(self):
        basic_auth_page.click_basic_auth_tab(self.driver)
        basic_auth_page.log_in_with_correct_credentials(self.driver)
        self.assertTrue(user_logged_in_page.user_logged_in_page_displayed(self.driver))

    def test15_basic_auth_incorrect_login(self):
        basic_auth_page.click_basic_auth_tab(self.driver)
        self.assertTrue(basic_auth_page.log_in_with_incorrect_credentials(self.driver))

    def test16_basic_auth_return_to_main_page(self):
        basic_auth_page.click_basic_auth_tab(self.driver)
        basic_auth_page.log_in_with_correct_credentials(self.driver)
        user_logged_in_page.return_to_home_page(self.driver)
        self.assertTrue(home_page.home_page_content_visible(self.driver))

    def test17_form_visibility(self):
        form_page.click_form_tab(self.driver)
        self.assertTrue(form_page.form_content_visible(self.driver))

    def test18_form_all_inputs_filled(self):
        form_page.click_form_tab(self.driver)
        self.assertTrue(form_page.submit_form_with_all_inputs_filled(self.driver))

    def test19_form_only_first_input_filled(self):
        form_page.click_form_tab(self.driver)
        self.assertFalse(form_page.submit_form_with_only_one_input_filled(self.driver, 1))

    def test20_form_only_second_input_filled(self):
        form_page.click_form_tab(self.driver)
        self.assertFalse(form_page.submit_form_with_only_one_input_filled(self.driver, 2))

    def test21_form_all_inputs_empty(self):
        form_page.click_form_tab(self.driver)
        self.assertFalse(form_page.submit_form_with_all_inputs_empty(self.driver))

    def test22_dropdown_select_default_option(self):
        dropdown_list_page.click_dropdown_tab(self.driver)
        self.assertTrue(dropdown_list_page.dropdown_content_visible(self.driver))
        self.assertTrue(dropdown_list_page.get_dropdown_list_value(self.driver, 0))

    def test23_dropdown_select_first_option(self):
        dropdown_list_page.click_dropdown_tab(self.driver)
        self.assertTrue(dropdown_list_page.dropdown_content_visible(self.driver))
        self.assertTrue(dropdown_list_page.get_dropdown_list_value(self.driver, 1))

    def test24_dropdown_select_second_option(self):
        dropdown_list_page.click_dropdown_tab(self.driver)
        self.assertTrue(dropdown_list_page.dropdown_content_visible(self.driver))
        self.assertTrue(dropdown_list_page.get_dropdown_list_value(self.driver, 2))

    def test25_key_presses_visibility(self):
        key_presses_page.click_key_presses_tab(self.driver)
        self.assertTrue(key_presses_page.key_presses_content_visible(self.driver))

    def test26_key_presses_press_letter_key_in_input(self):
        key_presses_page.click_key_presses_tab(self.driver)
        self.assertTrue(key_presses_page.press_letter_key_in_input(self.driver))

    def test27_key_presses_press_function_key_in_input(self):
        key_presses_page.click_key_presses_tab(self.driver)
        self.assertTrue(key_presses_page.press_function_key_in_input(self.driver))

    def test28_drag_and_drop_visibility(self):
        drag_and_drop_page.click_drag_and_drop_tab(self.driver)
        self.assertTrue(drag_and_drop_page.drag_and_drop_content_visible(self.driver))

    def test29_drag_and_drop_move_A_to_B(self):
        drag_and_drop_page.click_drag_and_drop_tab(self.driver)
        self.assertTrue(drag_and_drop_page.move_first_element_on_second_element(self.driver))

    def test30_drag_and_drop_move_B_to_A(self):
        drag_and_drop_page.click_drag_and_drop_tab(self.driver)
        self.assertTrue(drag_and_drop_page.move_second_element_on_first_element(self.driver))

    def test31_add_element(self):
        add_remove_elements_page.click_add_remove_elements_tab(self.driver)
        self.assertTrue(add_remove_elements_page.add_remove_content_visible(self.driver))
        add_remove_elements_page.add_element(self.driver)

    def test32_remove_element(self):
        add_remove_elements_page.click_add_remove_elements_tab(self.driver)
        self.assertTrue(add_remove_elements_page.add_remove_content_visible(self.driver))
        add_remove_elements_page.add_element(self.driver)
        add_remove_elements_page.delete_element(self.driver)
        self.assertTrue(add_remove_elements_page.element_invisible(self.driver))

    def test33_remove_all_elements(self):
        add_remove_elements_page.click_add_remove_elements_tab(self.driver)
        self.assertTrue(add_remove_elements_page.add_remove_content_visible(self.driver))
        add_remove_elements_page.add_more_elements(self.driver, 5)
        add_remove_elements_page.delete_all_elements(self.driver)
        self.assertTrue(add_remove_elements_page.element_invisible(self.driver))

    def test34_status_codes_visibility(self):
        status_codes_page.click_status_codes_tab(self.driver)
        self.assertTrue(status_codes_page.status_codes_content_visible(self.driver))

    def test35_status_codes_click_200_code(self):
        status_codes_page.click_status_codes_tab(self.driver)
        status_codes_page.click_on_code_link(self.driver, 200)
        self.assertTrue(http_status_code_page.check_status_code(self.driver, 200))

    def test36_status_codes_click_305_code(self):
        status_codes_page.click_status_codes_tab(self.driver)
        status_codes_page.click_on_code_link(self.driver, 305)
        self.assertTrue(http_status_code_page.check_status_code(self.driver, 305))

    def test37_status_codes_click_404_code(self):
        status_codes_page.click_status_codes_tab(self.driver)
        status_codes_page.click_on_code_link(self.driver, 404)
        self.assertTrue(http_status_code_page.check_status_code(self.driver, 404))

    def test38_status_codes_click_500_code(self):
        status_codes_page.click_status_codes_tab(self.driver)
        status_codes_page.click_on_code_link(self.driver, 500)
        self.assertTrue(http_status_code_page.check_status_code(self.driver, 500))

    def test39_iframe_visible(self):
        iframe_page.click_iframe_tab(self.driver)
        self.assertTrue(iframe_page.iframe_content_visible(self.driver))

    def test40_iframe_click_first_button(self):
        iframe_page.click_iframe_tab(self.driver)
        self.assertTrue(iframe_page.click_on_button_inside_iframe(self.driver, 1))

    def test41_iframe_click_second_button(self):
        iframe_page.click_iframe_tab(self.driver)
        self.assertTrue(iframe_page.click_on_button_inside_iframe(self.driver, 2))


if __name__ == '__main__':
    unittest.main()
