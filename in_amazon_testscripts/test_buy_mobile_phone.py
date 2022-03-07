import allure
from allure_commons.types import AttachmentType

from in_amazon_pages.addtocart import AddToCart
from in_amazon_pages.mobiles import Mobiles
from in_amazon_pages.phones import Phones
from in_amazon_pages.singin import SingIn
from in_amazon_testscripts.test_base import BaseTest
from in_amazon_pages.landing_page import LandingPage

@allure.severity(allure.severity_level.NORMAL)
class TestBuyMobilePhone(BaseTest):
    @allure.severity(allure.severity_level.MINOR)
    def test_buy_mobile(self):
        landing_page = LandingPage(self.driver)
        landing_page.click_mobiles()
        allure.attach(self.driver.get_screenshot_as_png(), name= "LandingPageSS", attachment_type=AttachmentType.PNG)

        mobiles = Mobiles(self.driver)
        mobiles.hover_over_mobile_and_accessories()
        mobiles.click_model()

        phone_buy = Phones(self.driver)
        phone_buy.click_phone()

        handle = self.driver.window_handles
        self.driver.switch_to.window(handle[1])

        cartload = AddToCart(self.driver)
        cartload.click_button()
        cartload.click_on_Procees_to_buy()

        sing_in = SingIn(self.driver)
        expected_test = "Sign-In"
        actual_text = sing_in.verify_sign_in_text()
        assert expected_test == actual_text







