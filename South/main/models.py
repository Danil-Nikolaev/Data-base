# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.db import connection



class LocalSqlQueries:

    """
    Класс с сырыми sql заросами
    """

    def patients_with_appointment():
        """
        Получить список всех пациентов, у которых есть назначенные процедуры
        """
        with connection.cursor() as curscor:
            curscor.execute('''
                            SELECT *
                            FROM "Patients"
                            WHERE EXISTS (
                            SELECT 1
                            FROM "Appointments"
                            WHERE "Appointments"."appointment_id" = "Patients"."appointment_id"
                            )
                            limit 1000;
                            
                            ''')
            return curscor.fetchall()
    

    def  procedure_high_price():
        """
        Получить список всех процедур, которые стоят дороже средней стоимости всех процедур:
        """
        with connection.cursor() as cursor:
            cursor.execute('''
                    SELECT *
                    FROM "Procedures"
                    WHERE "price" > (
                    SELECT AVG("price")
                    FROM "Procedures"
                    );
            ''')
            return cursor.fetchall()
    

    def doctors_high():
        """
       Вывести список всех врачей, специализирующихся на процедурах с ценой выше средней цены по всем процедурам
        """
        with connection.cursor() as cursor:

            cursor.execute('''
                SELECT *
                FROM "Doctors"
                WHERE "doctor_id" IN (
                SELECT DISTINCT "doctor_id"
                FROM "Appointments"
                WHERE "procedure_id" IN (
                    SELECT "procedure_id"
                    FROM "Procedures"
                    WHERE "price" > (
                    SELECT AVG("price")
                    FROM "Procedures"
                    )
                )
                );
            ''')

            return cursor.fetchall()
    

    def doctors_with_appointment():
        """
        Получить список всех докторов, у которых есть назначенные пациенты
        """
        with connection.cursor() as cursor:
            cursor.execute('''
                SELECT *
                FROM "Doctors"
                WHERE "doctor_id" IN (
                SELECT DISTINCT "doctor_id"
                FROM "Patients"
                );
                ''')
        
            return cursor.fetchall()
    

    def patients_with_high_price_procedure():
        """
        Получить список всех пациентов, у которых есть назначенные процедуры, стоимость которых выше средней стоимости всех процедур
        """
        with connection.cursor() as cursor:
            cursor.execute('''
            SELECT "Patients".*
            FROM "Patients"
            JOIN "Appointments" ON "Appointments"."appointment_id" = "Patients"."appointment_id"
            JOIN "Procedures" ON "Procedures"."procedure_id" = "Appointments"."procedure_id"
            WHERE "Procedures"."price" > (
            SELECT AVG("price")
            FROM "Procedures"
            ) limit 1000;

            ''')
        
            return cursor.fetchall()
    
    
    def procedure_without_appointment():
        """
        Вывести список всех процедур, которые никогда не были назначены на встречу
        """
        with connection.cursor() as cursor:
            cursor.execute('''
            SELECT *
            FROM "Procedures"
            WHERE NOT EXISTS (
            SELECT *
            FROM "Appointments"
            WHERE "Procedures"."procedure_id" = "Appointments"."procedure_id"
            );
            ''')

            return cursor.fetchall()
    

    def patients_low_capacity():
        """
        Вывести список всех пациентов, которые забронировали комнату с наименьшей вместимостью
        """
        with connection.cursor() as cursor:
            cursor.execute('''
            SELECT *
            FROM "Patients"
            WHERE "room_id" IN (
            SELECT "room_id"
            FROM "Rooms"
            WHERE "capacity" = (
                SELECT MIN("capacity")
                FROM "Rooms"
            )
            ) limit 1000;
            ''')
        
            model = cursor.fetchall()
        return model
    

class Appointments(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    doctor = models.ForeignKey('Doctors', models.DO_NOTHING, blank=True, null=True)
    procedure = models.ForeignKey('Procedures', models.DO_NOTHING, blank=True, null=True)
    appointment_date = models.DateField(blank=True, null=True)
    appointment_time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Appointments'


class Doctors(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    specialization = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Doctors'


class Filials(models.Model):
    filial_id = models.AutoField(primary_key=True)
    filial_name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Filials'


class Meals(models.Model):
    meal_id = models.AutoField(primary_key=True)
    meal_type = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Meals'


class Patients(models.Model):
    patient_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    room = models.ForeignKey('Rooms', models.DO_NOTHING, blank=True, null=True)
    doctor = models.ForeignKey(Doctors, models.DO_NOTHING, blank=True, null=True)
    reservation = models.ForeignKey('Reservations', models.DO_NOTHING, blank=True, null=True)
    appointment = models.ForeignKey(Appointments, models.DO_NOTHING, blank=True, null=True)
    meal = models.ForeignKey(Meals, models.DO_NOTHING, blank=True, null=True)
    filial = models.ForeignKey(Filials, models.DO_NOTHING, blank=True, null=True)
    rate = models.ForeignKey('Rates', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Patients'


class Procedures(models.Model):
    procedure_id = models.AutoField(primary_key=True)
    procedure_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Procedures'


class Rates(models.Model):
    rate_id = models.AutoField(primary_key=True)
    rate_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Rates'


class Reservations(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    check_in_date = models.DateField(blank=True, null=True)
    check_out_date = models.DateField(blank=True, null=True)
    total_price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Reservations'


class Rooms(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_number = models.IntegerField(blank=True, null=True)
    room_type = models.CharField(max_length=50, blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    busy = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Rooms'