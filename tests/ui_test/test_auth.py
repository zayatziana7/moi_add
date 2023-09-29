from const.data import login
from const.urls import Urls
from pages.auth_page import AuthPage


def test_auth_1(driver_1):
    driver_1.get(Urls.url_auth_page.value)
    auth_page = AuthPage(driver=driver_1)
    auth_page.insert_login(login=login)
    auth_page.click_sing_in_btn()








