from django.urls import path     
from . import views
urlpatterns = [
    path('/', views.fruit),
    path('/testform', views.testform),	
    path('/user', views.create_user),   
]
