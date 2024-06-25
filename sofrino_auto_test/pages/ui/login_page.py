import allure

from sofrino_auto_test.test_data.data import Userlogin
from selene import browser, have, by


class LogIn:

    @allure.step('Открыть браузер')
    def open_browser(self, url) -> object:
        browser.open(url)
        return self

    @allure.step('Заполнить поле E-mail:')
    def fill_login_mail_low(self, e_mail):
        browser.element('[type="text"]').type(e_mail)
        return self

    @allure.step('Заполнить поле Пароль:')
    def fill_login_password_low(self, password):
        browser.element('[type="password"]').type(password)
        return self

    @allure.step("Нажать кнопку войти")
    def submit_login_low(self):
        browser.element(by.text('Войти')).click()
        return self

    @allure.step("Нажать кнопку Выход")
    def submit_logout_low(self):
        browser.element(by.text('Выход')).click()
        return self

    @allure.step("Проверка не успешного входа Неправильный E-mail / пароль")
    def should_error_page_login_low(self):
        browser.element('.text-danger').should(have.exact_text('Неправильный E-mail / пароль'))
        return self

    @allure.step("Проверка успешного входа")
    def should_succes_page_login_low(self):
        browser.element('.shop-menu__link').should(have.exact_text('Корзина товаров'))
        return self


class StepsLogIn:

    @allure.step('Заполнить поля для авториазции')
    def fill_login_page(self, value: Userlogin):
        login.open_browser(url='/login')
        login.fill_login_mail_low(value.email)
        login.fill_login_password_low(value.password)
        login.submit_login_low()
        return self

    @allure.step('Проверка Вход с некоректными данными')
    def should_error_login_page(self):
        login.should_error_page_login_low()
        return self

    @allure.step('Проверка Вход с коректными данными')
    def should_login_user_lk_page(self):
        login.should_succes_page_login_low()
        return self


stepslogin = StepsLogIn()
login = LogIn()
