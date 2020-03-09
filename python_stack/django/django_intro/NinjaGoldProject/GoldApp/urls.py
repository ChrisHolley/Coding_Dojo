from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('gold_farm', views.gold_farm),
    path('gold_cave', views.gold_cave),
    path('gold_house', views.gold_house),
    path('gold_casino', views.gold_casino),
    path('reset', views.reset),
]