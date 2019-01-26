from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.siri_locators import SiriLocators


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

    def scroll_by_name(self, name):
        self.driver.execute_script('mobile: scroll', {'name': name})

    def scroll_by_direction(self, direction):
        self.driver.execute_script('mobile: scroll', {'direction': direction})

    def is_elem_displayed(self, *el):
        return self.find_element(*el).is_displayed()

    def is_text_displayed(self, text):
        return self.driver.find_element_by_name(text).is_displayed()

    def go_back(self):
        self.driver.back()

    def hey_siri_command(self, message):
        self.driver.execute_script('mobile: siriCommand', {'text': message})

    def get_hey_siri_text(self):
        return self.get_text(*SiriLocators.hey_siri)

    def call_siri_by_contact(self, message):
        self.hey_siri_command(message)
        self.wait.until(EC.presence_of_element_located(SiriLocators.which_number))
        self.hey_siri_command("mobile")

    def call_siri_by_number(self, message, number):
        self.hey_siri_command(message)
        self.wait.until(EC.presence_of_element_located(SiriLocators.who_to_call_message))
        self.hey_siri_command(number)

    def get_siri_error_message(self):
        return self.wait.until(EC.presence_of_element_located(SiriLocators.error_cant_make_call)).text






