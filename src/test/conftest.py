import os
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from src.test.resources.devices import ANDROID_DEVICES

def finalize_driver(request, driver):
    def fin():
        if request.node.rep_call.failed:
            driver.execute_script('lambda-status=failed')
        else:
            driver.execute_script('lambda-status=passed')
        driver.quit()
    request.addfinalizer(fin)

def pytest_generate_tests(metafunc):
    if 'device_config' in metafunc.fixturenames:
        metafunc.parametrize('device_config', ANDROID_DEVICES, ids= lambda d: d['deviceName'])

@pytest.fixture(scope='function')
def test_setup_android(request, device_config):
    test_name = request.node.name

    caps = {
        "lt:options": {
            "w3c": True,
            "platformName": "Android",
            "deviceName": device_config['deviceName'],
            "platformVersion": device_config['platformVersion'],
            "isRealMobile": True,
            "app": "lt://APP10160341071754500059009313",
            "build": "Android Pytest",
            "name": test_name
        }
    }

    username = os.environ.get("LT_USERNAME")
    access_key = os.environ.get("LT_ACCESS_KEY")
    driver = webdriver.Remote("https://"+username+":"+access_key+"@mobile-hub.lambdatest.com/wd/hub",
                              options=UiAutomator2Options().load_capabilities(caps))
    request.cls.driver = driver

    yield driver

    finalize_driver(request, driver)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item,call):
    # this sets the result as a test attribute for LambdaTest reporting.
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set an report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)