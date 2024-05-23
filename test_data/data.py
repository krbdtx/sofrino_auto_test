import dataclasses


@dataclasses.dataclass
class Product:
    product: str


@dataclasses.dataclass
class Review:
    name: str
    phone: str
    reviews: str


@dataclasses.dataclass
class User_login:
    email: str
    password: str


@dataclasses.dataclass
class User_data:
    first_name: str
    last_name: str
    phone_number: str
    email: str
    password: str