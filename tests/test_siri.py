"""
Practicing automating tests using Siri voice assistant
"""

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_hello_siri(driver_app):
    wait = WebDriverWait(driver_app, 10)

    # Trigger "Hey Siri" voice message
    driver_app.execute_script('mobile: siriCommand', {'text': 'Hey Siri'})
    # Explicitly waiting for the message 'Hey Siri' to appear on the screen
    actual_result = wait.until(EC.visibility_of_element_located((By.NAME, 'Hey Siri'))).text
    # Verify that text "Hey Siri" on the screen is as expected
    assert 'Hey Siri' == actual_result


def test_siri_call_contact(driver_app):
    wait = WebDriverWait(driver_app, 10)

    driver_app.execute_script('mobile: siriCommand', {'text': 'Call Kate Bell'})
    wait.until(EC.presence_of_element_located((By.NAME, "Which phone number for Kate Bell?")))
    driver_app.execute_script('mobile: siriCommand', {'text': 'mobile'})
    actual_result = wait.until(EC.presence_of_element_located((
            By.NAME, "I can’t make phone calls for you on this device, but I can make a FaceTime call."))).text

    assert "I can’t make phone calls for you on this device, but I can make a FaceTime call." == actual_result


def test_siri_call_number(driver_app):
    wait = WebDriverWait(driver_app, 10)

    driver_app.execute_script('mobile: siriCommand', {'text': 'Call by number'})
    wait.until(EC.presence_of_element_located((By.NAME, "Who do you want to call?")))
    driver_app.execute_script('mobile: siriCommand', {'text': '5555648583'})
    actual_result = wait.until(EC.presence_of_element_located((
        By.NAME, "I can’t make phone calls for you on this device, but I can make a FaceTime call."))).text
    assert "I can’t make phone calls for you on this device, but I can make a FaceTime call." == actual_result
