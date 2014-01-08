from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Book


def showBooks(request):
    books = Book.objects.all()

    return render(request, "books.html", { 'books': books })

# Create your views here.
