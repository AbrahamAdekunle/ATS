from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path("", views.index, name='index'),
    path("article-list/", views.ArticleListView.as_view(), name="article-list"),
    path("author-list/", views.AuthorListView.as_view(), name="author-list"),
    path("author/<int:pk>/", views.authordetails, name="author-details"),
    path("author/<int:pk>/update", views.authorupdate, name="update-author-details"),
    path("article/<slug:slug>/", views.articledetails, name="article-details"),
    path("article/<slug:slug>/comment/", views.CommentCreate.as_view(), name="article-comment"),
    path("article/<slug:slug>/comment/<int:pk>/delete", views.deletecomment, name="delete-comment"),
    path("article/<slug:slug>/comment/<int:pk>/restore", views.restorecomment, name="restore-comment"),
    path("article/<slug:slug>/delete/", views.deletearticle, name="delete-article"),
    path("article/<slug:slug>/restore", views.restorearticle, name="restore-article"),
    path("user/<str:username>/", views.userdetails, name="user-details"),
    path("user/<str:username>/update", views.userupdate, name="update-user-details"),
    path("user/<str:username>/delete", views.deleteuser, name="delete-user"),
    path("user/<str:username>/update/change-password", views.UpdatePassword.as_view(), name="change-password")
]
