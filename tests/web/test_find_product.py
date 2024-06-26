import allure
import pytest
from sofrino_auto_test.pages.ui.find_page import steps_findp_roduct
from sofrino_auto_test.test_data.data import fake_product, exists_product


@allure.tag('web')
@allure.epic('Проверка поиск UI')
@pytest.mark.web
@allure.step(f"Проверка поиск не существуюущего товара {fake_product}")
@pytest.fixture
def test_find_non_product():
    steps_findp_roduct.find_product(fake_product)
    steps_findp_roduct.should_find_non_product()


@allure.tag('web')
@allure.epic('Проверка поиск UI')
@pytest.mark.web
@allure.step(f"Проверка поиск сущесвующего товара {exists_product}")
@pytest.fixture
def test_find_exists_product():
    steps_findp_roduct.find_product(exists_product)
    steps_findp_roduct.should_find_product(exists_product)


@allure.tag('web')
@allure.epic('Проверка поиск UI')
@pytest.mark.web
@allure.step(f"Проверка поиск не существуюущего товара2 фейковая ошибка {fake_product}")
@pytest.fixture
def test_find_non_product_fake():
    steps_findp_roduct.find_product(fake_product)
    steps_findp_roduct.should_find_product(fake_product)
