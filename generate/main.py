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

        cursor.execute(f"""INSERT INTO "Bookings" (booking, client_id, filial_id, arrival_date, departue_date, room_id, rate_id)
                          VALUES ({id}, {client_id}, {filial_id}, '{arrival_date}', '{departue_date}', {room_id}, {rate_id})
                        """)
        connection.commit()
        


def generate_rooms(faker:Faker):
    """
    Генерация номеров. Надо учитывать что первая цифра номера
    является количество спальных мест. Также если номер не занят,
    то поле client_id будет пустым
    """
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


def generate_clients(faker: Faker):
    for i in range(10_000_000):
        id = i + 1
        name = faker.name()
        birthday = faker.date_between(start_date = "-70y", end_date="-10y")
        gender = random.choice(("Man", "Woman"))
        phone = faker.phone_number()
        email = faker.ascii_free_email()
        cursor.execute(f"""INSERT INTO "Clients" (client_id, name, birthday, gender, phone, email)
                          VALUES ({id}, '{name}', '{birthday}', '{gender}', '{phone}', '{email}')
                        """)
        connection.commit()


def generate_filials(faker: Faker):
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


def generate_services_in_rates():
    for i in range(100):
        id = i + 1
        rate_id = random.randint(1,5)
        service_id = random.randint(1,99)
        cursor.execute(f"""INSERT INTO "Services_in_rates" (id, rate_id, service_id) 
                       VALUES ({id}, {rate_id}, {service_id})""")
        connection.commit()
        

def generate_rates():
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



def generate_services(faker: Faker):
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


def generate_workers(faker: Faker):
    """
    Функция для генерации персонала санаторно-курортного комплекса.
    """
    list_post = [ "Повар", "Консьерж", "Бухгалтер",
                 "Аниматор", "Официант", "Врач", 
                 "Администратор", "Охранник", "Медсестра", 
                 "Горничные", "Тренер", "Садовник"]
    
    for i in range(500):
        id = i + 1
        name = faker.name()
        post = random.choice(list_post)
        phone = faker.phone_number()
        email = faker.ascii_free_email()
        address = faker.address()
        cursor.execute(f"""INSERT INTO "Workers" (worker_id, name, post, phone, email, address) 
                           VALUES ({id}, '{name}', '{post}', '{phone}', '{email}', '{address}')
                       """)
        connection.commit()


def main():
    faker = Faker(locale='ru_RU')
    # generate_workers(faker)
    # generate_services(faker)
    # generate_rates()
    # generate_services_in_rates()
    # generate_filials(faker)
    # generate_clients(faker)
    # generate_rooms(faker)
    generate_bookings(faker)

if __name__ == "__main__":
    main()
