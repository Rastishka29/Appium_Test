from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from locators.iOS.siri_locators import SiriLocators


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, *locator):
        if locator.__len__() == 2:
            return self.driver.find_element(*locator)
        return self.driver.find_element(*(locator[1], locator[2] % locator[0]))

    def find_elements(self, *locator):
        if locator.__len__() == 2:
            return self.driver.find_elements(*locator)
        return self.driver.find_elements(*(locator[1], locator[2] % locator[0]))

    def open_page(self, name):
        self.driver.find_element_by_name(name).click()

    def get_text(self, *el):
        return self.find_element(*el).text

    def is_elem_displayed(self, *el):
        return self.find_element(*el).is_displayed()

    def is_text_displayed(self, text):
        return self.driver.find_element_by_name(text).is_displayed()

    def go_back(self):
        self.driver.back()

    def tap(self, el):
        action = TouchAction(self.driver)
        action.tap(el).perform()

# iOS specific methods:

    def scroll_by_name_ios(self, name):
        self.driver.execute_script('mobile: scroll', {'name': name})

    def scroll_by_direction_ios(self, direction):
        self.driver.execute_script('mobile: scroll', {'direction': direction})

    def hey_siri_command_ios(self, message):
        self.driver.execute_script('mobile: siriCommand', {'text': message})

    def get_hey_siri_text_ios(self):
        return self.get_text(*SiriLocators.hey_siri)

    def call_siri_by_contact_ios(self, message):
        self.hey_siri_command_ios(message)
        self.wait.until(EC.presence_of_element_located(SiriLocators.which_number))
        self.hey_siri_command_ios("mobile")

    def call_siri_by_number_ios(self, message, number):
        self.hey_siri_command_ios(message)
        self.wait.until(EC.presence_of_element_located(SiriLocators.who_to_call_message))
        self.hey_siri_command_ios(number)

    def get_siri_error_message_ios(self):
        return self.wait.until(EC.presence_of_element_located(SiriLocators.error_cant_make_call)).text

# Android specific methods:

    def scroll_by_coordinates_android(self,start_x, start_y, end_x, end_y, duration):
        # Somehow I couldn't managed to make a scroll using Touchaction, so I used driver.swipe instead
        # action = TouchAction(self.driver)
        # action.press(els[0]).wait(500).move_to(els[12]).release().perform()
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)










