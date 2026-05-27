from faker import Faker
class Credentials:
    def generate_name(self):
        fake = Faker()
        return fake.name()

    def generate_password(self):
        fake = Faker()
        return fake.password()

    def generate_email(self):
        fake = Faker()
        return fake.email()