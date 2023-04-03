# Курсовая Работа по Базам данных.
## Тема: Санаторно - курортный комплекс 
## Диаграмма базы данных
![Диаграмма базы данных](/images/diagram.png)

## Скрипт создания таблиц в Postgresql
```
CREATE TABLE "Clients" (
  "client_id" integer PRIMARY KEY,
  "name" varchar,
  "series" varchar,
  "number" varchar,
  "birthday" varchar,
  "room_id" integer,
  "filial_id" integer,
  "rate_id" integer
);

CREATE TABLE "Rates" (
  "rate_id" integer PRIMARY KEY,
  "title" varchar,
  "feed" varchar,
  "room_level" varchar,
  "count_day" integer
);

CREATE TABLE "Filials" (
  "filial_id" integer PRIMARY KEY,
  "title" varchar,
  "address" varchar,
  "phone" varchar
);

CREATE TABLE "Rooms" (
  "room_id" integer PRIMARY KEY,
  "room_level" varchar,
  "busy" bool,
  "period" varchar
);

CREATE TABLE "Bookings" (
  "booking_id" integer PRIMARY KEY,
  "data_start" varchar,
  "data_end" varchar,
  "room_id" integer,
  "client_id" integer
);

CREATE TABLE "Workers" (
  "worker_id" integer PRIMARY KEY,
  "name" varchar,
  "post" varchar,
  "departament" varchar
);

CREATE TABLE "Procedures" (
  "procedure_id" integer PRIMARY KEY,
  "title" varchar,
  "worker_id" integer,
  "rate_id" integer
);

CREATE TABLE "Paid_procedures" (
  "paid_procedure_id" integer PRIMARY KEY,
  "title" varchar,
  "cost" integer,
  "worker_id" integer
);

ALTER TABLE "Paid_procedures" ADD FOREIGN KEY ("worker_id") REFERENCES "Workers" ("worker_id");

ALTER TABLE "Procedures" ADD FOREIGN KEY ("rate_id") REFERENCES "Rates" ("rate_id");

ALTER TABLE "Procedures" ADD FOREIGN KEY ("worker_id") REFERENCES "Workers" ("worker_id");

ALTER TABLE "Bookings" ADD FOREIGN KEY ("room_id") REFERENCES "Rooms" ("room_id");

ALTER TABLE "Bookings" ADD FOREIGN KEY ("client_id") REFERENCES "Clients" ("client_id");

ALTER TABLE "Clients" ADD FOREIGN KEY ("room_id") REFERENCES "Rooms" ("room_id");

ALTER TABLE "Clients" ADD FOREIGN KEY ("filial_id") REFERENCES "Filials" ("filial_id");

ALTER TABLE "Clients" ADD FOREIGN KEY ("rate_id") REFERENCES "Rates" ("rate_id");
```
