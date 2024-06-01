import allure
from pages.steps import steps_on_pages
from test_data.data import Product

product1 = Product(product='фываолдж')
product2 = Product(product='Яйцо')


@allure.step(f"Проверка поиск не существуюущего товара {product1}")
def test_find_non_product():

    steps_on_pages.find_product(product1)
    steps_on_pages.should_find_non_product()


@allure.step(f"Проверка поиск сущесвующего товара {product2}")
def test_find_exists_product():

    steps_on_pages.find_product(product2)
    steps_on_pages.should_find_product(product2)
