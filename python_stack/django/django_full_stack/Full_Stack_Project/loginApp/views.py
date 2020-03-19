from django.shortcuts import render, redirect

from .models import user

#render
def login(request):
    return render(request, 'login.html')

#POST
def create_user(request):
    fname = request.POST['form_first_name']
    lname = request.POST['form_last_name']
    email = request.POST['form_email']
    birthday = request.POST['form_birthday']
    password = request.POST['form_password']
    user.objects.create(first_name=fname, last_name=lname, email=email, birthday=birthday, password=password)
    request.session['new_user.email'] = email
    return redirect("success")
