import allure
from pages.ui.find_page import stepsfindproduct
from test_data.data import Product


@allure.step(f"Проверка поиск не существуюущего товара {Product.product1}")
def test_find_non_product():

    stepsfindproduct.find_product(Product.product1)
    stepsfindproduct.should_find_non_product()


@allure.step(f"Проверка поиск сущесвующего товара {Product.product2}")
def test_find_exists_product():

    stepsfindproduct.find_product(Product.product2)
    stepsfindproduct.should_find_product(Product.product2)
