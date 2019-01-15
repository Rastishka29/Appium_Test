"""
Practicing automating different common mobile interactions
"""


def test_send_keys(driver_app):
    driver_app.find_element_by_accessibility_id("Alert Views").click()
    driver_app.find_element_by_xpath("//*[@value='Text Entry']").click()
    text_field = driver_app.find_element_by_class_name("XCUIElementTypeOther")
    text_field.send_keys('Hello')
    driver_app.find_element_by_name("OK").click()

    assert text_field.is_displayed() is not True, "Text field is still displayed after submit"
    driver_app.back()


def test_scrolling(driver_app):
    driver_app.execute_script('mobile: scroll', {'name': "Toolbars"})
    driver_app.find_element_by_name("Toolbars").click()

    assert driver_app.find_element_by_name("Toolbars").is_displayed(), "'Toolbars' title is not displayed"
    driver_app.back()

    driver_app.execute_script('mobile: scroll', {'direction': 'up'})
    driver_app.find_element_by_name("Action Sheets").click()

    assert driver_app.find_element_by_name("Action Sheets").is_displayed(), "'Action Sheets' title is not displayed"
    driver_app.back()

    driver_app.execute_script('mobile: scroll', {'direction': 'down'})
    driver_app.find_element_by_name("Web View").click()

    assert driver_app.find_element_by_name("Web View").is_displayed(), "'Web View' title is not displayed"
    driver_app.back()


def test_increment(driver_app):
    driver_app.find_element_by_name("Steppers").click()
    driver_app.find_elements_by_name("Increment").pop(1).click()
    driver_app.find_elements_by_name("Increment").pop(1).click()
    counter = driver_app.find_elements_by_class_name("XCUIElementTypeStaticText").pop(2).text

    assert 2 == int(counter), "Increment counter is not correct"
    driver_app.back()


def test_find_element(driver_app):
    driver_app.find_element_by_name("Steppers").click()
    actual = driver_app.find_element_by_name("CUSTOM").get_attribute(name='name')

    assert "CUSTOM" == actual, "'Custom' text is not displayed"
    driver_app.back()


def test_picker_wheel(driver_app):
    driver_app.find_element_by_accessibility_id("Picker View").click()
    red_wheel = driver_app.find_element_by_name("Red color component value")
    red_wheel.send_keys("0")
    assert red_wheel.text == "0", "Incorrect red wheel value"

    green_wheel = driver_app.find_elements_by_class_name("XCUIElementTypePickerWheel").pop(1)
    green_wheel.send_keys("255")
    assert green_wheel.text == "255", "Incorrect green wheel value"

    blue_wheel = driver_app.find_element_by_xpath("//*[@name='Blue color component value']")
    blue_wheel.send_keys("45")
    assert blue_wheel.text == "45", "Incorrect blue wheel value"
    driver_app.back()
