"""
Practicing automating different common mobile interactions
"""

import unittest
from tests.base_test import BaseTest


class UiCatalog(BaseTest):

    def test_send_keys(self):
        driver = self.driver

        driver.find_element_by_accessibility_id("Alert Views").click()
        driver.find_element_by_xpath("//*[@value='Text Entry']").click()
        driver.find_element_by_class_name("XCUIElementTypeOther").send_keys('Hello')
        driver.find_element_by_name("OK").click()

    def test_scrolling(self):
        driver = self.driver

        driver.execute_script('mobile: scroll', {'name': "Toolbars"})
        driver.find_element_by_name("Toolbars").click()
        driver.back()

        driver.execute_script('mobile: scroll', {'direction': 'up'})
        driver.find_element_by_name("Action Sheets").click()
        driver.back()

        driver.execute_script('mobile: scroll', {'direction': 'down'})
        driver.find_element_by_name("Web View").click()
        driver.back()

    def test_increment(self):
        driver = self.driver

        driver.find_element_by_name("Steppers").click()
        driver.find_elements_by_name("Increment").pop(1).click()
        driver.find_elements_by_name("Increment").pop(1).click()

        counter = driver.find_elements_by_class_name("XCUIElementTypeStaticText").pop(2).text
        self.assertEqual(2, int(counter))

    def test_find_element(self):
        driver = self.driver

        driver.find_element_by_name("Steppers").click()
        actual = driver.find_element_by_name("CUSTOM").get_attribute(name='name')
        self.assertEqual("CUSTOM", actual)

    def test_picker_wheel(self):
        driver = self.driver

        driver.find_element_by_accessibility_id("Picker View").click()
        driver.find_element_by_name("Red color component value").send_keys("0")
        driver.find_elements_by_class_name("XCUIElementTypePickerWheel").pop(1).send_keys("255")
        driver.find_element_by_xpath("//*[@name='Blue color component value']").send_keys("45")




if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(UiCatalog)
    unittest.TextTestRunner(verbosity=2).run(suite)