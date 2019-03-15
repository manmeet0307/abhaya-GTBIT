from django.urls import path
from . import views

urlpatterns = [
path("",views.home,name="Home"),
path("ToBeMom",views.ToBeMom,name="ToBeMom"),
path("analyse",views.analyse,name="analyse"),    
]