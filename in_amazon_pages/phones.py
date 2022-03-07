from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from in_amazon_pages.base_page import BasePage

class Phones(BasePage):
    PHONE = (By.XPATH, "(//img[contains(@class,'s-image')])[3]")

    def __init__(self,driver):
        super().__init__(driver)

    def click_phone(self):
        #self.click_element(WebDriverWait(self.driver,60).until(expected_conditions.visibility_of_element_located(self.PHONE))).click()
        self.click_element(self.PHONE)