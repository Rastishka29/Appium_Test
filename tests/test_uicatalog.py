"""
Practicing automating different common mobile interactions
"""
from page_objects.home_page import HomePage
from page_objects.picker_wheel_page import PickerWheelPage
from page_objects.steppers_page import SteppersPage


def test_send_keys(driver_app):
    page = HomePage(driver_app)
    page.open_page("Alert Views")
    page.open_text_entry()
    page.submit_text_entry('SmartAss')

    assert page.is_text_field_displayed() is not True, "Text field pop up is still displayed after submit"
    driver_app.back()


def test_scrolling(driver_app):
    page = HomePage(driver_app)
    page.scroll_and_open_toolbars()
    assert page.is_toolbars_title_displayed(), "'Toolbars' title is not displayed"
    page.go_back()

    page.scroll_up_and_open_action_sheets()
    assert page.is_action_sheets_title_displayed(), "'Action Sheets' title is not displayed"
    page.go_back()

    page.scroll_down_and_open_web_view()
    assert page.is_web_view_title_displayed(), "'Web View' title is not displayed"
    page.go_back()


def test_increment(driver_app):
    page = SteppersPage(driver_app)
    page.open_page("Steppers")
    page.increment_counter_twice()
    assert page.counter_value() == 2, "Increment counter is not correct"
    page.go_back()


def test_find_element(driver_app):
    page = SteppersPage(driver_app)
    page.open_page("Steppers")

    assert page.get_custom_text() == "CUSTOM", "'Custom' text is not displayed"
    page.go_back()


def test_picker_wheel(driver_app):
    page = PickerWheelPage(driver_app)
    page.open_page("Picker View")
    page.set_red_wheel_value("0")
    assert page.get_red_wheel_value() == "0", "Incorrect red wheel value"

    page.set_green_wheel_value("255")
    assert page.get_green_wheel_value() == "255", "Incorrect green wheel value"

    page.set_blue_wheel_value("45")
    assert page.get_blue_wheel_value() == "45", "Incorrect blue wheel value"
    driver_app.back()
