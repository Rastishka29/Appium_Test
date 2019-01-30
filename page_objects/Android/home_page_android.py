from page_objects.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from locators.Android.home_page_locators_android import HomePageLocatorsAndroid


class HomePageAndroid(BasePage):
    def open_date_widgets_dialog(self):
        self.find_element(*HomePageLocatorsAndroid.views).click()
        self.wait.until(EC.visibility_of_element_located(HomePageLocatorsAndroid.date_widgets)).click()
        self.wait.until(EC.visibility_of_element_located(HomePageLocatorsAndroid.dialog)).click()

    def change_date(self):
        self.wait.until(EC.visibility_of_element_located(HomePageLocatorsAndroid.change_date_btn)).click()
        self.wait.until(EC.visibility_of_element_located(HomePageLocatorsAndroid.tomorrow_day)).click()
        self.wait.until(EC.visibility_of_element_located(HomePageLocatorsAndroid.ok_btn)).click()

    def get_date(self):
        date = self.wait.until((EC.visibility_of_all_elements_located(HomePageLocatorsAndroid.new_date))).pop(1).text
        return date.split('-')[1]



