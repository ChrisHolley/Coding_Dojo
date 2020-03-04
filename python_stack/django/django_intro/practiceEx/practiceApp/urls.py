from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	 
    path('new/', views.new),  
    path('create/', views.create),  
    path('<int:blogId>/', views.show),
    path('<int:blogId>/edit/', views.edit),
    path('<int:blogId>/delete/', views.destroy),
    path('name/<str:name>/', views.name)
]