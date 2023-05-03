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

    def occupancy_rate():
        """
        Процент заполнености номеров
        """
        with connection.cursor() as curscor:
            curscor.execute('''
                            SELECT (
                            (SELECT count(*) 
                            FROM "Rooms" 
                            WHERE busy = true) 
                            * 100) / COUNT(*) AS occupancy_rate 
                            FROM "Rooms";
                            ''')
            return curscor.fetchone()
    

    def  get_birthday_tommorow():
        """
        Возвращает у кого завтра день рождение
        и в каком номере
        """
        with connection.cursor() as cursor:
            cursor.execute('''
                    SELECT B.name, "Rooms".number
                    FROM (SELECT "Clients".client_id, "Clients".name
                    FROM "Clients"
                    where (date_part('month',"Clients".birthday) = date_part('month' ,CURRENT_DATE)) 
                    and (date_part('day',"Clients".birthday) > date_part('day' ,CURRENT_DATE))
                    and ((date_part('day',"Clients".birthday) - date_part('day' ,CURRENT_DATE)) < 2)
                ) AS B
                JOIN "Rooms" ON B.client_id = "Rooms".client_id
            ''')
            return cursor.fetchall()
    

    def get_popular_filial_type():
        """
        Из какого филиала берут чаще какой тип номера
        """
        with connection.cursor() as cursor:
            # cursor.execute('''
            # select "Filials".title, B.count, B.type.number
            # from (
	        #     select "Bookings".filial_id, count("Bookings".filial_id) as count, "Rooms".type_number
	        #     FROM "Rooms" as R
	        #     join "Bookings" ON R.room_id = "Bookings".room_id
	        #     GROUP BY "Bookings".filial_id
	        #     ORDER BY count("Bookings".filial_id) DESC
	        # ) as B
            # join "Filials" ON "Filials".filial_id = B.filial_id
            # ''')
            cursor.execute('''
                SELECT f.title, r.type_number, COUNT(*) AS count 
                FROM "Filials" as f 
                JOIN "Bookings" as b 
                ON f.filial_id = b.filial_id 
                JOIN "Rooms" as r 
                ON r.room_id = b.room_id 
                GROUP BY f.title, r.type_number 
                ORDER BY count DESC;
            ''')

            return cursor.fetchall()
    

    def popular_type_rooms():
        """
        Возвращает самый популярный тип номера
        """
        with connection.cursor() as cursor:
            cursor.execute('''
                SELECT type_number, COUNT(*) AS count 
                FROM "Rooms" 
                GROUP BY type_number 
                ORDER BY count DESC 
                LIMIT 1;
                ''')
        
            return cursor.fetchone()
    

    def popular_rates():
        """
        Возвращает самый популярный тариф
        """
        with connection.cursor() as cursor:
            cursor.execute('''
            SELECT title, COUNT(*) AS count 
            FROM "Rates" 
            JOIN "Bookings" 
            ON "Rates".rate_id = "Bookings".rate_id 
            GROUP BY title
            ORDER BY count DESC 
            LIMIT 1;
            ''')
        
            return cursor.fetchone()
    
    
    def unpopular_filial():
        """
        Возвращает самый не популярный филиал
        """
        with connection.cursor() as cursor:
            cursor.execute('''
            SELECT title, COUNT(*) AS count 
            FROM "Filials"
            JOIN "Bookings" 
            ON "Filials".filial_id = "Bookings".filial_id
            GROUP BY title
            ORDER BY count ASC
            LIMIT 1;
            ''')

            return cursor.fetchone()
    

    def services_in_rates_all():
        """
        Возвращет связь тарифов и услуг включенные в эти тарифы
        """
        with connection.cursor() as cursor:
            cursor.execute('''
            SELECT r.title AS rate_title, s.title AS service_title
            FROM "Services_in_rates" AS sr
            JOIN "Services" AS s ON sr.service_id = s.service_id
            JOIN "Rates" AS r ON sr.rate_id = r.rate_id
            ORDER BY r.title;
            ''')
        
            model = cursor.fetchall()
        return model
    


class Bookings(models.Model):
    booking_id = models.IntegerField(primary_key=True)
    client = models.ForeignKey('Clients', models.DO_NOTHING, blank=True, null=True)
    filial = models.ForeignKey('Filials', models.DO_NOTHING, blank=True, null=True)
    room = models.ForeignKey('Rooms', models.DO_NOTHING, blank=True, null=True)
    rate = models.ForeignKey('Rates', models.DO_NOTHING, blank=True, null=True)
    arrival_date = models.DateField(blank=True, null=True)
    departue_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Bookings'
    
    def __str__(self) -> str:
        return self.booking_id


class Clients(models.Model):
    client_id = models.IntegerField(primary_key=True)
    worker = models.BooleanField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(blank=True, null=True)
    phone = models.CharField(blank=True, null=True)
    email = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Clients'
    

    def __str__(self) -> str:
        return self.name


class Comments(models.Model):
    comment_id = models.IntegerField(primary_key=True)
    client = models.ForeignKey(Clients, models.DO_NOTHING, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    assessment = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Comments'
    

    def __str__(self) -> str:
        return self.description


class Filials(models.Model):
    filial_id = models.IntegerField(primary_key=True)
    title = models.CharField(blank=True, null=True)
    address = models.CharField(blank=True, null=True)
    phone = models.CharField(blank=True, null=True)
    email = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Filials'
    

    def __str__(self) -> str:
        return self.title


class Rates(models.Model):
    rate_id = models.IntegerField(primary_key=True)
    title = models.CharField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Rates'
    

    def __str__(self) -> str:
        return self.title


class Rooms(models.Model):
    room_id = models.IntegerField(primary_key=True)
    client = models.ForeignKey(Clients, models.DO_NOTHING, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    type_number = models.CharField(blank=True, null=True)
    busy = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Rooms'
    

    def __str__(self) -> str:
        return self.room_id


class Services(models.Model):
    service_id = models.IntegerField(primary_key=True)
    title = models.CharField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Services'
    

    def __str__(self) -> str:
        return self.title


class ServicesInBookings(models.Model):
    id = models.IntegerField(primary_key=True)
    booking = models.ForeignKey(Bookings, models.DO_NOTHING, blank=True, null=True)
    service = models.ForeignKey(Services, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Services_in_bookings'


class ServicesInRates(models.Model):
    id = models.IntegerField(primary_key=True)
    rate = models.ForeignKey(Rates, models.DO_NOTHING, blank=True, null=True)
    service = models.ForeignKey(Services, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Services_in_rates'


class WorkersInServices(models.Model):
    workers_in_services_id = models.IntegerField(db_column='Workers_in_services_id', primary_key=True)  # Field name made lowercase.
    cleint = models.ForeignKey(Clients, models.DO_NOTHING, blank=True, null=True)
    service = models.ForeignKey(Services, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Workers_in_services'

