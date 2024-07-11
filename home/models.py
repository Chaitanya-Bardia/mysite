from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=100)
    age= models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    image = models.ImageField()
    file = models.FileField()

class car(models.Model):
    cname = models.CharField(max_length=100)
    speed= models.IntegerField()

    def __str__(self) -> str:
        return self.cname
    

@receiver(post_save, sender = car)   
def call_car_api(sender,instance,**kwargs):
    print("Car Object created successfully")
    print(sender,instance,kwargs)
