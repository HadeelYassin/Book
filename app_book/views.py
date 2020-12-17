from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request):
    context={
        "all_books": Books.objects.all()
        }
    return render(request,"index.html", context)

def addbook(request):
    if request.method == 'POST':
        Books.objects.create(title=request.POST['title'], Desc=request.POST['desc'])
    return redirect('/')
def index1(request):
     context={
        "all_authors": Authors.objects.all()
        }
     return render(request,"index1.html", context)

def addauthor(request):
    if request.method == 'POST':
        Authors.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'], Notes=request.POST['notes'])
    return redirect('/authors')

def showb(request, num):
    this_book=Books.objects.get(id=int(num))
    context={
        "book_authors": this_book.authors.all(),
        "book":this_book,
        "all_authors": Authors.objects.all()
         }
    return render(request, "book_disc.html", context)

def addauthortobook(request, num):
    my_book=Books.objects.get(id=int(num))
    author=Authors.objects.get(id=request.POST['author'])
    my_book.authors.add(author)
    return redirect(f"/bookinfo/{num}")
