import requests
from allure_commons._allure import step
from selene import browser
from allure_commons.types import AttachmentType
from selene.support.conditions import have
import allure
from utils import attach


LOGIN = "фыв@фыв.com"
PASSWORD = "123123"
API_URL = "https://sofrino.ru/login"
WEB_URL = "https://sofrino.ru/users/lk"


def test_login_though_api():
    with step("Авторизация пользователя через API"):
        result = requests.post(
            url=API_URL,
            data={"action": "login", "email": LOGIN, "password": PASSWORD})
        allure.attach(body=result.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=str(result.cookies), name="UserToken", attachment_type=AttachmentType.TEXT, extension="txt")
    #with step("Get cookie from API"):
    #    cookie = result.cookies.get("UserToken")

    with step("Set cookie from API"):
    #    browser.open(WEB_URL)
    #    browser.driver.add_cookie({"name": "UserToken", "value": cookie})
        browser.open(WEB_URL)

    with step("Verify successful authorization"):
        browser.element('.shop-menu__link').should(have.exact_text('Корзина товаров'))

