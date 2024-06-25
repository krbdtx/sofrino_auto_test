import allure
import pytest
from sofrino_auto_test.pages.ui.register_page import stepsregistration
from sofrino_auto_test.test_data.data import dynamic_register_user, error_mail_register_user, empty_pass_register_user


@allure.tag('web')
@allure.epic('Регистрация UI')
@pytest.mark.web
@allure.step(f"Проверка регистрации сгенерированного пользователя {dynamic_register_user}")
def test_success_register_user():
    stepsregistration.fill_register_user(dynamic_register_user)
    stepsregistration.should_register_user()


@allure.tag('web')
@allure.epic('Регистрация UI')
@pytest.mark.web
@allure.step(f"Проверка регистрации не коректный e-mail {error_mail_register_user}")
def test_error_mail_register_user():
    stepsregistration.fill_register_user(error_mail_register_user)
    stepsregistration.should_error_mail_user()


@allure.tag('web')
@allure.epic('Регистрация UI')
@pytest.mark.web
@allure.step(f"Проверка регистрации сгенерированного пользователя Пустой пароль {empty_pass_register_user}")
def test_error_pass_register_user():
    stepsregistration.fill_register_user(empty_pass_register_user)
    stepsregistration.should_error_pass_user()
