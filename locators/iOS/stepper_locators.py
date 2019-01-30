from appium.webdriver.common.mobileby import MobileBy
from locators.iOS.home_page_locators import HomePageLocators


class SteppersLocators(HomePageLocators):
    increment = (MobileBy.NAME, "Increment")
    counter = (MobileBy.CLASS_NAME, "XCUIElementTypeStaticText")
    title = (MobileBy.NAME, "CUSTOM")
