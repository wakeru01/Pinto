from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from management.models import User
#, Shop, Order, Order_List, Wallet, Transaction, Comment, Menu
# Register your models here.

admin.site.register(User, UserAdmin)
'''
admin.site.register(Shop)
admin.site.register(Order)
admin.site.register(Order_List)
admin.site.register(Wallet)
admin.site.register(Transaction)
admin.site.register(Comment)
admin.site.register(Menu)
'''



