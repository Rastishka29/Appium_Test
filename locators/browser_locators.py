from selenium.webdriver.common.by import By


class BrowserLocators(object):
    email_field = (By.CSS_SELECTOR, "#identifierId")
    button = (By.CSS_SELECTOR, "#identifierNext > content > span")
    error_message = (By.CSS_SELECTOR, ".GQ8Pzc")