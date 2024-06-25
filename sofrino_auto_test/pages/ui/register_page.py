import allure

from sofrino_auto_test.test_data.data import Userdata
from selene import browser, have, be


class Registration:

    @allure.step('Открыть браузер')
    def open_browser(self, url) -> object:
        browser.open(url)
        return self

    @allure.step("Ввод Фамилии")
    def fill_user_last_name(self, last_name):
        browser.element('#register').all('.form-group').element_by(have.text('Фамилия:')).element('.form-control').type(
            last_name)
        return self

    @allure.step("Ввод Имени")
    def fill_user_first_name(self, first_name):
        browser.element('#register').all('.form-group').element_by(have.text('Имя:')).element('.form-control').type(
            first_name)
        return self

    @allure.step("Ввод Телефона")
    def fill_user_phone(self, phone):
        browser.element('#register').all('.form-group').element_by(have.text('Телефон:')).element('.form-control').type(
            phone)
        return self

    @allure.step("Ввод Почты")
    def fill_user_email(self, email):
        browser.element('#register').all('.form-group').element_by(have.text('E-mail:')).element('.form-control').type(
            email)
        return self

    @allure.step("Ввод Пароля")
    def fill_user_password(self, password):
        browser.element('#register').all('.form-group').element_by(have.text('Пароль:')).element('.form-control').type(
            password)
        return self

    @allure.step("Нажать кнопку Зарегистрироваться")
    def submit_register_user(self):
        browser.element('#register').element('.row').element('.btn').click()
        return self

    @allure.step("Проверка успешная регистрация")
    def should_succes_register_user(self):
        browser.element('[role="alert"]').should(have.text(
            'Вы успешно зарегистрированы. Мы выслали вам данные для входа на e-mail.'))
        return self

    @allure.step("Проверка поля адрес почты НЕ верный адрес почты")
    def should_error_mail_register_user(self):
        browser.element('#register').element('.border-danger').should(be.visible)
        return self

    @allure.step("Проверка поля пароль НЕ верный пароль")
    def should_error_pass_register_user(self):
        browser.element('#register').element('.border-danger').should(be.visible)
        return self


class StepsRegistration:

    @allure.step('Заполнить поля регистрации')
    def fill_register_user(self, value: Userdata):
        registration.open_browser(url='/login?state=register')
        registration.fill_user_last_name(value.first_name)
        registration.fill_user_first_name(value.first_name)
        registration.fill_user_phone(value.phone_number)
        registration.fill_user_email(value.email)
        registration.fill_user_password(value.password)
        registration.submit_register_user()
        return self

    @allure.step('Проверить успешность регистрации')
    def should_register_user(self):
        registration.should_succes_register_user()
        return self

    @allure.step('Проверить НЕ верный адрес почты')
    def should_error_mail_user(self):
        registration.should_error_mail_register_user()
        return self

    @allure.step('Проверить пустой пароль')
    def should_error_pass_user(self):
        registration.should_error_pass_register_user()
        return self


stepsregistration = StepsRegistration()
registration = Registration()
