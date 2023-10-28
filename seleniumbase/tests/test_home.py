from seleniumbase import BaseCase


class HomeTest(BaseCase):
    def test_home_page(self):
        # open home page
        self.open("https://practice.sdetunicorns.com/")
        # assert page title
        self.assert_title("Practice E-Commerce Site – SDET Unicorns – Helping you succeed in Software Quality.")
        # assert logo
        self.assert_element(".custom-logo-link")
