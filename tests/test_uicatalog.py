"""
Practicing automating different common mobile interactions
"""


def test_send_keys(driver_app):
    driver_app.find_element_by_accessibility_id("Alert Views").click()
    driver_app.find_element_by_xpath("//*[@value='Text Entry']").click()
    driver_app.find_element_by_class_name("XCUIElementTypeOther").send_keys('Hello')
    driver_app.find_element_by_name("OK").click()
    driver_app.back()


def test_scrolling(driver_app):
    driver_app.execute_script('mobile: scroll', {'name': "Toolbars"})
    driver_app.find_element_by_name("Toolbars").click()
    driver_app.back()

    driver_app.execute_script('mobile: scroll', {'direction': 'up'})
    driver_app.find_element_by_name("Action Sheets").click()
    driver_app.back()

    driver_app.execute_script('mobile: scroll', {'direction': 'down'})
    driver_app.find_element_by_name("Web View").click()
    driver_app.back()


def test_increment(driver_app):
    driver_app.find_element_by_name("Steppers").click()
    driver_app.find_elements_by_name("Increment").pop(1).click()
    driver_app.find_elements_by_name("Increment").pop(1).click()
    counter = driver_app.find_elements_by_class_name("XCUIElementTypeStaticText").pop(2).text
    assert 2 == int(counter)
    driver_app.back()


def test_find_element(driver_app):
    driver_app.find_element_by_name("Steppers").click()
    actual = driver_app.find_element_by_name("CUSTOM").get_attribute(name='name')
    assert "CUSTOM" == actual
    driver_app.back()


def test_picker_wheel(driver_app):
    driver_app.find_element_by_accessibility_id("Picker View").click()
    driver_app.find_element_by_name("Red color component value").send_keys("0")
    driver_app.find_elements_by_class_name("XCUIElementTypePickerWheel").pop(1).send_keys("255")
    driver_app.find_element_by_xpath("//*[@name='Blue color component value']").send_keys("45")
    driver_app.back()
