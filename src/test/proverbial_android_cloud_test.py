import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from appium.webdriver.webdriver import WebDriver


@pytest.mark.usefixtures('test_setup_android')
class TestProverbialApp:
    driver: WebDriver

    def test_proverbial_text(self):
        wait = WebDriverWait(self.driver, 20)
        text_button = wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.lambdatest.proverbial:id/Text")))
        text_button.click()

        text = self.driver.find_element(AppiumBy.ID, "com.lambdatest.proverbial:id/Textbox")
        assert text.is_displayed(), "Proverbial"