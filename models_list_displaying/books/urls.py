from . import views
from django.urls import path


urlpatterns = [
    path('books/', views.BookListView.as_view(), name='books'),
    path('books/<str:date>', views.BookListView.as_view(), name='sort_books')

]
