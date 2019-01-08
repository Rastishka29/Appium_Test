import unittest
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from tests.base_test import BaseTest


class SiriTest(BaseTest):

    def test_hello_siri(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        # Trigger "Hey Siri" voice message
        driver.execute_script('mobile: siriCommand', {'text': 'Hey Siri'})
        # Explicitly waiting for the message 'Hey Siri' to appear on the screen
        actual_result = wait.until(EC.visibility_of_element_located((By.NAME, 'Hey Siri'))).text
        # Verify that text "Hey Siri" on the screen is as expected
        self.assertEqual('Hey Siri', actual_result)

    def test_siri_call_contact(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        driver.execute_script('mobile: siriCommand', {'text': 'Call Kate Bell'})
        wait.until(EC.presence_of_element_located((By.NAME, "Which phone number for Kate Bell?")))
        driver.execute_script('mobile: siriCommand', {'text': 'mobile'})
        actual_result = wait.until(EC.presence_of_element_located((
                By.NAME, "I can’t make phone calls for you on this device, but I can make a FaceTime call."))).text

        self.assertEqual("I can’t make phone calls for you on this device, but I can make a FaceTime call.",
                         actual_result)

    def test_siri_call_number(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        driver.execute_script('mobile: siriCommand', {'text': 'Call by number'})
        wait.until(EC.presence_of_element_located((By.NAME, "Who do you want to call?")))
        driver.execute_script('mobile: siriCommand', {'text': '5555648583'})
        actual_result = wait.until(EC.presence_of_element_located((
            By.NAME, "I can’t make phone calls for you on this device, but I can make a FaceTime call."))).text
        self.assertEqual("I can’t make phone calls for you on this device, but I can make a FaceTime call.",
                         actual_result)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SiriTest)
    unittest.TextTestRunner(verbosity=2).run(suite)