from faker import Faker
import random
import json
import psycopg2
import datetime

connection = psycopg2.connect(user="postgres",
                                  # пароль, который указали при установке PostgreSQL
                                  password="1234",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="South")
cursor = connection.cursor()


def generate_patients(faker):
    print(10*'-' + "START GENERATE PATIENTS" + 10 * '-')
    for _ in range(10_000_000):
        first_name = faker.first_name()
        last_name = faker.last_name()
        birthdate = faker.date_of_birth(minimum_age=20)
        gender = random.choice(("Male", "Female"))
        address = faker.address()
        phone_number = faker.phone_number()
        email = faker.email()
        reservation_id = random.randint(1, 1000)
        room_id = random.randint(1,1000)
        doctor_id = random.randint(1, 300)
        appointment_id = random.randint(1, 1000)
        meal_id = random.randint(1, 100)
        filial_id = random.randint(1, 200)
        rate_id = random.randint(1, 5)
        cursor.execute(f"""INSERT INTO "Patients" (first_name, last_name, birthdate, gender, address, phone_number, 
                            email, room_id, doctor_id, reservation_id, appointment_id, meal_id, filial_id, rate_id)
                          VALUES ('{first_name}', '{last_name}', '{birthdate}', '{gender}', '{address}, '{phone_number}',
                          '{email}', {room_id}, {doctor_id}, {reservation_id}, {appointment_id}, {meal_id}, {filial_id}, {rate_id})
                        """)
        connection.commit()
    print(10 * '-' + "END GENERATE PATIENTS")


def generate_appointments(faker):
    print(10 * '-' + "START GENERATE APPONTMENTS" + 10 * '-')
    for _ in range(1000):
        doctor_id = random.randint(1, 300)
        procedure_id = random.randint(1, 99)
        appointment_date = faker.date_between(start_date="today", end_date="+10y")
        appointment_time = faker.time()
        cursor.execute(f"""INSERT INTO "Appointments" (doctor_id, procedure_id, appointment_date, appointment_time)
                          VALUES ({doctor_id}, {procedure_id}, '{appointment_date}', '{appointment_time}')
                        """)
        connection.commit()
    print(10 * '-' + "END GENERATE APPONTMENTS" + 10 * '-')


def generate_doctors(faker):
    print(10 * '-' + "START GENERATE DOCTORS" + 10 * '-')
    with open("json_files/specialization.json", "r", encoding="utf-8") as f:
        dict_specialization = json.load(f)
    for _ in range(300):
        id_spec = random.randint(1, 21)
        specialization = dict_specialization[id_spec]
        first_name = faker.first_name()
        last_name = faker.last_name()
        phone_number = faker.phone_number()
        email = faker.email()
        cursor.execute(f"""INSERT INTO "Doctors" (first_name, last_name, specialization, phone_number, email)
                          VALUES ('{first_name}', '{last_name}', '{specialization}', '{phone_number}', '{email}')
                        """)
        connection.commit()
    print(10 * '-' + "END GENERATE DOCTORS" + 10 * '-')


def generate_rooms(faker:Faker):
    print(10*'-' + 'GENERATE ROOMS START' + 10*'-')
    set_level_room = ("Эконом", "Полулюкс", "Люкс", "Презедентский", "Дом")
    for i in range(1000):
        id = i + 1
        type_number = random.choice(set_level_room)
        number = id
        busy = random.choice((True, False))
        capacity = random.randint(1,4)
        cursor.execute(f"""INSERT INTO "Rooms" (room_number, room_type, capacity, busy)
                          VALUES ({number}, '{type_number}', {capacity}, {busy})
                        """)
        connection.commit()
    print(10*'-' + 'GENERATE ROOMS FINISH' + 10*'-')


def generate_reservations(faker):
    print(10 * '-' + "START GENERATE RESERVATIONS" + 10 * '-')
    for _ in range(1000):
        check_in_date = faker.date_between(start_date="today", end_date="+10y")
        check_out_date = faker.date_between(start_date=check_in_date, end_date="+10y")
        total_price = random.randint(5000, 50000)
        cursor.execute(f"""INSERT INTO "Reservations" (check_in_date, check_out_date, total_price)
                          VALUES ('{check_in_date}', '{check_out_date}', {total_price})
                        """)
        connection.commit()
    print(10 * '-' + "END GENERATE RESERVATIONS" + 10 * '-')


def generate_meals(faker):
    print(10 * '-' + "START GENERATE MEALS" + 10 * '-')
    with open("json_files/descriptions.json", "r", encoding="utf-8") as f:
        dict_desription = json.load(f)
    for key, desctription in dict_desription.items():
        meal_type = faker.random_element(elements=('Завтрак', 'Обед', 'Ужин'))
        price = random.randint(500, 5000)
        cursor.execute(f"""INSERT INTO "Meals" (meal_type, description, price)
                          VALUES ('{meal_type}', '{desctription}', {price})
                        """)
        connection.commit()
    print(10 * '-' + "END GENERATE MEALS" + 10 * '-')


def generate_filials(faker: Faker):
    print(10*'-' + 'GENERATE FILIALS START' + 10*'-')
    for i in range(200):
        filial_name = faker.company()
        address = faker.address()
        phone_number = faker.phone_number()
        cursor.execute(f"""INSERT INTO "Filials" (filial_name, address, phone_number)
                          VALUES ('{filial_name}', '{address}', '{phone_number}')
                        """)
        connection.commit()
    print(10*'-' + 'GENERATE FILIALS FINISH' + 10*'-')    
        

def generate_rates():
    print(10*'-' + 'GENERATE RATES START' + 10*'-')
    with open("json_files/rates.json", "r", encoding="utf-8") as f:
        dict_rates = json.load(f)
    prices = (5000, 7000, 4000, 8000, 50000)
    index = 0
    for key, value in dict_rates.items():
        rate_name = key
        description = value
        price = prices[index]
        index += 1
        cursor.execute(f""" INSERT INTO "Rates" (rate_name, description, price)
                           VALUES ('{rate_name}', '{description}', '{price}')
                        """)
        connection.commit()
    print(10*'-' + 'GENERATE RATES FINISH' + 10*'-')


def generate_procedures(faker: Faker):
    print(10*'-' + 'GENERATE SERVICES START' + 10*'-')
    with open("json_files/service.json", "r", encoding="utf-8") as f:
        dict_services = json.load(f)
    for key, value in dict_services.items():
        procedure_name = key
        description = value
        price = random.randint(500, 5000)
        cursor.execute(f"""INSERT INTO "Services" (procedure_name, description, price)
                          VALUES ('{procedure_name}', '{description}', '{price}')
                        """)
        connection.commit()
    print(10*'-' + 'GENERATE SERVICES FINISH' + 10*'-')
        
        

def main():
    faker = Faker(locale='ru_RU')
    generate_procedures(faker)
    generate_rates()
    generate_filials(faker)
    generate_meals(faker)
    generate_reservations(faker)
    generate_rooms(faker)
    generate_doctors(faker)
    generate_appointments(faker)
    generate_patients(faker)


if __name__ == "__main__":
    main()
