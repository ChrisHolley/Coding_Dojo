from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
import bcrypt
# from .models import NAME_OF_YOUR_MODEL_HERE
#render
def LOGIN_REGISTRATION(request):
        return render(request, ('dojoReadsLogin.html'))