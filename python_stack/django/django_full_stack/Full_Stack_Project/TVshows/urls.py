from django.urls import path
from . import views
urlpatterns = [
    path('', views.shows),
    path('addShow', views.add_new_show),
    path('details/<int:show_id>', views.show_details),
    path('edit/<int:show_id>', views.show_edit),
    path('create', views.create_show),
    path('delete/<int:show_id>', views.delete_show),
]
