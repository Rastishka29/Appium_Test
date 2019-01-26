"""
Practicing automation tests using Safari browser
"""

from page_objects.browser_page import BrowserPage


def test_open_google(driver_safari):
    page = BrowserPage(driver_safari)
    page.open_page("https://gmail.com")
    page.enter_email_and_submit("test_user2@gmail.com")
    assert page.get_error_message() == "Couldn't find your Google Account"
