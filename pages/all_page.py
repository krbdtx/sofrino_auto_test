import allure

from selene import browser, have, by, be


class Elements:

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

    @allure.step("заполнить поле имя формы отзыв")
    def fild_review_name_low(self, name):
        browser.element('[name="data[name]"]').type(name)
        return self

    @allure.step("заполнить поле номер телефона формы отзыв")
    def fild_review_phone_low(self, phone):
        browser.element('[name="data[phone]"]').type(phone)
        return self

    @allure.step("заполнить поле текст отзыва формы отзыв")
    def fild_review_low(self, reviews):
        browser.element('[name="data[review]"]').type(reviews)
        return self

    @allure.step("Нажать кнопку отправить отзыв")
    def submit_review_low(self):
        browser.element(by.text('Отправить')).click()
        return self

    @allure.step("Проверка отправки отзыва")
    def should_review_low(self):
        browser.element('.fs-16').should(have.exact_text('Ваш отзыв успешно отправлен.'))
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


elements = Elements()
