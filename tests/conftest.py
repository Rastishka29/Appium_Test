"""
This is file with fixtures for running preconditions and postconditions for our tests.
"""

import pytest
from appium import webdriver
import os
from selenium.webdriver.support.wait import WebDriverWait


# Fixture for autotests which are running in browser Safari
@pytest.fixture(scope='module', autouse=False)
def driver_safari():
    # Set up appium
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723/wd/hub',
        desired_capabilities={
            'browserName': 'Safari',
            'automationName': 'XCUITest',
            'platformName': 'iOS',
            'platformVersion': '12.1',
            'deviceName': 'iPhone XS',
            'noReset': True
        })
    yield driver
    driver.quit()


# Fixture for autotests which are running in app
@pytest.fixture(scope='module', autouse=True)
def driver_app():
    app = os.path.join(os.path.dirname(__file__),
                       '/Users/ykon/Library/Developer/Xcode/DerivedData/UICatalog-cbyqlluuqdtgqvgfqcnluofyvutg/'
                       'Build/Products/Debug-iphonesimulator/UICatalog.app')
    app = os.path.abspath(app)
    driver = webdriver.Remote(
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
    wait = WebDriverWait(driver, 10)
    yield driver
    driver.quit()


"""
Unfortunately I can't practice creating test on real iOS devices, because I don't have a "xcodeOrgId" which is Team Id.
It can be available only when purchasing a membership at Apple Developer Program.
"""

# @pytest.fixture()
# def driver_real_device(self):
#     app = os.path.join(os.path.dirname(__file__),
#                        '/Users/ykon/Library/Developer/Xcode/DerivedData/UICatalog-cbyqlluuqdtgqvgfqcnluofyvutg/',
#                        'Build/Products/Debug-iphonesimulator/UICatalog.app')
#     app = os.path.abspath(app)
#     # Set up appium
#     driver = webdriver.Remote(
#         command_executor='http://127.0.0.1:4723/wd/hub',
#         desired_capabilities={
#             'app': app,
#             "automationName": "XCUITest",
#             'platformName': 'iOS',
#             'platformVersion': '12.1',
#             'deviceName': 'iPhone XS',
#             'bundleId': 'com.example.apple-samplecode.UICatalog',
#             'noReset': True
#             "xcodeOrgId": "<Team ID>",
#             "xcodeSigningId": "iPhone Developer"
#             "udid":
#             "updateWDABundleId":
#         })
