from django.shortcuts import render, HttpResponse, redirect
from .models import *
def index(request):
    context = {
        "Ninja": ninjas.objects.all(),
        "Dojos": dojos.objects.all(),
    }
    return render(request, "index.html", context)
def add_dojo(request):
    name = request.POST['dojo_name']
    city = request.POST['dojo_city']
    state = request.POST['dojo_state']
    desc = request.POST['dojo_desc']
    dojos.objects.create(name=name, city=city, state=state, desc=desc)
    return redirect('/')




