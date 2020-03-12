from django.urls import path
from . import views
urlpatterns = [
    path('', views.bookpage),
    path('addBook', views.addBook),
    path('<int:bookID>', views.viewBook),
    path('authorpage', views.authorpage),
    path('authorpage/<int:authorID>', views.viewAuthor),
    path('addAutherToBook', views.addAutherToBook),
    path('addAuthor', views.addAuthor),


]