from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_open_google(driver_safari_sauce_lab):
    wait = WebDriverWait(driver_safari_sauce_lab, 60)

    driver_safari_sauce_lab.get("https://gmail.com")
    # wait.until(EC.visibility_of_element_located((
    #     By.CSS_SELECTOR, "body > nav > div > a.gmail-nav__nav-link.gmail-nav__nav-link__sign-in"))).click()
    wait.until(EC.visibility_of_element_located((
        By.CSS_SELECTOR, "#identifierId"))).send_keys("test_user2@gmail.com")
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#identifierNext > content > span"))).click()
    actual = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.GQ8Pzc'))).text
    assert actual == "Couldn't find your Google Account"
