from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return render(request, "index.html")
def displayFruit(request):
    return render(request, "fruits.html")
def checkout(request):
    print("Got Post Info*****************************")
    print(request.POST)
    # 'count': sum(strawberry + raspberry + apple)
    context= {
        "strawberry": request.POST['strawberry'],
        "raspberry": request.POST['raspberry'],
        "apple": request.POST['apple'],
        "firstName": request.POST['first_name'],
        "lastName": request.POST['last_name'],
        "student_id": request.POST['student_id'],
    }
    first_name = context['firstName']
    last_name = context['lastName']
    raspberry = context['raspberry']
    apple = context['apple']
    strawberry = context['strawberry']
    count = int(raspberry)+int(apple)+int(strawberry)
    print(f"Charging {first_name} {last_name} for {count}  {int(strawberry)+int(raspberry)+int(apple)} items ")
    return render(request, "checkout.html", context, "count")

