from django.urls import path
from loveOfMyLife import views

urlpatterns = [
    path('', views.home, name='home'),
]