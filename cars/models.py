from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from common.models import BaseModel

# Create your models here.

class Car(BaseModel):
    class GearType(models.TextChoices):
        MANUAL = 'Manual'
        AVTO = 'Avto'
        HYBRID = 'Hybrid'

    name = models.CharField(max_length=100,null=False,blank=False)
    description = models.TextField(null=True,blank=True)
    price = models.PositiveIntegerField(null=False,blank=False)
    brand = models.ForeignKey('cars.Brand',on_delete=models.CASCADE,related_name='cars')
    year = models.PositiveIntegerField(validators=[
        MinValueValidator(1900),
        MaxValueValidator(2025)
    ])
    color = models.CharField(max_length=30)
    gear_type = models.CharField(choices=GearType.choices)
    distance_convered = models.PositiveIntegerField(null=False,blank=False)

    def __str__(self):
        return self.name


class Brand(BaseModel):
    name = models.CharField(max_length=100,null=False,blank=False)
    logo = models.ImageField(upload_to='logos',null=True,blank=True)

    def __str__(self):
        return self.name







