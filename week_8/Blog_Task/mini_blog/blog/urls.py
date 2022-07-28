from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path("", views.index, name='index'),
    path("article-list/", views.ArticleListView.as_view(), name="article-list"),
    path("author-list/", views.AuthorListView.as_view(), name="author-list"),
    path("author/<int:pk>/", views.authordetails, name="author-details"),
    path("article/<slug:slug>/", views.articledetails, name="article-details"),
    path("article/<slug:slug>/comment/", views.CommentCreate.as_view(), name="article-comment")
    ]


