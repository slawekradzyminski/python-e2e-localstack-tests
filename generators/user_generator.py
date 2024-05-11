from faker import Faker

from api.data.register import User

fake = Faker()

def get_random_user() -> User:
    return User(
        username=fake.user_name(),
        password=fake.password(),
        email=fake.email(),
        firstName=fake.first_name(),
        lastName=fake.last_name(),
        roles=["ROLE_ADMIN", "ROLE_CLIENT"],
    )
