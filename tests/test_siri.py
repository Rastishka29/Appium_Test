"""
Practicing automating tests using Siri voice assistant
"""

from page_objects.base_page import BasePage


def test_hello_siri(driver_app):
    page = BasePage(driver_app)
    # Trigger "Hey Siri" voice message
    page.hey_siri_command("Hey Siri")
    assert page.get_hey_siri_text() == 'Hey Siri'


def test_siri_call_contact(driver_app):
    page = BasePage(driver_app)
    page.call_siri_by_contact("Call Kate Bell")
    assert page.get_siri_error_message() == "I can’t make phone calls for you on this device," \
                                            " but I can make a FaceTime call."


def test_siri_call_number(driver_app):
    page = BasePage(driver_app)
    page.call_siri_by_number("Call by number", "5555648583")

    assert page.get_siri_error_message() == "I can’t make phone calls for you on this device, " \
                                            "but I can make a FaceTime call."
