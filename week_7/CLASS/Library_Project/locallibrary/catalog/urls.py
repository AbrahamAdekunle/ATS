from django.urls import path
from . import views

app_name = "catalog"
urlpatterns = [
    path("",views.index,name="index"),
    path("book/", views.BookListView.as_view(), name="book"),
    path('book/<int:pk>', views.BookDetailView, name="book-detail"),
    path("book/<int:pk>/update", views.BookUpdate.as_view(), name="book-update"),
    path("book/<int:pk/delete", views.BookDelete.as_view(), name="book-delete"),
    path("book/create/", views.BookCreate.as_view(), name="book-create"),
    path("author/", views.AuthorListView.as_view(), name="author"),
    path("author/<int:pk>", views.AuthorDetail, name="author-detail"),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),
    path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path("borrowedbooks/", views.LoanedBooks.as_view(), name="borrowed-book"),
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),

]