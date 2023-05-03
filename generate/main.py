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


def generate_bookings(faker: Faker):
    print(10*'-' + 'GENERATE BOOKINGS START' + 10*'-')

    cursor.execute("""
                       SELECT room_id 
                       FROM "Rooms"
                       WHERE "Rooms".busy is False;
                       """)
    not_busy_room = cursor.fetchall()
    count_not_busy_room = len(not_busy_room)

    cursor.execute("""
        SELECT cl.client_id
        FROM "Clients" cl
        WHERE NOT EXISTS (SELECT
		        		  FROM "Rooms"
				          WHERE client_id = cl.client_id);
    """)

    not_busy_clients = cursor.fetchall()
    count_not_busy_clients = len(not_busy_clients)

    for i in range(10_000):
        id = i + 1
        client = not_busy_clients[random.randint(1, count_not_busy_clients - 1)]
        client_id = client[0]
        filial_id = random.randint(1,200)
        rate_id = random.randint(1,5)
        room = not_busy_room[random.randint(1, count_not_busy_room - 1)]
        room_id = room[0]
        arrival_date = faker.date_between(start_date="today", end_date="+10y")
        departue_date = faker.date_between(start_date=arrival_date, end_date="+10y")

        cursor.execute(f"""INSERT INTO "Bookings" (booking_id, client_id, filial_id, room_id, rate_id, arrival_date, departue_date)
                          VALUES ({id}, {client_id}, {filial_id}, {room_id}, {rate_id}, '{arrival_date }', '{departue_date}')
                        """)
        connection.commit()
        
    print(10*'-' + 'GENERATE BOOKINGS FINISH' + 10*'-')


def generate_rooms(faker:Faker):
    """
    Генерация номеров. Надо учитывать что первая цифра номера
    является количество спальных мест. Также если номер не занят,
    то поле client_id будет пустым
    """
    print(10*'-' + 'GENERATE ROOMS START' + 10*'-')
    set_level_room = ("Эконом", "Полулюкс", "Люкс", "Презедентский", "Дом")
    for i in range(1000):
        id = i + 1
        type_number = random.choice(set_level_room)
        number = id
        busy = random.choice((True, False))
        if busy:
            client_id = random.randint(1, 10_000_000)
        else:
            client_id = "NULL"
        cursor.execute(f"""INSERT INTO "Rooms" (room_id, number, type_number, busy, client_id)
                          VALUES ({id}, {number}, '{type_number}', {busy}, {client_id})
                        """)
        connection.commit()
    print(10*'-' + 'GENERATE ROOMS FINISH' + 10*'-')


def generate_clients(faker: Faker):
    print(10*'-' + 'GENERATE CLIENTS START' + 10*'-')
    count_workers = 0
    for i in range(10_000_000):
        worker = False
        id = i + 1
        name = faker.name()
        birthday = faker.date_between(start_date = "-70y", end_date="-10y")
        if count_workers < 500:
            worker = random.choices((True, False), weights=[5,100])[0]
            if worker:
                count_workers += 1
                birthday = faker.date_between(start_date = "-50y", end_date="-20y")
        gender = random.choice(("Man", "Woman"))
        phone = faker.phone_number()
        email = faker.ascii_free_email()
        cursor.execute(f"""INSERT INTO "Clients" (client_id, worker,name, birthday, gender, phone, email)
                          VALUES ({id}, '{worker}', '{name}', '{birthday}', '{gender}', '{phone}', '{email}')
                        """)
        connection.commit()
    print(10*'-' + 'GENERATE CLIENTS FINISH' + 10*'-')


def generate_filials(faker: Faker):
    print(10*'-' + 'GENERATE FILIALS START' + 10*'-')
    for i in range(200):
        id = i + 1
        title = faker.company()
        address = faker.address()
        phone = faker.phone_number()
        email = faker.ascii_free_email()
        cursor.execute(f"""INSERT INTO "Filials" (filial_id, title, address, phone, email)
                          VALUES ({id}, '{title}', '{address}', '{phone}', '{email}')
                        """)
        connection.commit()
    print(10*'-' + 'GENERATE FILIALS FINISH' + 10*'-')


def generate_services_in_rates():
    print(10*'-' + 'GENERATE SERVICES_IN_RATES START' + 10*'-')
    for i in range(100):
        id = i + 1
        rate_id = random.randint(1,5)
        service_id = random.randint(1,99)
        cursor.execute(f"""INSERT INTO "Services_in_rates" (id, rate_id, service_id) 
                       VALUES ({id}, {rate_id}, {service_id})""")
        connection.commit()
    print(10*'-' + 'GENERATE SERVICES_IN_RATES FINISH' + 10*'-')
        

def generate_rates():
    print(10*'-' + 'GENERATE RATES START' + 10*'-')
    with open("json_files/rates.json", "r", encoding="utf-8") as f:
        dict_rates = json.load(f)
    id = 0
    prices = (5000, 7000, 4000, 8000, 50000)
    index = 0
    for key, value in dict_rates.items():
        id += 1
        title = key
        description = value
        price = prices[index]
        index += 1
        cursor.execute(f""" INSERT INTO "Rates" (rate_id, title, description, price)
                           VALUES ({id}, '{title}', '{description}', '{price}')
                        """)
        connection.commit()
    print(10*'-' + 'GENERATE RATES FINISH' + 10*'-')



def generate_services(faker: Faker):
    print(10*'-' + 'GENERATE SERVICES START' + 10*'-')
    with open("json_files/service.json", "r", encoding="utf-8") as f:
        dict_services = json.load(f)
    id = 0
    for key, value in dict_services.items():
        id += 1
        title = key
        description = value
        price = random.randint(500, 5000)
        cursor.execute(f"""INSERT INTO "Services" (service_id, title, description, price)
                          VALUES ({id}, '{title}', '{description}', '{price}')
                        """)
        connection.commit()
    print(10*'-' + 'GENERATE SERVICES FINISH' + 10*'-')


def generate_services_in_bookings():
    print(10*'-' + 'GENERATE SERVICES_IN_BOOKINGS START' + 10*'-')
    for i in range(1_000):
        id = i
        booking_id = random.randint(0,10_000)
        cursor.execute(f"""
        SELECT rate_id
        FROM "Bookings"
        WHERE booking_id = {booking_id}
        """)
        rate = cursor.fetchone()[0]
        cursor.execute(f"""
            SELECT s.service_id AS service_title
            FROM "Services_in_rates" AS sr
            JOIN "Services" AS s ON sr.service_id = s.service_id
            JOIN "Rates" AS r ON sr.rate_id = {rate}
        """)
        query_services = cursor.fetchall()
        services = [service[0] for service in query_services]
        service = random.randint(1, 99)
        while service in services:
            service = random.randint(1, 99)
        cursor.execute(
            f"""
            INSERT INTO "Services_in_bookings" ("id", "booking_id", "service_id")
            VALUES ({id}, {booking_id}, {service})
            """
            )
        connection.commit()
    print(10*'-' + 'GENERATE SERVICES_IN_BOOKINGS FINISH' + 10*'-')
        
        


def generate_workers_in_services():
    print(10*'-' + 'GENERATE workers_in_services START' + 10*'-')
    cursor.execute(f"""
                            SELECT client_id
                            FROM "Clients"
                            WHERE worker = true;
                            """)
    workers = cursor.fetchall()
    id = 0
    for worker in workers:
        worker_id = worker[0]
        service_id = random.randint(1, 99)
        cursor.execute(f"""
        INSERT INTO "Workers_in_services" ("Workers_in_services_id", "cleint_id", "service_id")
        VALUES ({id}, {worker_id}, {service_id})
        """)
        connection.commit()
        id += 1
    print(10*'-' + 'GENERATE workers_in_services FINISH' + 10*'-')


def main():
    faker = Faker(locale='ru_RU')
    # generate_services(faker)
    # generate_rates()
    # generate_services_in_rates()
    # generate_filials(faker)
    # generate_clients(faker)
    # generate_rooms(faker)
    # generate_workers_in_services()
    # generate_bookings(faker)
    generate_services_in_bookings()

if __name__ == "__main__":
    main()
