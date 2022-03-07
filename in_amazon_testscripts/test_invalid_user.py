from in_amazon_pages.landing_page import LandingPage
from in_amazon_pages.singin import SingIn
from in_amazon_testscripts.test_base import  BaseTest


class TestInvalidUser(BaseTest):
    def test_invalid_user(self):
        #hover over help sign in menu
        landing_page = LandingPage(self.driver)
        landing_page.hover_over_hello_sign_in()
        landing_page.click_sing_in_button()
        sign_in = SingIn(self.driver)
        sign_in.enter_email()
        sign_in.click_continue_button()
        actual_text = sign_in.verify_message()
        expected_text = "We cannot find an account with that email address"
        assert expected_text == actual_text




