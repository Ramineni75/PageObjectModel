from selenium.webdriver.common.by import By
from in_amazon_pages.base_page import BasePage

class SingIn(BasePage):
    SIGNIN = (By.XPATH, "//h1[contains(@class,'spacing-small')]")
    EMAIL = (By.ID, "ap_email")
    CONTINUE = (By.ID, "continue")
    MESSAGE = (By.XPATH, "(//div[contains(@class,'a-alert-content')])[1]")

    def __init__(self,driver):
        super().__init__(driver)

    def verify_sign_in_text(self):
        text = self.get_text(self.SIGNIN)
        return text

    def enter_email(self):
        self.enter_text(self.EMAIL,"batman554466@gmail.com" )

    def click_continue_button(self):
        self.click_element(self.CONTINUE)

    def verify_message(self):
        text = self.get_text(self.MESSAGE)
        return text

