import unittest
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SafariTest(unittest.TestCase):
    def setUp(self):
        # Set up appium
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'browserName': 'Safari',
                'automationName': 'XCUITest',
                'platformName': 'iOS',
                'platformVersion': '12.1',
                'deviceName': 'iPhone XS',
                'noReset': True
            })

    def tearDown(self):
        self.driver.quit()

    def test_open_google(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        driver.get("https://gmail.com")
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > nav > div > a.gmail-nav__nav-link.gmail-nav__nav-link__sign-in"))).click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#identifierId"))).send_keys("test_user2@gmail.com")
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#identifierNext > content > span"))).click()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SafariTest)
    unittest.TextTestRunner(verbosity=2).run(suite)