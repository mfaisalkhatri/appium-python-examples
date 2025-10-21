import os.path

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.fixture(scope="function")
def driver():
    apk_path = os.path.abspath('./src/test/resources/android.wdio.native.app.v1.0.8.apk')
    options = UiAutomator2Options().load_capabilities({
        'platformName':'Android',
        'automationName':'uiautomator2',
        'deviceName':'Pixel 6 API 34',
        'app':apk_path
    })

    driver = webdriver.Remote("http://localhost:4723", options=options)
    yield driver

    driver.quit()


def test_login_flow(driver):
    wait = WebDriverWait(driver, 20)

    login_button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Login")')
    login_button.click()

    email_field = wait.until(ec.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID,"input-email")))
    email_field.send_keys("faisalk@gmail.com")

    password_field = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "input-password")
    password_field.send_keys("password123")

    login_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "button-LOGIN")
    login_button.click()

    alert_title = wait.until(ec.presence_of_element_located((AppiumBy.ID, "android:id/alertTitle")))
    assert alert_title.is_displayed(), "Success"

    print("✅ Login test passed successfully!")