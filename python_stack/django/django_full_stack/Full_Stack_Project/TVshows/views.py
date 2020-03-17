from django.shortcuts import render, HttpResponse, redirect
from .models import Show

# RENDERS
def shows(request):
    context = {
        "shows_database" : Show.objects.all()
    }
    return render(request, 'shows.html', context)

def add_new_show(request):
    return render(request, 'addShow.html')

# def all_shows(request):
#     return render(request, ('shows.html'))

def show_details(request, show_id):
    context = {
        'show_info': Show.objects.get(id=show_id)
    }
    return render(request, 'showDetails.html', context)


#POSTs
def create_show(request):
    title = request.POST['form_title']
    network = request.POST['form_network']
    release = request.POST['form_release']
    desc = request.POST['form_desc']
    new_show = Show.objects.create(show_title=title, show_network=network, show_release=release, show_desc=desc)
    return redirect(f"/shows/details/{new_show.id}")

def show_edit(request, show_id):
    if request.method=='POST':
        edit_show = Show.objects.get(id=show_id)
        edit_show.show_title = request.POST['new_title']
        edit_show.show_network = request.POST['new_network']
        edit_show.show_release = request.POST['new_release']
        edit_show.show_desc = request.POST['new_desc']
        edit_show.save()
        return redirect(f"/shows/details/{edit_show.id}")
    context = {
        'show_info': Show.objects.get(id=show_id)
    }
    return render(request, 'editShow.html', context)


#Delete
def delete_show(request, show_id):
    delete_show = Show.objects.get(id=show_id)
    delete_show.delete()
    
    return redirect("/shows")