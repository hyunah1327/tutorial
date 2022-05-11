from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
from django.db import models
class Curriculum(models.Model):
    name = models.CharField(max_length=255)

