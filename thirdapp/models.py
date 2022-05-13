from django.db import models

# Create your models here.
from django.db import models
from django.db.models.fields import CharField, IntegerField
from django.db.models.fields import FloatField
from django.db.models.fields import DateField

class JejuOlle(models.Model):
    course = CharField(max_length=10)
    course_name = CharField(max_length=20)
    distance = FloatField()
    time_info = CharField(max_length=10)
    start_end_info = CharField(max_length=20)
    cre_date = DateField()
    class Meta:
        db_table = 'jeju_olle'
        managed = False

class Shop(models.Model):
    shop_id = IntegerField(primary_key=True)
    shop_name = CharField(max_length=100, null=True)
    shop_desc = CharField(max_length=100, null=True)
    rest_date = CharField(max_length=100, null=True)
    parking_info = CharField(max_length=100, null=True)
    img_path = CharField(max_length=255, null=True)
    class Meta:
        db_table = 'shop'
        app_label = 'thirdapp'
        managed = False

class Owner(models.Model):
    name = models.CharField(max_length=50, null=True)
    class Meta:
        db_table = 'owner'

class Animal(models.Model):
    name = models.CharField(max_length=50, null=True)
    age = models.IntegerField(null=True)
    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, null=True)
    class Meta:
        db_table = 'animal'

class Warranty(models.Model):
    model_nm = models.CharField(max_length=50, null=True)
    period = models.IntegerField(null=True)
    class Meta:
        db_table = 'warranty'

class Animal(models.Model):
    name = models.CharField(max_length=50, null=True)
    age = models.IntegerField(null=True)
    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, null=True)
    class Meta:
        db_table = 'animal'       
class Product(models.Model):
    name = models.CharField(max_length=50, null=True)
    price = models.IntegerField(null=True)
    animal = models.ForeignKey(Animal, on_delete=models.SET_NULL, null=True)
    warranty = models.OneToOneField(Warranty, on_delete=models.SET_NULL, null=True)
    class Meta:
        db_table = 'product'


        
class Playground(models.Model):
    name = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=50, null=True)
    tel = models.CharField(max_length=20, null=True)
    animals = models.ManyToManyField(Animal, null=True)
    class Meta:
        db_table = 'playground'
