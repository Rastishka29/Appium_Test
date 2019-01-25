from page_objects.base_page import BasePage
from locators.base_locators import BaseLocators


class HomePage(BasePage):

    def open_alert_page(self):
        self.find_element(*BaseLocators.alert_views).click()

    def open_text_entry(self):
        self.find_element(*BaseLocators.text_entry).click()

    def submit_text_entry(self, message):
        self.find_element(*BaseLocators.text_field).send_keys(message)
        self.find_element(*BaseLocators.ok_btn).click()

    def is_text_field_displayed(self):
        return self.find_element(*BaseLocators.text_field).is_displayed()










