# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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

