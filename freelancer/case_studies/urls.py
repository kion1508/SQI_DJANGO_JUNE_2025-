from django.urls import path
from . import views
urlpatterns=[
    path('case_studies/',views.case_studies,name='case_studies')
]