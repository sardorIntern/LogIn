from django.contrib.auth.forms import AuthenticationForm
from django import forms

from pages.models import News, Books


class LoginForm(AuthenticationForm):
    pass


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"


class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = "__all__"
