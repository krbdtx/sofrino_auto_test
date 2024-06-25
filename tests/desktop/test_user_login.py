import allure
import pytest
from sofrino_auto_test.pages.ui.login_page import stepslogin
from sofrino_auto_test.test_data.data import user1, user2, user3


@allure.tag('web')
@allure.epic('Авторизация UI')
@pytest.mark.web
@allure.step(f"Проверка Успешный входа пользователя корректные данные{user1}")
def test_succes_login():

    stepslogin.fill_login_page(user1)
    stepslogin.should_login_user_lk_page()


@allure.tag('web')
@allure.epic('Авторизация UI')
@pytest.mark.web
@allure.step(f"Проверка не успешного входа пользователя не корректные статичные данные{user2}")
def test_error_static_login():

    stepslogin.fill_login_page(user2)
    stepslogin.should_error_login_page()


@allure.tag('web')
@allure.epic('Авторизация UI')
@pytest.mark.web
@allure.step(f"Проверка не успешного входа пользователя не корректные динамичные данные{user3}")
def test_error_dynamic_login():

    stepslogin.fill_login_page(user3)
    stepslogin.should_error_login_page()
