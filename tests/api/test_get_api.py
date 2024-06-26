import allure
import pytest
from jsonschema import validate
from allure_commons._allure import step
from sofrino_auto_test.utils.api_helper import api_request
from sofrino_auto_test.schemas.carts import mini_cart_view
from sofrino_auto_test.schemas.review import review_cend

endpoint_view = '/carts/mincart'
endpoint_review = '/leads/add'


@allure.tag('api')
@allure.epic('Просмотр Пустой корзины API')
@pytest.mark.api
def test_view_cart_api(base_api_url):
    with step("Просмотр корзины через API"):
        payload = {"task": 'view'}
        result = api_request(base_api_url, endpoint_view, 'GET', params=payload)

    with allure.step('Проверка статус Кода 200'):
        assert result.status_code == 200

        result_json = result.json()
    with allure.step('Проверка Значение в *response*.'):
        assert 'allAmounts' in result_json
        assert result_json['allAmounts'] is not None

    with allure.step('Schema is validate'):
        validate(result.json(), mini_cart_view)


@allure.tag('api')
@allure.epic('Просмотр пустого отзыва API')
@pytest.mark.api
def test_review_get_api(base_api_url):
    with step("Просмотр корзины через API"):
        payload = {"status": ""}
        result = api_request(base_api_url, endpoint_review, 'GET', params=payload)

    with allure.step('Проверка статус Кода 200'):
        assert result.status_code == 200

        result_json = result.json()
    with allure.step('Проверка Значение в *response*.'):
        assert 'status' in result_json
        assert result_json['status'] is not None

    with allure.step('Schema is validate'):
        validate(result.json(), review_cend)
