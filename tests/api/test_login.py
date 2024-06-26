import allure
import pytest
from jsonschema import validate
from selene import browser, have
from allure_commons._allure import step
from selene.support.conditions import have
from sofrino_auto_test.utils import attach
from sofrino_auto_test.test_data.data import exists_user, error_user
from sofrino_auto_test.utils.api_helper import api_request
from sofrino_auto_test.schemas.login import login_success, login_error

endpoint = '/login'


@allure.tag('api')
@allure.epic('Авторизация API')
@pytest.mark.api
def test_login_api(base_api_url):
    with step("Успешная Авторизация пользователя через API"):
        payload = {"action": "login", "email": exists_user.email, "password": exists_user.password}
        result = api_request(base_api_url, endpoint, 'POST', params=payload)
    with allure.step('Проверка статус Кода 200'):
        assert result.status_code == 200
        result_json = result.json()
    with allure.step('Проверка Значение в *response*.'):
        assert 'loginSuccess' in result_json
        assert result_json['loginSuccess'] is not None
    with allure.step('Schema is validate'):
        validate(result.json(), login_success)
    with step("Получение cookie сессии API"):
        cookies = result.cookies.get_dict()
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
        result = api_request(base_api_url, endpoint, 'POST', params=payload)
    with allure.step('Проверка статус Кода 200'):
        assert result.status_code == 200
        result_json = result.json()
    with allure.step('Проверка Значение в *response*.'):
        assert 'loginErrors' in result_json
    with allure.step('Schema is validate'):
        validate(result.json(), login_error)
    with step("Проверка ответа API не успешная авторизация"):
        assert 'loginErrors' in result.json()
