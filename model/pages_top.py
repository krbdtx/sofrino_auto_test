import allure

from data.small_bd import *
from model.pages_lower_lvl import lower_lvl


class pages_top:
    """
    Класс работы верхний урвоень
    """

    @allure.step('Проверка работы с поиском по товарам')
    def find_product(self, find: Tovar):
        lower_lvl.open_win(url='/')
        lower_lvl.find_product_low(find.product)
        return self

    @allure.step('Результат поиска товара')
    def should_find_product(self, find: Tovar):
        lower_lvl.should_find_product_low(find.product)
        return self

    @allure.step('Заполнить и отправить отзыв')
    def fild_review(self, value: Review):
        lower_lvl.open_win(url='/o-predpriyatii/otzyvy')
        lower_lvl.fild_review_name_low(value.name)
        lower_lvl.fild_review_phone_low(value.phone)
        lower_lvl.fild_review_low(value.reviews)
        lower_lvl.submit_review_low()
        return self

    @allure.step('проверить запись об успешной отправке отзыва')
    def should_review(self):
        lower_lvl.should_review_low()
        return self

    @allure.step('Заполнить поля для авториазции')
    def fill_login_pgs(self, value: User_login):
        lower_lvl.open_win(url='/login')
        lower_lvl.fill_login_mail_low(value.email)
        lower_lvl.fill_login_password_low(value.password)
        lower_lvl.submit_login_low()
        return self

    @allure.step('Вход с некоректными данными')
    def should_login_neg_pgs(self):
        lower_lvl.should_neg_login_low()
        return self

    @allure.step('Вход с коректными данными')
    def should_login_good_pgs(self):
        lower_lvl.should_pozitiv_login_low()
        return self

    @allure.step('Заполнить поля регистрации')
    def fill_register_user(self, value: User_data):
        lower_lvl.open_win(url='/login?state=register')
        lower_lvl.fill_user_last_name(value.first_name)
        lower_lvl.fill_user_first_name(value.first_name)
        lower_lvl.fill_user_phone(value.phone_number)
        lower_lvl.fill_user_email(value.email)
        lower_lvl.fill_user_password(value.password)
        lower_lvl.submit_register_user()
        return self

    @allure.step('Проверить успешность регистрации')
    def should_register_user(self):
        lower_lvl.should_good_register_user()
        return self


top_lvl = pages_top()
