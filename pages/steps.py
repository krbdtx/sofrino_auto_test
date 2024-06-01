import allure

from test_data.data import *
from pages.all_page import elements


class Steps_on_pages:
    """
    Класс работы Средний уровень
    тут составляются тест кейсы
    т.к. это демо версия которая потом возможно пойдет в диплом то на разные файлы разбивать не стал
    TODO разнести тест кейсы по разным файлам-страницам или по пакетам
    """

    @allure.step('Проверка работы с поиском по товарам')
    def find_product(self, find: Product):
        elements.open_browser(url='/')
        elements.find_product_low(find.product)
        return self

    @allure.step('Результат поиска товара')
    def should_find_product(self, find: Product):
        elements.should_find_product_low(find.product)
        return self

    @allure.step('Результат не удалось найти товар')
    def should_find_non_product(self):
        elements.should_find_non_product_low()
        return self

    @allure.step('Заполнить и отправить отзыв')
    def fild_review(self, value: Review):
        elements.open_browser(url='/o-predpriyatii/otzyvy')
        elements.fild_review_name_low(value.name)
        elements.fild_review_phone_low(value.phone)
        elements.fild_review_low(value.reviews)
        elements.submit_review_low()
        return self

    @allure.step('Проверить запись об успешной отправке отзыва')
    def should_review(self):
        elements.should_review_low()
        return self

    @allure.step('Заполнить поля для авториазции')
    def fill_login_page(self, value: User_login):
        elements.open_browser(url='/login')
        elements.fill_login_mail_low(value.email)
        elements.fill_login_password_low(value.password)
        elements.submit_login_low()
        return self

    @allure.step('Вход с некоректными данными')
    def should_error_login_page(self):
        elements.should_error_page_login_low()
        return self

    @allure.step('Вход с коректными данными')
    def should_login_user_lk_page(self):
        elements.should_succes_page_login_low()
        return self

    @allure.step('Заполнить поля регистрации')
    def fill_register_user(self, value: User_data):
        elements.open_browser(url='/login?state=register')
        elements.fill_user_last_name(value.first_name)
        elements.fill_user_first_name(value.first_name)
        elements.fill_user_phone(value.phone_number)
        elements.fill_user_email(value.email)
        elements.fill_user_password(value.password)
        elements.submit_register_user()
        return self

    @allure.step('Проверить успешность регистрации')
    def should_register_user(self):
        elements.should_succes_register_user()
        return self

    @allure.step('Проверить НЕ верный адрес почты')
    def should_error_mail_user(self):
        elements.should_error_mail_register_user()
        return self

    @allure.step('Проверить пустой пароль')
    def should_error_pass_user(self):
        elements.should_error_pass_register_user()
        return self


steps_on_pages = Steps_on_pages()
