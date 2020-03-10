from django.shortcuts import render, HttpResponse, redirect
import random


def index(request):
    if "gold" not in request.session:
        request.session['gold'] = 0
    context = {
        "gold_house": random.randrange(0, 10),
        "gold": request.session['gold'],
    }
    return render(request, "index.html", context)
def gold_farm(request):
    request.session['gold'] = random.randrange(10, 20) + request.session['gold']
    return redirect('/')
def gold_cave(request):
    request.session['gold'] = random.randrange(5, 10) + request.session['gold']
    return redirect('/')
def gold_house(request):
    request.session['gold'] = random.randrange(2, 5) + request.session['gold']
    return redirect('/')
def gold_casino(request):
    # if request.session['activityLog'] not in request.session:
    #     request.session['activityLog'] = []
    request.session['activityLog'] = []
    request.session['goldThisTurn'] = random.randrange(-50,50)
    request.session['gold'] = request.session['goldThisTurn'] + request.session['gold']
    request.session['activityLog'].append(f"Earned {request.session['goldThisTurn']} gold this turn")
    print(request.session['activityLog'])
    print(f"gold this turn: {request.session['goldThisTurn']}")
    return redirect('/')
def reset(request): 
    request.session.flush()
    return redirect('/')    