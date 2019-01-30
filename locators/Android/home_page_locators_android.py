from appium.webdriver.common.mobileby import MobileBy
import datetime


class HomePageLocatorsAndroid(object):
    views = (MobileBy.XPATH, "//android.widget.TextView[@text='Views']")
    date_widgets = (MobileBy.XPATH, "//android.widget.TextView[@text='Date Widgets']")
    dialog = (MobileBy.XPATH, "//android.widget.TextView[@text='1. Dialog']")
    change_date_btn = (MobileBy.XPATH, "//android.widget.Button[@text='CHANGE THE DATE']")
    tomorrow_xpath = "//android.view.View[@text='" + str(datetime.date.today() + datetime.timedelta(days=1))[8:] + "']"
    tomorrow_day = (MobileBy.XPATH, tomorrow_xpath)
    ok_btn = (MobileBy.XPATH, "//android.widget.Button[@text='OK']")
    new_date = (MobileBy.XPATH, "//android.widget.TextView[@index='0']")