from locators.picker_wheel_locators import PickerWheelLocators
from page_objects.base_page import BasePage


class PickerWheelPage(BasePage):
    def set_red_wheel_value(self, value):
        self.find_element(*PickerWheelLocators.red_wheel).send_keys(value)

    def get_red_wheel_value(self):
        return self.find_element(*PickerWheelLocators.red_wheel).text

    def set_green_wheel_value(self, value):
        self.find_elements(*PickerWheelLocators.green_wheel).pop(1).send_keys(value)

    def get_green_wheel_value(self):
        return self.find_elements(*PickerWheelLocators.green_wheel).pop(1).text

    def set_blue_wheel_value(self, value):
        self.find_element(*PickerWheelLocators.blue_wheel).send_keys(value)

    def get_blue_wheel_value(self):
        return self.find_element(*PickerWheelLocators.blue_wheel).text
