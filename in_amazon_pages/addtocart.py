from selenium.webdriver.common.by import By
from in_amazon_pages.base_page import BasePage


class AddToCart(BasePage):
    PHONETOBUY = (By.ID,"add-to-cart-button" )
    PROCEEDTOBUY = (By.XPATH,  "//input[contains(@aria-labelledby, 'attach-sidesheet-checkout-button-announce')]")

    def __init__(self,driver):
        super().__init__(driver)

    def click_button(self):
        self.click_element(self.PHONETOBUY)

    def click_on_Procees_to_buy(self):
        self.click_element(self.PROCEEDTOBUY)