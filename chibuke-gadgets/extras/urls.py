from django.urls import path
from . import views
urlpatterns=[
    path('us/',views.extras,name='us'),
]