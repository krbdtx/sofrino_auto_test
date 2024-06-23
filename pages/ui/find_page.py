import allure

from test_data.data import Product
from selene import browser, have


class FindProduct:

    @allure.step('Открыть браузер')
    def open_browser(self, url) -> object:
        browser.open(url)
        return self

    @allure.step("Заполнить поле поиска по товарам ")
    def find_product_low(self, find):
        browser.element('.topline__search__input').click()
        browser.element('#searchResultsInput').type(find).press_enter()
        return self

    @allure.step("Проверка результата поиска по товарам ")
    def should_find_product_low(self, find):
        browser.element('.container-header').should(
            have.exact_text(f'Товары по запросу "{find}"'))
        return self

    @allure.step("Проверка результата поиска по не существуюущим товарам ")
    def should_find_non_product_low(self):
        browser.element('.text-box').should(have.text('Нам не удалось найти товар по вашему запросу.'))
        return self


class StepsOnFindPages:

    @allure.step('Проверка работы с поиском по товарам')
    def find_product(self, find: Product):
        findproduct.open_browser(url='/')
        findproduct.find_product_low(find.product)
        return self

    @allure.step('Результат поиска товара')
    def should_find_product(self, find: Product):
        findproduct.should_find_product_low(find.product)
        return self

    @allure.step('Результат не удалось найти товар')
    def should_find_non_product(self):
        findproduct.should_find_non_product_low()
        return self


stepsfindproduct = StepsOnFindPages()
findproduct = FindProduct()
