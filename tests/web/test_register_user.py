import allure
import pytest
from sofrino_auto_test.pages.ui.register_page import stepsregistration
from sofrino_auto_test.test_data.data import registeruser1, registeruser2, registeruser3


@allure.tag('web')
@allure.epic('Регистрация UI')
@pytest.mark.web
@allure.step(f"Проверка регистрации сгенерированного пользователя {registeruser1}")
def test_succes_register_user():

    stepsregistration.fill_register_user(registeruser1)
    stepsregistration.should_register_user()


@allure.tag('web')
@allure.epic('Регистрация UI')
@pytest.mark.web
@allure.step(f"Проверка регистрации не коректный e-mail {registeruser2}")
def test_error_mail_register_user():

    stepsregistration.fill_register_user(registeruser2)
    stepsregistration.should_error_mail_user()


@allure.tag('web')
@allure.epic('Регистрация UI')
@pytest.mark.web
@allure.step(f"Проверка регистрации сгенерированного пользователя Пустой пароль {registeruser3}")
def test_error_pass_register_user():

    stepsregistration.fill_register_user(registeruser3)
    stepsregistration.should_error_pass_user()
