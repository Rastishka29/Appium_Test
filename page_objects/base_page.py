
class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        if locator.__len__() == 2:
            return self.driver.find_element(*locator)
        return self.driver.find_element(*(locator[1], locator[2] % locator[0]))

    def find_elements(self, *locator):
        if locator.__len__() == 2:
            return self.driver.find_elements(*locator)
        return self.driver.find_elements(*(locator[1], locator[2] % locator[0]))

    def open_page(self, name):
        self.driver.find_element_by_name(name).click()

    def scroll_by_name(self, name):
        self.driver.execute_script('mobile: scroll', {'name': name})

    def scroll_by_direction(self, direction):
        self.driver.execute_script('mobile: scroll', {'direction': direction})

    def is_elem_displayed(self, *el):
        return self.find_element(*el).is_displayed()

    def is_text_displayed(self, text):
        return self.driver.find_element_by_name(text).is_displayed()

    def go_back(self):
        self.driver.back()



