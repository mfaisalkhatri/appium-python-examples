import os.path
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


apk_path = os.path.abspath('./src/test/resources/proverbial_android.apk')
options = UiAutomator2Options().load_capabilities({
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'Pixel 6 API 34',
    'app': apk_path
})

appium_server_url = 'http://localhost:4723'

class TestProverbialApp:
    def setup_method(self):
        self.driver = webdriver.Remote(appium_server_url, options=options)

    def teardown_method(self):
        if self.driver:
            self.driver.quit()

    def test_proverbial_text(self):
        wait = WebDriverWait(self.driver, 20)
        text_button = wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.lambdatest.proverbial:id/Text")))
        text_button.click()

        text = self.driver.find_element(AppiumBy.ID, "com.lambdatest.proverbial:id/Textbox")
        assert text.is_displayed(), "Proverbial"