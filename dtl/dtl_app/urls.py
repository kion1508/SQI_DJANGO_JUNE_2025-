from django.urls import path
from . import views
urlpatterns=[
    path('messages',views.practice_dt1,name='messages'),
]