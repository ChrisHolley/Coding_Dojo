from django.urls import path
from . import views
urlpatterns = [
    path('', views.login),
    path('login', views.login),
    path('create_user', views.create_user),
    # path('welcome', views.welcome),
    path('logout', views.logout),
]