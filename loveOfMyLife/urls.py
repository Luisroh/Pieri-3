from django.urls import path
from loveOfMyLife import views  

urlpatterns = [
    path('', "views/historia.html", name='home'), 
]
