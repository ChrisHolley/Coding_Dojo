from django.urls import path
from . import views
urlpatterns = [
    path('', views.bookpage),
    path('addBook', views.addBook),
    path('<int:bookID>', views.viewBook)
]