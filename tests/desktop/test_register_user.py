import allure
from pages.ui.register_page import stepsregistration
from test_data.data import registeruser1, registeruser2, registeruser3


@allure.step(f"Проверка регистрации сгенерированного пользователя {registeruser1}")
def test_succes_register_user():

    stepsregistration.fill_register_user(registeruser1)
    stepsregistration.should_register_user()


@allure.step(f"Проверка регистрациине не коректный e-mail {registeruser2}")
def test_error_mail_register_user():

    stepsregistration.fill_register_user(registeruser2)
    stepsregistration.should_error_mail_user()


@allure.step(f"Проверка регистрации сгенерированного пользователя Пустой пароль {registeruser3}")
def test_error_pass_register_user():

    stepsregistration.fill_register_user(registeruser3)
    stepsregistration.should_error_pass_user()
