from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from datetime import datetime

Customer = get_user_model()

class Command(BaseCommand):
    help = 'Create a superuser with additional customer fields'

    def handle(self, *args, **options):
        username = input("Username: ")
        email = input("Email: ")
        password = input("Password: ")
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        birthday_str = input("Birthday (YYYY-MM-DD): ")
        birthday = datetime.strptime(birthday_str, "%Y-%m-%d").date()
        address = input("Address: ")
        city = input("City: ")
        house_number = input("House Number: ")
        postal_code = input("Postal Code: ")
        country = input("Country: ")
        phone_number = input("Phone Number: ")

        Customer.objects.create_superuser(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            birthday=birthday,
            address=address,
            city=city,
            house_number=house_number,
            postal_code=postal_code,
            country=country,
            phone_number=phone_number
        )

        self.stdout.write(self.style.SUCCESS(f'Superuser {username} created successfully'))