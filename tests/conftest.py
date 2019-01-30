"""
This is file with fixtures for running preconditions and postconditions for our tests with different configurations.
"""

import pytest
from appium import webdriver
import os
from selenium.webdriver.support.wait import WebDriverWait


# Fixture for autotests for browser Safari in iOS
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
            #'noReset': True
        })
    yield driver
    driver.quit()

# Fixture for autotests for Chrome in Android
@pytest.fixture(scope='module', autouse=False)
def driver_chrome():
    # Set up appium
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723/wd/hub',
        desired_capabilities={
            'browserName': 'Chrome',
            'platformName': 'Android',
            'platformVersion': '8.1',
            'deviceName': 'Pixel 2',
            #'noReset': True
        })
    yield driver
    driver.quit()


# Fixture for autotests which are running in app for iOS
@pytest.fixture(scope='module', autouse=False)
def driver_ios_app():
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
            #'noReset': True
        })
    yield driver
    driver.quit()


# Fixture for autotests which are running in app for Android
@pytest.fixture(scope='module', autouse=False)
def driver_android_app():
    app = os.path.join(os.path.dirname(__file__),
                       '/Users/ykon/Education/Appium/Appium_Test_Project/ApiDemos-debug.apk')
    app = os.path.abspath(app)
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723/wd/hub',
        desired_capabilities={
            'app': app,
            'platformName': 'Android',
            'platformVersion': '8.1',
            'deviceName': 'Pixel 2'
        })
    yield driver
    driver.quit()

# Below is fixture with capabilities for running tests in cloud using saucelabs tool for mobile browser.
# However, I will not use it right now for my tests because I have only trial subscription for saucelabs and tests
# on cloud are running noticable slower.


@pytest.fixture()
def driver_safari_sauce_lab():
    # Set up appium
    driver = webdriver.Remote(
        command_executor='http://rastishka29:bd8c0275-e0ed-4adf-b5a5-50f618fac4ba@ondemand.saucelabs.com:80/wd/hub',
        desired_capabilities={
            'browserName': 'Safari',
            'automationName': 'XCUITest',
            'appiumVersion': '1.9.1',
            'name': 'Safari Test',
            'platformName': 'iOS',
            'platformVersion': '12.0',
            'deviceName': 'iPhone XS',
            'deviceOrientation': 'portrait',
            #'noReset': True
        })
    yield driver
    driver.quit()


# Below is fixture with capabilities for running tests in cloud using saucelabs tool for mobile app.
# However, I will not use it right now for my tests because I have only trial subscription for saucelabs and tests
# on cloud are running noticable slower.
# Also app should be loaded somewhere on cloud like aws or on
# temporary on saucelab cloud https://wiki.saucelabs.com/display/DOCS/Temporary+Storage+Methods.


@pytest.fixture()
def driver_safari_sauce_lab_app():
    # Set up appium
    driver = webdriver.Remote(
        command_executor='http://rastishka29:bd8c0275-e0ed-4adf-b5a5-50f618fac4ba@ondemand.saucelabs.com:80/wd/hub',
        desired_capabilities={
            'app':'sauce-storage:"name-of-the-app-in-zip-archive-posted-somewhere"',
            'automationName': 'XCUITest',
            'appiumVersion': '1.9.1',
            'name': 'Safari Test',
            'platformName': 'iOS',
            'platformVersion': '12.0',
            'deviceName': 'iPhone XS',
            'deviceOrientation': 'portrait',
            #'noReset': True
        })
    yield driver
    driver.quit()

# Below is fixture for using real iOS devices for tests. Unfortunately I can't practice creating test on real
# iOS devices, because I don't have a "xcodeOrgId" which is Team Id.
# It can be available only when purchasing a membership at Apple Developer Program.


@pytest.fixture()
def driver_real_device():
    app = os.path.join(os.path.dirname(__file__),
                       '/Users/ykon/Library/Developer/Xcode/DerivedData/UICatalog-cbyqlluuqdtgqvgfqcnluofyvutg/',
                       'Build/Products/Debug-iphonesimulator/UICatalog.app')
    app = os.path.abspath(app)
    # Set up appium
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723/wd/hub',
        desired_capabilities={
            'app': app,
            "automationName": "XCUITest",
            'platformName': 'iOS',
            'platformVersion': '12.1',
            'deviceName': 'iPhone XS',
            'bundleId': 'com.example.apple-samplecode.UICatalog',
            #'noReset': True,
            "xcodeOrgId": "<Team ID>",
            "xcodeSigningId": "iPhone Developer"
            #"udid":
            #"updateWDABundleId":
        })
    yield driver
    driver.quit()
