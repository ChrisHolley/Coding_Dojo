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

def addAuthor(request):
    addFirstName = request.POST['formFirstName']
    addLastName = request.POST['formLastName']
    addNotes = request.POST['formNotes']
    authors.objects.create(first_name=addFirstName, last_name=addLastName, notes=addNotes)
    return redirect('/books/authorpage')


def viewBook(request, bookID):
    if request.method == 'POST':
        Authors = authors.objects.get(id=request.POST['Authors'])
        books.objects.get(id=bookID).Authors.add(Authors)
    this_book = books.objects.get(id=bookID)
    context = {
        "thisBook": books.objects.get(id=bookID),
        "bookAuthors": this_book.Authors.all(),
        "authors": authors.objects.all()
    }
    return render(request, "viewBook.html", context)

def authorpage(request):
    context = {
        "books": books.objects.all(),
        "authors": authors.objects.all()
    }
    return render(request, "authors.html", context)

def viewAuthor(request, authorID):
    context= {
        "thisAuthor": authors.objects.get(id=authorID)
    }
    return render(request, "viewAuthor.html", context)

def addAutherToBook(request):
    book_ID = request.POST['book_id']
    author_ID = request.POST['author.id']
    return HttpResponse(book_ID, author_ID)