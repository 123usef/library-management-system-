from multiprocessing import context
from django.shortcuts import render ,redirect
from .models import *
from .forms import BookForm ,CategoryForm
# Create your views here.

def index(request) :
    if request.method == 'POST':
        add_book = BookForm(request.POST,request.FILES)
        if add_book.is_valid():
            add_book.save()
        add_cat = CategoryForm(request.POST)
        if add_cat.is_valid():
            add_cat.save()


    books = Book.objects.all()
    allbooks = Book.objects.filter(available=True).count()
    allsold = Book.objects.filter(status='sold').count()
    allrent = Book.objects.filter(status='available').count()
    allavailble = Book.objects.filter(status='rental').count()
    cat = Category.objects.all()

    context = {
        'books':books ,
        'cat':cat ,
        'form': BookForm(),
        'formcat':CategoryForm(),
        'allbooks':allbooks,
        'allsold':allsold,
        'allrent':allrent,
        'allavailble':allavailble,
    }

    return render(request , 'pages/index.html',context)    


def books_view(request):
    books = Book.objects.all()
    cat = Category.objects.all()

    context = {
        'books':books ,
        'cat':cat ,
    }
    return render(request , 'pages/books.html' ,context)

def delete(request, id):
    book = Book.objects.get(id=id)
    if request.method =='POST':
       book.delete() 
       return redirect('/')

    return render(request , 'pages/delete.html')

def update(request , id):
    book = Book.objects.get(id=id)
    if request.method =='POST':
        book_save = BookForm(request.POST , request.FILES , instance=book)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else:
        book_save = BookForm(instance=book)   
    context={
        'form':book_save,
    }       
    return render(request , 'pages/update.html',context)

