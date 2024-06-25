import allure
import pytest
from sofrino_auto_test.pages.ui.find_page import stepsfindproduct
from sofrino_auto_test.test_data.data import product1, product2


@allure.tag('web')
@allure.epic('Проверка поиск UI')
@pytest.mark.web
@allure.step(f"Проверка поиск не существуюущего товара {product1}")
def test_find_non_product():
    stepsfindproduct.find_product(product1)
    stepsfindproduct.should_find_non_product()


@allure.tag('web')
@allure.epic('Проверка поиск UI')
@pytest.mark.web
@allure.step(f"Проверка поиск сущесвующего товара {product2}")
def test_find_exists_product():
    stepsfindproduct.find_product(product2)
    stepsfindproduct.should_find_product(product2)
