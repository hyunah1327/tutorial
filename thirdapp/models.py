from turtle import distance
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