from django.db import models
from django.conf import settings
# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=16)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    phone_number = models.PhoneNumberField("null=False, blank=False, unique=True")

class Member(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length=30)
    money = models.IntegerField()

class Zone(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    price = models.IntegerField()
    available_seat = models.IntegerField()

class SeatBooking(models.Model):
    member = models.ForeignKey(Member, null=True, on_delete=models.CASCADE)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    time_check_in = models.DateTimeField(auto_now=True)
    time_check_out = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    total_price = models.IntegerField(null=True)
    create_date = models.DateField(auto_now=True)
    create_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class TopupLog(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    topup_date = models.DateTimeField(auto_now=True)
    topup_by = models.ForeignKey(User, on_delete=models.CASCADE)

class Menu(models.Model):
    
