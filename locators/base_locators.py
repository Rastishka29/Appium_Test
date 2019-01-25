from appium.webdriver.common.mobileby import MobileBy


class BaseLocators(object):
    alert_views = (MobileBy.ACCESSIBILITY_ID, "Alert Views")
    text_entry = (MobileBy.XPATH, "//*[@value='Text Entry']")
    text_field = (MobileBy.CLASS_NAME, "XCUIElementTypeOther")
    ok_btn = (MobileBy.NAME, "OK")
    toolbars = (MobileBy.NAME, "Toolbars")
    action_sheets = (MobileBy.NAME, "Action Sheets")
    web_view = (MobileBy.NAME, "Web View")
