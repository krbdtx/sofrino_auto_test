import requests
import allure
import pytest
import json
from selene import browser, have
from allure_commons._allure import step
from selene.support.conditions import have
from sofrino_auto_test.test_data.data import exists_user, error_user
from sofrino_auto_test.utils import attach


@allure.tag('api')
@allure.epic('Авторизация API')
@pytest.mark.api
def test_login_api(base_api_url):
    with step("Успешная Авторизация пользователя через API"):
        payload = {"action": "login", "email": exists_user.email, "password": exists_user.password}
        payload_json = json.dumps(payload)
        headers = {
            'content-type': 'application/json; charset=UTF-8',
            'x-requested-with': 'XMLHttpRequest'
        }

        result = requests.post(base_api_url + '/login', headers=headers, data=payload_json)
        attach.request_url_and_body(result)
    with step("Получение cookie сессии API"):
        cookies = result.cookies.get_dict()
        attach.response_json_and_cookies(result)
        browser.open(base_api_url + '/users/lk')
    with step("Установка cookie сессии API"):
        for name, value in cookies.items():
            browser.driver.add_cookie({"name": name, "value": value})
        browser.driver.refresh()
    with step("Проверка API авторизации в UI"):
        attach.add_screenshot(browser)
        assert browser.element('.shop-menu__link').should(have.exact_text('Корзина товаров'))


@allure.tag('api')
@allure.epic('Авторизация API')
@pytest.mark.api
def test_failed_login_api(base_api_url):
    with step("Не успешная Авторизация пользователя через API"):
        payload = {"action": "login", "email": exists_user.email, "password": error_user.password}
        payload_json = json.dumps(payload)
        headers = {
            'content-type': 'application/json; charset=UTF-8',
            'x-requested-with': 'XMLHttpRequest'
        }

        result = requests.post(base_api_url + '/login', headers=headers, data=payload_json)
        attach.request_url_and_body(result)

    with step("Проверка ответа API не успешная авторизация"):
        assert 'loginErrors' in result.json()
