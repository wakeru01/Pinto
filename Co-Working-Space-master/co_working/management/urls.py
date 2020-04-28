"""co_working URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('member-registeration/', views.sign_up, name='member_registeration'),
    path('shop/', views.shop, name='shop'),
    path('add_menu/', views.add_menu, name='add_menu'),
    path('menu/', views.menu, name='menu'),
    path('menu/<int:menu_id>/', views.edit_menu, name='edit_menu'),

]
