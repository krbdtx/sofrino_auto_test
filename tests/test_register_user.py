import allure
from pages.steps import steps_on_pages
from test_data.data import User_data
from faker import Faker
fake = Faker()

user1 = User_data(first_name=fake.name_female(), last_name=fake.name_male(), phone_number=fake.phone_number(), email=fake.email(),
                  password=fake.password())
user2 = User_data(first_name='ghjghjghj', last_name='xcvxcvxcv', phone_number='0000000005', email='3a2a11$asdasd.gnom', password='******')
user3 = User_data(first_name=fake.name_female(), last_name=fake.name_male(), phone_number=fake.phone_number(), email=fake.email(),
                  password='   ')


@allure.step(f"Проверка регистрации сгенерированного пользователя {user1}")
def test_succes_register_user():

    steps_on_pages.fill_register_user(user1)
    steps_on_pages.should_register_user()


@allure.step(f"Проверка регистрациине не коректный e-mail {user2}")
def test_error_mail_register_user():

    steps_on_pages.fill_register_user(user2)
    steps_on_pages.should_error_mail_user()


@allure.step(f"Проверка регистрации сгенерированного пользователя Пустой пароль {user3}")
def test_error_pass_register_user():

    steps_on_pages.fill_register_user(user3)
    steps_on_pages.should_error_pass_user()
