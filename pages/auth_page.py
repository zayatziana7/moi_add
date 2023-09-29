from pages.base_page import BaseUIMethods
from pages.ui_locators import Locators


class AuthPage(BaseUIMethods):
    def insert_login(self, login: str) -> None:
        self.get_value()
        self.element_presence(locator=Locators.passp_field_login, driver=self.driver).send_keys(login)

    def click_sing_in_btn(self) -> None:
        self.element_presence(locator=Locators.passp_sign_in, driver=self.driver).click()

    def insert_password(self, password: str) -> None:
        self.element_presence(locator=Locators.passp_field_passwd, driver=self.driver).send_keys(password)




