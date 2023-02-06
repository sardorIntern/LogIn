from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.hashers import check_password
from .forms import LoginForm, NewsForm, BooksForm
from .models import *
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView


class HomeView(TemplateView):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class LogInPage(LoginView):
    template_name = 'login.html'
    form_class = LoginForm

    def form_valid(self, form):
        user = User.objects.filter(username=form.cleaned_data['username']).first()
        if user is not None and check_password(form.cleaned_data['password'], user.password):
            login(self.request, user)
            return HttpResponseRedirect(reverse_lazy('pages:home'))
        return HttpResponseRedirect(reverse_lazy('pages:login'))


class AddBook(CreateView):
    model = Books
    template_name = 'books.html'
    form_class = BooksForm
    success_url = reverse_lazy("pages:home")

    def get_context_data(self, **kwargs):
        books = Books.objects.all()
        data = {
            "books": books
        }
        return super().get_context_data()

    def __str__(self):
        return Books.title


class AddNews(CreateView):
    model = News
    template_name = 'news.html'
    form_class = NewsForm
    success_url = reverse_lazy("pages:home")

    def get_context_data(self, **kwargs):
        news = News.objects.all()
        data = {
            "news": news
        }
        print(data)
        return super().get_context_data()

    def __str__(self):
        return News.title
