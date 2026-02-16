from django.db import models

# Create your models here.

class Service(models.Model):
 name=models.CharField(max_length=100)
 price=models.DecimalField(max_digits=8,decimal_places=2)
 description=models.TextField()
 image = models.FileField(upload_to='service/', max_length=200, null=True, blank=False)

class Booking(models.Model):
 name=models.CharField(max_length=100)
 phone=models.CharField(max_length=20)
 address=models.TextField()
 service=models.CharField(max_length=100)
 pickup_date=models.DateField()
 pickup_time=models.TimeField()

class Product(models.Model):
 name=models.CharField(max_length=100)
 price=models.DecimalField(max_digits=9,decimal_places=2)
 image = models.FileField(upload_to='product/', max_length=200, null=True, blank=False)
#  image=models.URLField()
 description=models.TextField()

class Order(models.Model):
 reference=models.CharField(max_length=100)
 amount=models.DecimalField(max_digits=10,decimal_places=2)
 paid=models.BooleanField(default=False)