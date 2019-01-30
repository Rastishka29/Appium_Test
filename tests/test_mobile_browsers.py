"""
Practicing automation tests using Safari browser and in Chrome browser.
Tests below are using the same page objects and locators, only different capabilities for iOS and Android respectively.
"""

from page_objects.browser_page import BrowserPage


def test_open_google_in_safari(driver_safari):
    page = BrowserPage(driver_safari)
    page.open_page("https://gmail.com")
    page.enter_email_and_submit("test_user2@gmail.com")
    assert page.get_error_message() == "Couldn't find your Google Account"


def test_open_google_in_chrome(driver_chrome):
    page = BrowserPage(driver_chrome)
    page.open_page("https://gmail.com")
    page.enter_email_and_submit("test_user2@gmail.com")
    assert page.get_error_message() == "Couldn't find your Google Account"