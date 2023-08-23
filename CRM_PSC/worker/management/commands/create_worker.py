import sqlite3
import random

from django.core.management import BaseCommand

from datetime import datetime, timedelta
from worker.models import Worker
from mimesis.builtins import RussiaSpecProvider
from mimesis import Transport, Locale
# from mimesis.

from faker import Faker

from structure_of_company.models import Affiliated_company
from document.models import (Passport,
                             Driving_license,
                             Security_license,
                             Medical_certificate,
                             Periodic_inspection,
                             Electrical_certificate,
                             Insurance_policy,
                             Vehicle_passport,
                             Registration_certificate
                             )

from vehicle.models import Vehicle





#dt = Datetime()
fake = Faker('ru_RU')
ru_spec = RussiaSpecProvider()
transport = Transport()

class Command(BaseCommand):
    """
    Creates workers
    """

    def handle(self, *args, **options):
        # conn = sqlite3.connect(r'C:\Users\Себастьян Перейро\Documents\GitHub\CRM_for_private_security_company\CRM_PSC\db.sqlite3')
        conn = sqlite3.connect('/home/andrey/PycharmProjects/CRM_for_private_security_company/CRM_PSC/db.sqlite3')
        # conn = sqlite3.connect('/home/einsatz174/CRM_for_private_security_company/CRM_PSC/db.sqlite3')
        # cursor = conn.cursor()
        self.stdout.write("Create firm")
        x = 5
        companies = []  # Переменная для хранения созданных компаний
        for _ in range(x):
            affiliated_company, created = Affiliated_company.objects.get_or_create(
                name=fake.company(),
                address=fake.address()[:-8],
                phone=83511112233,
                email='example@mail.ru',
                director=f"{fake.last_name_male()} {fake.first_name_male()[0]}.{fake.middle_name_male()[0]}.",
                contact_person=f"{fake.last_name_male()} {fake.first_name_male()[0]}.{fake.middle_name_male()[0]}.",
                phone_contact_person=89991112233,
            )
            companies.append(affiliated_company)  # Сохраняем созданную компанию

        self.stdout.write(self.style.SUCCESS(f"{x} affiliated_company created"))

        self.stdout.write("Create auto")
        x1 = 15
        for _ in range(x1):
            owner_company = random.choice(companies)
            license_plate = f'A{random.randint(100, 999)}TC174RUS'
            VIN_number = f'{random.randint(10000000, 99999999)}'
            name = transport.car()

            date_issue = fake.date_between(start_date="-{}y".format(7), end_date="today")
            vehicle_passport, created = Vehicle_passport.objects.get_or_create(
                owner=owner_company,
                VIN_number=VIN_number,
                license_plate=license_plate,
                series_and_number=ru_spec.series_and_number(),
                date_issue=date_issue,
            )

            date_issue = fake.date_between(start_date="-{}y".format(15), end_date="today")
            registration_certificate, created = Registration_certificate.objects.get_or_create(
                owner=owner_company,
                license_plate=license_plate,
                series_and_number=ru_spec.series_and_number(),
                date_issue=date_issue,
            )

            date_issue = fake.date_between(start_date="-{}y".format(1), end_date="today")
            expiration_date = date_issue + timedelta(days=365 * 10)
            insurance_policy, created = Insurance_policy.objects.get_or_create(
                owner=owner_company,
                vehicle=name,
                license_plate=license_plate,
                series_and_number=ru_spec.series_and_number(),
                date_issue=date_issue,
                date_expiration=expiration_date
            )

            vehicle, created = Vehicle.objects.get_or_create(
                name=name,
                VIN_number=VIN_number,
                license_plate=license_plate,
                owner_company=owner_company,
                date_manufacture=fake.date_between(start_date="-{}y".format(5), end_date="today"),
                receipt_date=fake.date_between(start_date="-{}y".format(5), end_date="today"),
                mileage=random.randint(1000, 99999),
                service_date=fake.date_between(start_date="-{}y".format(2), end_date="today"),
                engine_oil=random.choice(['Toyota', 'Shell', 'Castrol']),
                engine_oil_viscosity=random.choice(['0W-20', '5W-30', '5W-40']),
                insurance_policy_limit=random.choice(["Без ограничения", "Ограниченная"]),
                passport_copy=vehicle_passport,
                insurance_policy=insurance_policy,
                registration_certificate=registration_certificate,
            )


        self.stdout.write(self.style.SUCCESS(f"{x} insurance_policy and vehicles created"))

        n = 100

        for _ in range(n):
            gender = fake.random_element(['Male', 'Female'])  # Случайно выбираем мужской или женский пол

            if gender == 'Male':
                first_name = fake.first_name_male()  # Генерируем мужское имя
                second_name = fake.last_name_male()
                middle_name = fake.middle_name_male()
            else:
                first_name = fake.first_name_female()  # Генерируем женское имя
                second_name = fake.last_name_female()
                middle_name = fake.middle_name_female()


            date_issue = fake.date_between(start_date="-{}y".format(15), end_date="today")
            expiration_date = date_issue + timedelta(days=365 * 10)
            passport, created = Passport.objects.get_or_create(
                owner=f"{second_name} {first_name[0]}.{middle_name[0]}.",
                series_and_number=ru_spec.series_and_number(),
                date_issue=date_issue,
                date_expiration=expiration_date
            )
            date_issue = fake.date_between(start_date="-{}y".format(15), end_date="today")
            expiration_date = date_issue + timedelta(days=365 * 10)
            driving_license, created = Driving_license.objects.get_or_create(
                owner=f"{second_name} {first_name[0]}.{middle_name[0]}.",
                series_and_number=ru_spec.series_and_number(),
                date_issue=date_issue,
                date_expiration=expiration_date
            )
            date_issue = fake.date_between(start_date="-{}y".format(7), end_date="today")
            expiration_date = date_issue + timedelta(days=365 * 5)
            security_license, created = Security_license.objects.get_or_create(
                owner=f"{second_name} {first_name[0]}.{middle_name[0]}.",
                series_and_number=ru_spec.series_and_number(),
                date_issue=date_issue,
                date_expiration=expiration_date
            )
            date_issue = fake.date_between(start_date="-{}y".format(3), end_date="today")
            expiration_date = date_issue + timedelta(days=365)
            medical_certificate, created = Medical_certificate.objects.get_or_create(
                owner=f"{second_name} {first_name[0]}.{middle_name[0]}.",
                series_and_number=ru_spec.series_and_number(),
                date_issue=date_issue,
                date_expiration=expiration_date
            )
            date_issue = fake.date_between(start_date="-{}y".format(3), end_date="today")
            expiration_date = date_issue + timedelta(days=365)
            periodic_inspection, created = Periodic_inspection.objects.get_or_create(
                owner=f"{second_name} {first_name[0]}.{middle_name[0]}.",
                series_and_number=ru_spec.series_and_number(),
                date_issue=date_issue,
                date_expiration=expiration_date
            )
            date_issue = fake.date_between(start_date="-{}y".format(15), end_date="today")
            electrical_certificate, created = Electrical_certificate.objects.get_or_create(
                owner=f"{second_name} {first_name[0]}.{middle_name[0]}.",
                series_and_number=ru_spec.series_and_number(),
                date_issue=date_issue,
                test_date=fake.date_between(start_date="-{}y".format(6), end_date="today")
            )
            worker, created = Worker.objects.get_or_create(
                first_name=first_name,
                middle_name=middle_name,
                second_name=second_name,
                address=fake.address()[:-8],
                official_employment=random.choice(['True', 'False']),
                organization=random.choice(companies),  # Выбираем случайную компанию из сохраненных
                date_birth=fake.date_of_birth().strftime('%Y-%m-%d'),
                data_employment=fake.date_between(start_date="-{}y".format(5), end_date="today"),
                category=random.choice(['4', '5', '5', 'Нет разряда']),
                phone=83511112233,
                electrical_safety_qualification=random.choice(['1', '2', '3', '4', 'Нет разряда']),
                passport=passport,
                driving_license=driving_license,
                security_license=security_license,
                medical_certificate=medical_certificate,
                periodic_inspection=periodic_inspection,
                electrical_certificate=electrical_certificate
            )

        self.stdout.write(self.style.SUCCESS(f"{n} workers created"))






