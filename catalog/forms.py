from django import forms
from django.contrib.auth.models import User
from .models import Book


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']  # Example fields


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn']  # Example fields
