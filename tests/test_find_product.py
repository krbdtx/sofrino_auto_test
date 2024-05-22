import allure
from model.pages_top import top_lvl
from data.small_bd import Tovar

product1 = Tovar(product='фываолдж')
product2 = Tovar(product='Яйцо')


@allure.step(f"Проверка поиск товара {product1}")
def test_find_product_01():

    top_lvl.find_product(product1)
    top_lvl.should_find_product(product1)


@allure.step(f"Проверка поиск товара {product2}")
def test_find_product_02():

    top_lvl.find_product(product2)
    top_lvl.should_find_product(product2)
