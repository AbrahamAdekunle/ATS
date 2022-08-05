from django.shortcuts import render, get_object_or_404, redirect
from .models import Author, Article, Niche, Comment, User
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse
from .forms import CommentOnArticle, CreateUserForm, UpdateAuthor, UpdateUser, ChangePassword
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.db.models import Q

# Create your views here.


def index(request):
    num_articles = Article.active_objects.all().count()
    num_authors = Author.objects.all().count()
    num_niches = Niche.objects.all().count()
    num_users = User.objects.filter(is_staff=False).count()

    context = {"num_articles": num_articles,
               "num_authors": num_authors,
               "num_niches": num_niches,
               "num_users": num_users}
    return render(request, "blog/index.html", context)


class ArticleListView(ListView):
    model = Article
    queryset = Article.active_objects.all()
    context_object_name = "article_list"
    template_name = "blog/article_list.html"
    paginate_by = 5


class AuthorListView(LoginRequiredMixin, ListView):
    model = Author
    template_name = "blog/author_list.html"
    queryset = Author.objects.all()
    context_object_name = 'author_list'


@login_required
def authordetails(request, pk):
    author = get_object_or_404(Author, pk=pk)
    active_articles = Article.active_objects.filter(author=author)
    deleted_articles = Article.deleted_objects.filter(author=author)
    context = {"author": author,
               "active_articles": active_articles,
               "deleted_articles": deleted_articles}

    return render(request, "blog/author_details.html", context)


@login_required
def articledetails(request, slug):
    article = Article.active_objects.get(slug=slug)
    all_comments = Comment.objects.filter(article=article)
    active_comments = Comment.active_objects.filter(article=article)
    deleted_comments = Comment.deleted_objects.filter(article=article)

    if request.method == "POST":
        comment_form = CommentOnArticle(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = Article.objects.get(slug=slug)
            comment.commenter_name = request.user
            comment.save()

            return HttpResponseRedirect(reverse("blog:article-details", args=[slug]))

    comment_form = CommentOnArticle()
    context = {"article": article,
               "comment_form": comment_form,
               "all_comments": all_comments,
               "deleted_comments":deleted_comments,
               "active_comments":active_comments}
    return render(request, "blog/article_details.html", context )


class CommentCreate(View):
    def get(self, request, slug):
        comment_form = CommentOnArticle()
        context = {
            "comment_form": comment_form
        }

        return render(request, "blog/comment_form.html", context)

    def post(self, request, slug):
        comment_form = CommentOnArticle(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = Article.objects.get(slug=slug)
            comment.commenter_name = self.request.user
            comment.save()
            return HttpResponseRedirect(reverse("blog:article-details", args=[slug]))

        context = {
            "comment-form": comment_form,
        }
        return render(request, "blog/comment_form.html", context)


def create_user(request):
    if request.method == "GET":
        user_form = CreateUserForm()
        context = {"user_form": user_form}

        return render(request, "registration/signup.html", context)

    elif request.method == "POST":
        user_form = CreateUserForm(request.POST)

        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.password = make_password(user_form.cleaned_data["password"])
            user.save()

        return HttpResponseRedirect(reverse("login"))

@login_required()
def authorupdate(request,pk):
    author = Author.objects.get(id=pk)
    form = UpdateAuthor(instance=author)

    if request.method =="POST":
        form = UpdateAuthor(request.POST, request.FILES, instance=author)

        if form.is_valid():
            updated_author = form.save(commit=False)
            updated_author.author_picture = form.cleaned_data["author_picture"]
            updated_author.save()
            # form.save()
            return HttpResponseRedirect(author.get_absolute_url())

    elif request.method == "GET":
        context = {"form": form}
        return render(request, "blog/user_update_form.html", context)

class UpdatePassword(View):
    def get(self, username):
        print(username)
        form = ChangePassword()

        context = {"form": form}
        return render(request, "blog/change_password.html", context)

    def post(self, username):
        user = User.objects.get(username=username)
        password_form = ChangePassword(request.POST)

        if password_form.is_valid():
            user.password = make_password(password_form.cleaned_data["password"])
            user.save()
            return HttpResponseRedirect(reverse("blog:user-details", args=[username]))


@login_required()
def userdetails(request, username):
    user = User.objects.get(username=username)
    context = {"user" : user}

    return render(request, "blog/user_details.html", context)

@login_required()
def userupdate(request,username):
    user = get_object_or_404(User, username=username)
    form = UpdateUser(instance=user)

    if request.method == "POST":
        form = UpdateUser(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("blog:user-details", args=[username]))

    context = {"form":form}
    return render(request, "blog/user_update_form.html", context)

@login_required()
def deleteuser(request, username):
    user = get_object_or_404(User, username=username)

    if request.method == "POST":
        user.is_active = False
        user.save()
        return redirect("blog:index")

    context = {"obj" : user}
    return render(request,"blog/delete.html", context)


@login_required()
def deletearticle(request, slug):
    article = get_object_or_404(Article, slug=slug)

    if request.method == "POST":
        article.is_delete = True
        article.save()
        return HttpResponseRedirect(reverse("blog:author-details", args=[article.author.id]))

    context = {"obj": article}
    return render(request, "blog/delete.html", context)

@login_required()
def restorearticle(request, slug):
    article = get_object_or_404(Article, slug=slug)

    if request.method == 'POST':
        article.is_delete = False
        article.save()
        return HttpResponseRedirect(reverse("blog:author-details", args=[article.author.id]))

    context = {"obj" : article}
    return render(request, "blog/restore.html", context)


@login_required()
def deletecomment(request, slug, pk):
    comment = get_object_or_404(Comment, id=pk)
    # article = Articles.active_objects.filter()
    if request.method == "POST":
        comment.is_delete = True
        comment.save()
        return HttpResponseRedirect(reverse("blog:article-details", args=[slug]))

    context = {"obj": comment.comment_description()}
    return render(request, "blog/delete.html", context)

def restorecomment(request, slug, pk):
    comment = get_object_or_404(Comment,id=pk)
    if request.method == "POST":
        comment.is_delete = False
        comment.save()
        return HttpResponseRedirect(reverse("blog:article-details", args=[slug]))

    context = {"obj" : comment.comment_description()}
    return render(request, "blog/restore.html", context)

