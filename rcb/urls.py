from rcb.views import *
from django.urls import path

urlpatterns=[
    path('caption/',caption,name='caption'),
]