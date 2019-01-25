
class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        if locator.__len__() == 2:
            return self.driver.find_element(*locator)
        return self.driver.find_element(*(locator[1], locator[2] % locator[0]))



