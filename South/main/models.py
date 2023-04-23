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

    def occupancy_rate(self):
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
    

    def  get_birthday_tommorow(self):
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
    

    def get_popular_filial_type(self, type):
        """
        Возвращает какой филиал, берет чаще всего тип номера,
        который ввели
        """
        with connection.cursor() as cursor:
            cursor.execute('''
            select "Filials".title, B.count
            from (
	            select "Bookings".filial_id, count("Bookings".filial_id) as count
	            FROM (
                    select "Rooms".room_id
		            FROM "Rooms"
		            WHERE "Rooms". type_number = '%s'
                ) as R
	            join "Bookings" ON R.room_id = "Bookings".room_id
	            GROUP BY "Bookings".filial_id
	            ORDER BY count("Bookings".filial_id) DESC
	            LIMIT 1
	        ) as B
            join "Filials" ON "Filials".filial_id = B.filial_id
            ''', [type])

        return cursor.fetchone()
    

    def popular_type_rooms(self):
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
    

    def popular_rates(self):
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
    
    
    def unpopular_filial(self):
        """
        Возвращает самый не популярный филиал
        """
        with connection.cursor() as cursor:
            cursor.connection('''
            SELECT title, COUNT(*) AS count 
            FROM "Filials"
            JOIN "Bookings" 
            ON "Filials".filial_id = "Bookings".filial_id
            GROUP BY title
            ORDER BY count ASC
            LIMIT 1;
            ''')

        return cursor.fetchone()
    

    def services_in_rates_all(self):
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
        
        return cursor.fetchall()
    


class Bookings(models.Model):
    booking = models.IntegerField(primary_key=True)
    client = models.ForeignKey('Clients', models.DO_NOTHING, blank=True, null=True)
    filial = models.ForeignKey('Filials', models.DO_NOTHING, blank=True, null=True)
    arrival_date = models.DateField(blank=True, null=True)
    departue_date = models.DateField(blank=True, null=True)
    room = models.ForeignKey('Rooms', models.DO_NOTHING, blank=True, null=True)
    rate = models.ForeignKey('Rates', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Bookings'
    
    def __str__(self) -> str:
        return self.booking


class Clients(models.Model):
    client_id = models.IntegerField(primary_key=True)
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
    number = models.IntegerField(blank=True, null=True)
    type_number = models.CharField(blank=True, null=True)
    busy = models.BooleanField(blank=True, null=True)
    client = models.ForeignKey(Clients, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Rooms'
    
    def __str__(self) -> str:
        return self.number


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


class ServicesInRates(models.Model):
    id = models.IntegerField(primary_key=True)
    rate = models.ForeignKey(Rates, models.DO_NOTHING, blank=True, null=True)
    service = models.ForeignKey(Services, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Services_in_rates'


class Workers(models.Model):
    worker_id = models.IntegerField(primary_key=True)
    name = models.CharField(blank=True, null=True)
    post = models.CharField(blank=True, null=True)
    phone = models.CharField(blank=True, null=True)
    email = models.CharField(blank=True, null=True)
    address = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Workers'
    

    def __str__(self) -> str:
        return self.name

