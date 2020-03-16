from django.urls import path
from . import views
urlpatterns = [
    path('', views.shows),
    path('shows/addShow', views.add_new_show),
    path('allShows', views.all_shows),
    path('showdetails', views.show_details),
]
