from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return render(request, "index.html")
def displayFruit(request):
    return render(request, "fruits.html")
def checkout(request):
    print("Got Post Info*****************************")
    print(request.POST)
    # use this to create a variable that can be plugged in html {{ item_counter }} dont forget to use migration command on server
    request.session['item_counter'] = int(request.POST['strawberry']) + int(request.POST['raspberry']) + int(request.POST['apple'])
    context= {
        "strawberry": request.POST['strawberry'],
        "raspberry": request.POST['raspberry'],
        "apple": int(request.POST['apple']),
        "firstName": request.POST['first_name'],
        "lastName": request.POST['last_name'],
        "student_id": request.POST['student_id'],
    }
    first_name = context['firstName']
    last_name = context['lastName']
    raspberry = int(context['raspberry'])
    apple = int(context['apple'])
    strawberry = int(context['strawberry'])
    count_int = apple + strawberry + raspberry
    count = int(raspberry)+int(apple)+int(strawberry)
    print(f"Charging {first_name} {last_name} for {count_int} {count}  {int(strawberry)+int(raspberry)+int(apple)} items ")
    return render(request, "checkout.html", context)

