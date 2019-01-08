"""
Unfortunately I can't practice creating test on real iOS devices, because I don't have a "xcodeOrgId" which is Team Id.
It can be available only when purchasing a membership at Apple Developer Program.
"""
# import unittest
# import os
# from appium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.common.by import By
#
#
# class RealDeviceBaseTest(unittest.TestCase):
#     def setUp(self):
        # app = os.path.join(os.path.dirname(__file__),
        #                    '/Users/ykon/Library/Developer/Xcode/DerivedData/UICatalog-cbyqlluuqdtgqvgfqcnluofyvutg/',
        #                    'Build/Products/Debug-iphonesimulator/UICatalog.app')
        # app = os.path.abspath(app)
        # # Set up appium
        # self.driver = webdriver.Remote(
        #     command_executor='http://127.0.0.1:4723/wd/hub',
        #     desired_capabilities={
        #         'app': app,
        #         "automationName": "XCUITest",
        #         'platformName': 'iOS',
        #         'platformVersion': '12.1',
        #         'deviceName': 'iPhone XS',
        #         'bundleId': 'com.example.apple-samplecode.UICatalog',
        #         'noReset': True
        #         "xcodeOrgId": "<Team ID>",
        #         "xcodeSigningId": "iPhone Developer"
        #         "udid":
        #         "updateWDABundleId":
        #     })