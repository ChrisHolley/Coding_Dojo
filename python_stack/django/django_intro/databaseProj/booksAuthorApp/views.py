from django.shortcuts import render, HttpResponse, redirect
from .models import *

def bookpage(request):
    context = {
        "books": books.objects.all(),
        "authors": authors.objects.all()
    }
    return render(request, "books.html", context)

def addBook(request):
    title = request.POST['book_title']
    desc = request.POST['book_desc']
    books.objects.create(title=title, desc=desc)
    return redirect('/books')

def viewBook(request, bookID):
    this_book = books.objects.get(id=bookID)
    context = {
        "thisBook": books.objects.get(id=bookID),
        "bookAuthors": this_book.Authors.all()
    }
    return render(request, "viewBook.html", context)


# def displayFruit(request):
#     return render(request, "fruits.html")
# def checkout(request):
#     print("Got Post Info*****************************")
#     print(request.POST)
#     # 'count': sum(strawberry + raspberry + apple)
#     request.session['item_counter'] = int(request.POST['strawberry']) + int(request.POST['raspberry']) + int(request.POST['apple'])
#     context= {
#         "strawberry": request.POST['strawberry'],
#         "raspberry": request.POST['raspberry'],
#         "apple": int(request.POST['apple']),
#         "firstName": request.POST['first_name'],
#         "lastName": request.POST['last_name'],
#         "student_id": request.POST['student_id'],
#     }
#     first_name = context['firstName']
#     last_name = context['lastName']
#     raspberry = int(context['raspberry'])
#     apple = int(context['apple'])
#     strawberry = int(context['strawberry'])
#     count_int = apple + strawberry + raspberry
#     count = int(raspberry)+int(apple)+int(strawberry)
#     print(f"Charging {first_name} {last_name} for {count_int} {count}  {int(strawberry)+int(raspberry)+int(apple)} items ")
#     return render(request, "checkout.html", context, count)

