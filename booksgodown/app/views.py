from django.shortcuts import render
from . import forms
from app.models import Book
# Create your views here.

def index_view(requst):
    return render(requst,'index.html')

def display_view(request):
    book_list = Book.objects.all()
    return render(request,'bookslist.html',{'book_list':book_list})

def insert_view(request):
    form = forms.BookForm()
    if request.method =="POST":
        form = forms.BookForm(request.POST)
        if form.is_valid():
            form.save(commit = True)
        return render(request,'index.html')
    return render(request,'insert.html',{'form':form})