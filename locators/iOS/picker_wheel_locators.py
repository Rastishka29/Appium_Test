from appium.webdriver.common.mobileby import MobileBy
from locators.iOS.home_page_locators import HomePageLocators


class PickerWheelLocators(HomePageLocators):
    red_wheel = (MobileBy.NAME, "Red color component value")
    green_wheel = (MobileBy.CLASS_NAME, "XCUIElementTypePickerWheel")
    blue_wheel = (MobileBy.XPATH, "//*[@name='Blue color component value']")
