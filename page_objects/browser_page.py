from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.browser_locators import BrowserLocators


class BrowserPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_page(self, url):
        self.driver.get(url)

    def enter_email_and_submit(self, email):
        self.wait.until(EC.visibility_of_element_located(BrowserLocators.email_field)).send_keys(email)
        self.wait.until(EC.visibility_of_element_located(BrowserLocators.button)).click()

    def get_error_message(self):
        return self.wait.until(EC.visibility_of_element_located(BrowserLocators.error_message)).text