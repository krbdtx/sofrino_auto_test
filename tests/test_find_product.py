import allure
from pages.steps import mid_lvl
from test_data.data import Product

product1 = Product(product='фываолдж')
product2 = Product(product='Яйцо')


@allure.step(f"Проверка поиск не существуюущего товара {product1}")
def test_find_product():

    mid_lvl.find_product(product1)
    mid_lvl.should_find_product(product1)


@allure.step(f"Проверка поиск сущесвующего товара {product2}")
def test_find_product():

    mid_lvl.find_product(product2)
    mid_lvl.should_find_product(product2)
