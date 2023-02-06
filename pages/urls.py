from django.contrib.auth.views import LogoutView
from django.urls import path
from pages.views import LogInPage, HomeView, AddBook, AddNews

app_name = "pages"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LogInPage.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('books/new', AddBook.as_view(), name='book_new'),
    path('news/new', AddNews.as_view(), name='news_new'),
]
