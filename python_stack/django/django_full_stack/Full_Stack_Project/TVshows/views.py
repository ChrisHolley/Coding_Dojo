from django.shortcuts import render

# RENDERS
def shows(request):
    return render(request, 'shows.html')

def add_new_show(request):
    return render(request, ('addShow.html'))

def all_shows(request):
    return render(request, ('shows.html'))

def show_details(request):
    return render(request, ('showDetails.html'))