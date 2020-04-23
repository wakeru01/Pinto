from django.db import models
from django.conf import settings
# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=16)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=10, default='0')

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

class Shop(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField()
    # status = ((open, 'open'),(close, 'close'))
    location = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)

class Customer(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Admin(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Menu(models.Model):
    menu_name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    menu_pic = models.CharField(max_length=255)
    shop_shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)

class Wallet(models.Model):
    # amount = models.FloatField(max_length=8)
    history = models.CharField(max_length=255)
    user_id  = models.ForeignKey(User, on_delete=models.CASCADE)

class Image(models.Model):
    url = models.CharField(max_length=255)
    date = models.DateField(auto_now=True)
    menu_menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)

class Order(models.Model):
    # order_type = ((in_shop, 'in shop'),(backhome, 'back home'))
    date_time = models.DateTimeField(auto_now=True)
    # status = ((not_arrival, 'not arrival'),(arrived, 'arrived'))
    date_time_arrival = models.DateTimeField(auto_now=True)
    wallet_wallet_id = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    admin_user_id = models.ForeignKey(Admin, on_delete=models.CASCADE)

class Order_List(models.Model):
    # list_no = models.IntegerField(null=True) AI
    unit = models.IntegerField(null=True)
    # price = models.FloatField(max_length=8)
    order_order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)

class Customer_Shop(models.Model):
    date = models.DateField(auto_now=True)
    score = models.IntegerField(null=True)
    commend = models.TextField(max_length=255)
    shop_shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
    customer_user_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Transfering(models.Model):
    amount = models.FloatField(max_length=8)
    # ไม่แน่ใจ

class wallet_wallet(models.Model):
    wallet_wallet_id = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    transfer_id = models.ForeignKey(Transfering, on_delete=models.CASCADE)

class Table(models.Model):
    # amount = models.FloatField(max_length=10)
    # status = ((using, 'using'),(free, 'free'))
    shop_shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
    order_order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
