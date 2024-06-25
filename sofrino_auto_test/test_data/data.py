from dataclasses import dataclass
from faker import Faker

fake = Faker()


@dataclass
class Product:
    product: str


@dataclass
class ReviewData:
    name: str
    phone: str
    reviews: str


@dataclass
class UserLogin:
    email: str
    password: str


@dataclass
class UserData:
    first_name: str
    last_name: str
    phone_number: str
    email: str
    password: str


fake_product = Product(
    product=fake.text(10)
)
exists_product = Product('Яйцо')

dynamic_review = ReviewData(
    name=fake.name(),
    phone=fake.phone_number(),
    reviews=fake.text(100)
)
static_review = ReviewData(
    name='Робот',
    phone='9876543210',
    reviews='Это тестовый робот для тренировки, ваш ресурс прекрасно для этого подходит, уже вышел!!!'
)

exists_user = UserLogin(
    email='фыв@фыв.com',
    password='123123'
)
error_user = UserLogin(
    email='11asasdasd1@2asdasasd22.com',
    password='фывфвфыв123123123asdasdasd'
)
fake_user = UserLogin(
    email=fake.email(),
    password=fake.password()
)
dynamic_register_user = UserData(
    first_name=fake.name_female(),
    last_name=fake.name_male(),
    phone_number=fake.phone_number(),
    email=fake.email(),
    password=fake.password()
)
error_mail_register_user = UserData(
    first_name='ghjghjghj',
    last_name='xcvxcvxcv',
    phone_number='0000000005',
    email='3a2a11$asdasd.gnom',
    password='******'
)
empty_pass_register_user = UserData(
    first_name=fake.name_female(),
    last_name=fake.name_male(),
    phone_number=fake.phone_number(),
    email=fake.email(),
    password='   '
)
