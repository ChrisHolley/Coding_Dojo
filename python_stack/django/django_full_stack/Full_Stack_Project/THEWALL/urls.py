from django.urls import path
from . import views
urlpatterns = [
    path('', views.WALL),
    path('welcome', views.WALL),
    path('form_new_post', views.new_post),
    path('form_new_comment', views.new_comment),
    path('form_delete_comment', views.delete_comment),
]
