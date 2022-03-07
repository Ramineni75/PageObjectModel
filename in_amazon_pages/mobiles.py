from selenium.webdriver.common.by import By
from in_amazon_pages.base_page import BasePage


class Mobiles(BasePage):
    MOBILES_AND_ACCESSORIES = (By.LINK_TEXT,"Mobiles & Accessories" )
    MODEL = (By.LINK_TEXT, "Samsung")


    def __init__(self,driver):
        super().__init__(driver)

    def hover_over_mobile_and_accessories(self):
        self.hover_over_element(self.MOBILES_AND_ACCESSORIES)

    def click_model(self):
        self.click_element(self.MODEL)