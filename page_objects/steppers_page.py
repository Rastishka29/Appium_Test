from locators.stepper_locators import SteppersLocators
from page_objects.base_page import BasePage


class SteppersPage(BasePage):
    def increment_counter_twice(self):
        self.find_elements(*SteppersLocators.increment).pop(1).click()
        self.find_elements(*SteppersLocators.increment).pop(1).click()

    def counter_value(self):
        return int(self.find_elements(*SteppersLocators.counter).pop(2).text)

    def get_custom_text(self):
        return self.find_element(*SteppersLocators.title).get_attribute(name='name')
