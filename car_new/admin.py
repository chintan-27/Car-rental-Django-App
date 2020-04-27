from django.contrib import admin
from .models import Carrent,Location,RentedCar
# Register your models here.
admin.site.register(Carrent)
admin.site.register(Location)
admin.site.register(RentedCar)
