from email.policy import default

from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    '''
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=128)
    last_login = models.DateField()
    is_superuser = models.BooleanField()
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined =  models.DateField()
    email = models.EmailField(('email address'), unique=True)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    '''
    phone_number = models.CharField(max_length=10, default='')
    ADMIN = 'admin'
    CUSTOMER = 'customer'
    SHOP = 'shop'
    TYPE_CHOICES = (
        (ADMIN, 'admin'),
        (CUSTOMER, 'customer'),
        (SHOP, 'shop')
    )
    user_type = models.CharField(
        max_length=8,
        choices=TYPE_CHOICES,
        default=CUSTOMER,
    )
    

class Shop(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    review = models.TextField()
    OPEN = 'open'
    CLOSE = 'close'
    STATUS_CHOICES = (
        (OPEN, 'open'),
        (CLOSE, 'close'),
    )
    status = models.CharField(
        max_length=5,
        choices=STATUS_CHOICES,
        default=OPEN,
    )
    location = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    total_table = models.IntegerField(default='0')

class Menu(models.Model):
    menu_name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    menu_price = models.DecimalField(max_digits=8, decimal_places=3, default='0')
    image_url = models.CharField(max_length=255)

class Wallet(models.Model):
    amount = models.DecimalField(max_digits=8, decimal_places=3, default='0')
    user_id  = models.ForeignKey(User, on_delete=models.CASCADE, default='')

class Transaction(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    amount = models.DecimalField(max_digits=8, decimal_places=3, default='0')
    wallet_id_from = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    wallet_id_from =models.ForeignKey(Wallet, on_delete=models.CASCADE)

class Order(models.Model):   
    '''OPEN = 'open'
    CLOSE = 'close'
    STATUS_CHOICES = (
        (OPEN, 'open'),
        (CLOSE, 'close'),
    )
    status = models.CharField(
        max_length=5,
        choices=STATUS_CHOICES,
        default=OPEN,
    )'''
    IN_SHOP = 'in shop'
    BACKHOME = 'back home'
    ORDER_TYPE_CHOICES = (
        (IN_SHOP, 'in shop'),
        (BACKHOME, 'back home')
    )
    order_type = models.CharField(max_length=12,
        choices=ORDER_TYPE_CHOICES,
        default=IN_SHOP
    )
    ARRIVED = 'arrived'
    NOT_ARRIVAL = 'not_arrival'
    FINISHED = 'finished'
    STATUS_CHOICES = (
        (NOT_ARRIVAL, 'not arrival'), 
        (ARRIVED, 'arrived'),
        (FINISHED, 'finished')
    )
    status_type = models.CharField(max_length=12,
        choices=STATUS_CHOICES,
        default=ARRIVED
    )
    date_time = models.DateTimeField(auto_now=True)
    reserved_table = models.IntegerField(default="0")
    date_time_arrival = models.DateTimeField(auto_now=True)
    wallet_wallet_id = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default='')

class Order_List(models.Model):
    unit = models.IntegerField(null=True)
    price = models.DecimalField(max_digits=8, decimal_places=3, default='0')
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)

class Comment(models.Model):
    comment = models.TextField(max_length=255)
    score = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
