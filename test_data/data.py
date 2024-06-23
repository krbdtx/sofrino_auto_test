from dataclasses import dataclass
from faker import Faker

fake = Faker()


@dataclass
class Product:
    product: str
    product1 = 'фываолдж'
    product2 = 'Яйцо'


@dataclass
class ReviewData:
    name: str
    phone: str
    reviews: str


@dataclass
class Userlogin:
    email: str
    password: str


@dataclass
class Userdata:
    first_name: str
    last_name: str
    phone_number: str
    email: str
    password: str


rev1 = ReviewData(name=fake.name(), phone=fake.phone_number(), reviews=fake.text(100))
rev2 = ReviewData(name='Робот', phone='9876543210',
                  reviews='Здравствуйте Уважаемые коллеги, это тестовый робот для тренировки, ваш ресурс прекрасно для этого подходит, уже вышел!!!')

user1 = Userlogin(email='фыв@фыв.com', password='123123')
user2 = Userlogin(email='11asasdasd1@2asdasasd22.com', password='фывфвфыв123123123asdasdasd')
user3 = Userlogin(email=fake.email(), password=fake.password())


registeruser1 = Userdata(first_name=fake.name_female(), last_name=fake.name_male(), phone_number=fake.phone_number(), email=fake.email(),
                  password=fake.password())
registeruser2 = Userdata(first_name='ghjghjghj', last_name='xcvxcvxcv', phone_number='0000000005', email='3a2a11$asdasd.gnom', password='******')
registeruser3 = Userdata(first_name=fake.name_female(), last_name=fake.name_male(), phone_number=fake.phone_number(), email=fake.email(),
                  password='   ')