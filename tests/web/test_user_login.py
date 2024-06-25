import allure
import pytest
from sofrino_auto_test.pages.ui.login_page import stepslogin
from sofrino_auto_test.test_data.data import exists_user, error_user, fake_user


@allure.tag('web')
@allure.epic('Авторизация UI')
@pytest.mark.web
@allure.step(f"Проверка Успешный входа пользователя корректные данные{exists_user}")
def test_success_login():
    stepslogin.fill_login_page(exists_user)
    stepslogin.should_login_user_lk_page()


@allure.tag('web')
@allure.epic('Авторизация UI')
@pytest.mark.web
@allure.step(f"Проверка не успешного входа пользователя не корректные статичные данные{error_user}")
def test_error_static_login():
    stepslogin.fill_login_page(error_user)
    stepslogin.should_error_login_page()


@allure.tag('web')
@allure.epic('Авторизация UI')
@pytest.mark.web
@allure.step(f"Проверка не успешного входа пользователя не корректные динамичные данные{fake_user}")
def test_error_dynamic_login():
    stepslogin.fill_login_page(fake_user)
    stepslogin.should_error_login_page()
