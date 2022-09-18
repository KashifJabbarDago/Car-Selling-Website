
from django.db import models

# Create your models here.
class OwnSellCars(models.Model):
    unique_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=150,default='')
    car_name = models.CharField(max_length=200)
    owner_number = models.CharField(max_length=150)
    owner_location = models.TextField()
    car_model = models.CharField(max_length=50)
    car_color = models.CharField(max_length=50)
    uploading_date = models.DateField()
    price = models.CharField(max_length=200,default='')
    image = models.ImageField(upload_to='ownercars/',default='')

    def __str__(self):
        return self.car_name

class CustomersCarForSell(models.Model):
    unique_id = models.AutoField(primary_key=True)
    customer_car_category = models.CharField(max_length=150,default='')
    customer_car_name = models.CharField(max_length=200)
    customer_number = models.CharField(max_length=150)
    customer_location = models.TextField()
    customer_car_model = models.CharField(max_length=50)
    customer_car_color = models.CharField(max_length=50)
    customer_uploading_date = models.DateField()
    customer_car_price = models.CharField(max_length=200,default='')
    customer_car_image = models.FileField(upload_to='customercar/')

    def __str__(self):
        return self.customer_car_name




