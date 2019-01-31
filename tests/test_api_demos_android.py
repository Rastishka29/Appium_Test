"""
Practicing automating different common mobile interactions in test app on Android
"""
from page_objects.Android.home_page_android import HomePageAndroid
import datetime


def test_change_date(driver_android_app):
    page = HomePageAndroid(driver_android_app)
    page.open_date_widgets_dialog()
    page.change_date()
    # Validating that changed date is tomorrow date:
    assert page.get_date() == str(datetime.date.today() + datetime.timedelta(days=1))[8:]


def test_scrolling(driver_android_app):
    page = HomePageAndroid(driver_android_app)
    page.scroll_and_open_web_view()
    assert page.get_web_view_title() == "Views/WebView"

