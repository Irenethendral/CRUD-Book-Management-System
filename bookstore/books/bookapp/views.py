from django.shortcuts import render, redirect, get_object_or_404
from .models import Book

def books_list(request):
    books = Book.objects.all()
    return render(request, 'books_list.html',
                  {'books': books})

def books_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')

        Book.objects.create(
            title=title,
            author=author,
            price=price,
        )
        return redirect('books_list')

    return render(request, 'books_form.html')

def books_update(request, id):
    books  = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        books.title = request.POST.get('title')
        books.author = request.POST.get('author')
        books.price = request.POST.get('price')
        books.save()

        return redirect('books_list')

    return render(request, 'books_form.html',
                  {'books': books})

def books_delete(request, id):
    books = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        books.delete()

    return redirect('books_list')


