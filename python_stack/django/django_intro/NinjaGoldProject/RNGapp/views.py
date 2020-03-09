from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    if "counter" not in request.session:
        request.session['counter'] = 0
    request.session['counter'] += 1
    context = {
        "unique_id": get_random_string(length=32),
        "counter": request.session['counter'],
    }
    return render(request, "rng.html", context)
def reset(request): 
    request.session.flush()
    return redirect('/rng')