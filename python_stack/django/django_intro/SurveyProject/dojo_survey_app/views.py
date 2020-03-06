from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request,"index.html")
def create_user(request):
    print("Got Post Info*****************************")
    print(request.POST)
    name_form_value = request.POST['form_name']
    location_form_value = request.POST['form_location']
    lang_form_value = request.POST['form_lang']
    
    print(name_form_value)
    context = {
        "name_form_value" : name_form_value,
        "location_form_value" : location_form_value,
        "lang_form_value" : lang_form_value
    }
    return render(request, "user.html", context)
