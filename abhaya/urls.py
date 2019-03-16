from django.urls import path
from . import views

urlpatterns = [
path("",views.home,name="Home"),
path("ToBeMom",views.ToBeMom,name="ToBeMom"),
path("analyse",views.analyse,name="analyse"),
path("GovtSchemes",views.GovtSchemes,name="GovtSchemes"),  
path("Diet",views.Diet,name="Diet"),    
path("Excercise",views.Excercise,name="Excercise"),
path("videos",views.videos,name="videos"),
path("voice",views.voice,name="voice")

]