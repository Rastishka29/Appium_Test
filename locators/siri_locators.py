from appium.webdriver.common.mobileby import MobileBy

from locators.base_locators import HomePageLocators


class SiriLocators(HomePageLocators):
    hey_siri = (MobileBy.NAME, "Hey Siri")
    which_number = (MobileBy.NAME, "Which phone number for Kate Bell?")
    error_cant_make_call = (MobileBy.NAME,
                            "I can’t make phone calls for you on this device, but I can make a FaceTime call.")
    who_to_call_message = (MobileBy.NAME, "Who do you want to call?")