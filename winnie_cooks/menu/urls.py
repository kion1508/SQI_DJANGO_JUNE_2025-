from django.urls import path
from . import views

app_name='menu'

urlpatterns=[
    path('dishes',views.available_dishes,name='dishes'),
]