from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Carrent(models.Model):
    car_name = models.CharField(max_length=250)
    id = models.AutoField(primary_key=True)
    car_color=models.CharField(max_length=250,null=True)
    transmission_type=models.CharField(max_length=250,null=True)
    fuel_type=models.CharField(max_length=250,null=True)
    costperday = models.IntegerField(null=True)
    car_num = models.CharField(max_length=20)
    car_image=models.ImageField(null=True,blank=True)


    def __str__(self):
        return self.car_name


class Location(models.Model):

    location=models.CharField(max_length=250)
    pickup=models.CharField(max_length=250)
    id = models.AutoField(primary_key=True)



    def __str__(self):
        return self.location

class RentedCar(models.Model):
    username_id = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.CharField(max_length=20)
    car_num = models.CharField(max_length=20)

    def __str__(self):
        return self.username_id
