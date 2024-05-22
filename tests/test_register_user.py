import allure
from model.pages_top import top_lvl
from data.small_bd import User_data
from faker import Faker
fake = Faker()

user1 = User_data(first_name=fake.name_female(), last_name=fake.name_male(), phone_number=fake.phone_number(), email=fake.email(),
                  password=fake.password())
user2 = User_data(first_name='ghjghjghj', last_name='xcvxcvxcv', phone_number='0000000005', email='3a2a11$asdasd.gnom', password='******')
user3 = User_data(first_name=fake.name_female(), last_name=fake.name_male(), phone_number=fake.phone_number(), email=fake.email(),
                  password=fake.password())


@allure.step(f"Проверка регистрации пользователя {user1}")
def test_review_send_01():

    top_lvl.fill_register_user(user1)
    top_lvl.should_register_user()


@allure.step(f"Проверка регистрации пользователя {user2}")
def test_review_send_02():

    top_lvl.fill_register_user(user2)
    top_lvl.should_register_user()


@allure.step(f"Проверка регистрации пользователя {user3}")
def test_review_send_03():

    top_lvl.fill_register_user(user3)
    top_lvl.should_register_user()
