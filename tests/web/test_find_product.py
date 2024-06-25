import allure
import pytest
from sofrino_auto_test.pages.ui.find_page import stepsfindproduct
from sofrino_auto_test.test_data.data import fake_product, exists_product


@allure.tag('web')
@allure.epic('Проверка поиск UI')
@pytest.mark.web
@allure.step(f"Проверка поиск не существуюущего товара {fake_product}")
def test_find_non_product():
    stepsfindproduct.find_product(fake_product)
    stepsfindproduct.should_find_non_product()


@allure.tag('web')
@allure.epic('Проверка поиск UI')
@pytest.mark.web
@allure.step(f"Проверка поиск сущесвующего товара {exists_product}")
def test_find_exists_product():
    stepsfindproduct.find_product(exists_product)
    stepsfindproduct.should_find_product(exists_product)


@allure.tag('web')
@allure.epic('Проверка поиск UI')
@pytest.mark.web
@allure.step(f"Проверка поиск не существуюущего товара2 фейковая ошибка {fake_product}")
def test_find_non_product():
    stepsfindproduct.find_product(fake_product)
    stepsfindproduct.should_find_product(fake_product)