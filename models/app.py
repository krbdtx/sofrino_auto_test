import allure

from test_data.data import *
from pages.all_page import low_lvl


class Mid_lvl:
    """
    Класс работы Средний уровень
    тут составляются тест кейсы
    т.к. это демо версия которая потом возможно пойдет в диплом то на разные файлы разбивать не стал
    TODO разнести тест кейсы по разным файлам-страницам или по пакетам
    """

    @allure.step('Проверка работы с поиском по товарам')
    def find_product(self, find: Product):
        low_lvl.open_browser(url='/')
        low_lvl.find_product_low(find.product)
        return self

    @allure.step('Результат поиска товара')
    def should_find_product(self, find: Product):
        low_lvl.should_find_product_low(find.product)
        return self

    @allure.step('Заполнить и отправить отзыв')
    def fild_review(self, value: Review):
        low_lvl.open_browser(url='/o-predpriyatii/otzyvy')
        low_lvl.fild_review_name_low(value.name)
        low_lvl.fild_review_phone_low(value.phone)
        low_lvl.fild_review_low(value.reviews)
        low_lvl.submit_review_low()
        return self

    @allure.step('Проверить запись об успешной отправке отзыва')
    def should_review(self):
        low_lvl.should_review_low()
        return self

    @allure.step('Заполнить поля для авториазции')
    def fill_login_pgs(self, value: User_login):
        low_lvl.open_browser(url='/login')
        low_lvl.fill_login_mail_low(value.email)
        low_lvl.fill_login_password_low(value.password)
        low_lvl.submit_login_low()
        return self

    @allure.step('Вход с некоректными данными')
    def should_login_neg_pgs(self):
        low_lvl.should_negative_login_low()
        return self

    @allure.step('Вход с коректными данными')
    def should_login_good_pgs(self):
        low_lvl.should_pozitiv_login_low()
        return self

    @allure.step('Заполнить поля регистрации')
    def fill_register_user(self, value: User_data):
        low_lvl.open_browser(url='/login?state=register')
        low_lvl.fill_user_last_name(value.first_name)
        low_lvl.fill_user_first_name(value.first_name)
        low_lvl.fill_user_phone(value.phone_number)
        low_lvl.fill_user_email(value.email)
        low_lvl.fill_user_password(value.password)
        low_lvl.submit_register_user()
        return self

    @allure.step('Проверить успешность регистрации')
    def should_register_user(self):
        low_lvl.should_good_register_user()
        return self


mid_lvl = Mid_lvl()
