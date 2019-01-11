import unittest
import os
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class BaseTest(unittest.TestCase):
    def setUp(self):
        app = os.path.join(os.path.dirname(__file__),
                           '/Users/ykon/Library/Developer/Xcode/DerivedData/UICatalog-cbyqlluuqdtgqvgfqcnluofyvutg/',
                           'Build/Products/Debug-iphonesimulator/UICatalog.app')
        app = os.path.abspath(app)
        # Set up appium
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                "automationName": "XCUITest",
                'platformName': 'iOS',
                'platformVersion': '12.1',
                'deviceName': 'iPhone XS',
                'bundleId': 'com.example.apple-samplecode.UICatalog',
                'noReset': True
            })

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(BaseTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
