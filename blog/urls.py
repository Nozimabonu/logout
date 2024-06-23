from django.contrib import admin
from django.urls import path

from blog.views.views import index, product_detail, customers, customers_detail, delete_customer, add_customer, \
    update_customer
from blog.views.auth import login_page, logout_page, register

urlpatterns = [
    path('', index, name='index'),
    path('detail/<slug:slug>/', product_detail, name='product_detail'),
    path('customer/', customers, name='customers'),
    path('customers_detail/<int:pk>/', customers_detail, name='customers_detail'),
    path('delete/<int:pk>', delete_customer, name='delete'),
    path('add-customer/', add_customer, name='add_customers'),
    path('customer/<int:pk>/', update_customer, name='update_customer'),
    # authentication's url
    path('login-page/', login_page, name='login'),
    path('logout-page/', logout_page, name='logout'),
    path('register-page/', register, name='register')
]
