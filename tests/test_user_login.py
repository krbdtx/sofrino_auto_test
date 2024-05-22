import allure
from model.pages_top import top_lvl
from data.small_bd import User_login
from faker import Faker
fake = Faker()

user1 = User_login(email='фыв@фыв.com', password='123123')
user2 = User_login(email='11asasdasd1@2asdasasd22.com', password='фывфвфыв123123123asdasdasd')
user3 = User_login(email=fake.email(), password=fake.password())


@allure.step(f"Проверка входа пользователя {user1}")
def test_login_01():

    top_lvl.fill_login_pgs(user1)
    top_lvl.should_login_good_pgs()


@allure.step(f"Проверка входа пользователя {user2}")
def test_login_02():

    top_lvl.fill_login_pgs(user2)
    top_lvl.should_login_neg_pgs()

@allure.step(f"Проверка входа пользователя {user3}")
def test_login_03():

    top_lvl.fill_login_pgs(user2)
    top_lvl.should_login_neg_pgs()
