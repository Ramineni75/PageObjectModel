from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator):
        WebDriverWait(self.driver,60).until(expected_conditions.visibility_of_element_located(locator)).click()

    def enter_text(self,locator,text):
        WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located(locator)).send_keys(text)

    def is_element_enabled(self,locator):
        status = WebDriverWait(self.driver,60).until(expected_conditions.visibility_of_element_located(locator)).is_enabled()
        return status

    def get_title(self):
        return self.driver.title

    def get_text(self,locator):
        value = WebDriverWait(self.driver,60).until(expected_conditions.visibility_of_element_located(locator)).text
        return value

    def hover_over_element(self, locator):
        action = ActionChains(self.driver)
        action.move_to_element(WebDriverWait(self.driver,60).until(expected_conditions.visibility_of_element_located(locator))).perform()