from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Book
from .forms import UserForm, BookForm


def user_list(request):
    query = request.GET.get('q', '')
    users = User.objects.filter(username__icontains=query) if query else User.objects.all()
    return render(request, 'catalog/user_list.html', {'users': users, 'query': query})


def book_list(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(title__icontains=query) if query else Book.objects.all()
    return render(request, 'catalog/book_list.html', {'books': books, 'query': query})


def add_user(request, pk=None):
    user = get_object_or_404(User, pk=pk) if pk else None

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)

    return render(request, 'catalog/user_form.html', {'form': form})


def add_book(request, pk=None):
    book = get_object_or_404(Book, pk=pk) if pk else None

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)

    return render(request, 'catalog/book_form.html', {'form': form})


def update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            # Additional logic if needed
            return redirect('book_list')


def update_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            # Additional logic if needed
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'catalog/user_form.html', {'form': form})


def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect('user_list')


def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')


def search_users(request):
    query = request.GET.get('q')
    users = User.objects.filter(username__icontains=query) if query else User.objects.none()
    return render(request, 'catalog/user_list.html', {'users': users, 'query': query})


def search_books(request):
    query = request.GET.get('q')
    books = Book.objects.filter(title__icontains=query) if query else Book.objects.none()
    return render(request, 'catalog/book_list.html', {'books': books, 'query': query})
