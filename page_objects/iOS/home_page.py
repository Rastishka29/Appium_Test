from page_objects.base_page import BasePage
from locators.iOS.home_page_locators import HomePageLocators


class HomePage(BasePage):

    def open_text_entry(self):
        self.find_element(*HomePageLocators.text_entry).click()

    def submit_text_entry(self, message):
        self.find_element(*HomePageLocators.text_field).send_keys(message)
        self.find_element(*HomePageLocators.ok_btn).click()

    def is_text_field_displayed(self):
        return self.is_elem_displayed(*HomePageLocators.text_field)

    def scroll_and_open_toolbars(self):
        self.scroll_by_name("Toolbars")
        self.find_element(*HomePageLocators.toolbars).click()

    def scroll_up_and_open_action_sheets(self):
        self.scroll_by_direction("up")
        self.find_element(*HomePageLocators.action_sheets).click()

    def scroll_down_and_open_web_view(self):
        self.scroll_by_direction("down")
        self.find_element(*HomePageLocators.web_view).click()

    def is_toolbars_title_displayed(self):
        return self.is_elem_displayed(*HomePageLocators.toolbars)

    def is_action_sheets_title_displayed(self):
        return self.is_elem_displayed(*HomePageLocators.action_sheets)

    def is_web_view_title_displayed(self):
        return self.is_elem_displayed(*HomePageLocators.web_view)















