from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support import expected_conditions as EC
import time
import os

desired_caps = {
    "lt:options": {
    "deviceName": "Galaxy S20",
    "platformName": "Android",
    "platformVersion": "10",
    "app": "lt://APP10160341071754500059009313",
    "isRealMobile": True,
    "build": "Python Vanilla Android",
    "name": "Sample Test - Python",
    "network": False,
    "visual": True,
    "video": True
}
}


def startingTest():
    global driver
    if os.environ.get("LT_USERNAME") is None:
        username = "username" #Add username here
    else:
        username = os.environ.get("LT_USERNAME")
    if os.environ.get("LT_ACCESS_KEY") is None:
        accesskey = "accesskey" #Add accessKey here
    else:
        accesskey = os.environ.get("LT_ACCESS_KEY")

    try:
        driver = webdriver.Remote("https://" +
                                  username+":"+accesskey+"@mobile-hub.lambdatest.com/wd/hub",
                                  options=UiAutomator2Options().load_capabilities(desired_caps))

        color_element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (AppiumBy.ID, "com.lambdatest.proverbial:id/color")))
        color_element.click()

        text_element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((AppiumBy.ID, "com.lambdatest.proverbial:id/Text")))
        text_element.click()

        toast_element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (AppiumBy.ID, "com.lambdatest.proverbial:id/toast")))
        toast_element.click()

        notification = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (AppiumBy.ID, "com.lambdatest.proverbial:id/notification")))
        notification.click()

        geolocation = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (AppiumBy.ID, "com.lambdatest.proverbial:id/geoLocation")))
        geolocation.click()
        time.sleep(5)

        driver.back()

        home = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (AppiumBy.ID, "com.lambdatest.proverbial:id/buttonPage")))
        home.click()

        speed_test = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (AppiumBy.ID, "com.lambdatest.proverbial:id/speedTest")))
        speed_test.click()
        time.sleep(5)

        driver.back()

        browser = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (AppiumBy.ID, "com.lambdatest.proverbial:id/webview")))
        browser.click()

        url = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (AppiumBy.ID, "com.lambdatest.proverbial:id/url")))
        url.send_keys("https://www.lambdatest.com")

        find = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (AppiumBy.ID, "com.lambdatest.proverbial:id/find")))
        find.click()
        driver.quit()
    except:
        driver.quit()


startingTest()