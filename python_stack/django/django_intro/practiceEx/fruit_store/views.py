from django.shortcuts import render, HttpResponse, redirect

def fruit(request):
    return render(request,"fruit.html")
def testform(request):
    return render(request, "testform.html")
def create_user(request):
    print("Got Post Info*****************************")
    print(request.POST)
    name_form_value = request.POST['form_name']
    print(name_form_value)
    context = {
        "name_form_value" : name_form_value,
    }
    return render(request, "testform_output.html", context)


