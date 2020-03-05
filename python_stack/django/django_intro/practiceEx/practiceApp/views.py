from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
    context = {
    	"name": "Noelle",
    	"favorite_color": "turquoise",
    	"pets": ["Bruce", "Fitz", "Georgie"],
    }
    return render(request, "index.html", context)
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")
def create(request):
    return HttpResponse("this is the create page")
def show(request, blogId):
    # return HttpResponse("placeholder to display blog number:{}".format(blogId))
    return HttpResponse(f"placeholder to display blog number:{blogId}")
def edit(request, blogId):
    return HttpResponse(f"placeholder to edit blog {blogId}")
def destroy(request, blogId):
    return redirect("/")
def name(request, name):
    context = {
        "htmlName": name,
        "namelist": ["Alfred", "Berry", "Celestine", "Dewbert"]
    }
    return render(request, "names.html", context)
def timedisplay(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request, "timedisplay.html", context)





