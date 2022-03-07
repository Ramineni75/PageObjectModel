from selenium.webdriver.common.by import By
from in_amazon_pages.base_page import BasePage


class LandingPage(BasePage):
    MOBILES = (By.LINK_TEXT, "Mobiles")
    HELLO_SIGN_IN = (By.ID, "nav-link-accountList")
    SIGNIN = (By.LINK_TEXT, "Sign in")

    def __init__(self, driver):
        super().__init__(driver)

    def click_mobiles(self):
        self.click_element(self.MOBILES)

    def hover_over_hello_sign_in(self):
        self.hover_over_element(self.HELLO_SIGN_IN)

    def click_sing_in_button(self):
        self.click_element(self.SIGNIN)


