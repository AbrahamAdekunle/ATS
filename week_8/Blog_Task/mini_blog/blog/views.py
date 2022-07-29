from django.shortcuts import render, get_object_or_404
from .models import Author, Article, Niche, Comment, User
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import CommentOnArticle, CreateUserForm
from django.contrib.auth.hashers import make_password


# Create your views here.


def index(request):
    num_articles = Article.objects.all().count()
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
    queryset = Article.objects.all()
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
    context = {"author": author}

    return render(request, "blog/author_details.html", context)


# @login_required
def articledetails(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == "POST":
        comment_form = CommentOnArticle(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = Article.objects.get(slug=slug)
            comment.commenter_name = request.user
            comment.save()

            return HttpResponseRedirect(reverse("blog:article-details", args=[slug]))

    comment_form = CommentOnArticle()
    return render(request, "blog/article_details.html", {"article": article, "comment_form": comment_form})


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

            # username = user_form.cleaned_data["username"]
            # firstname = user_form.cleaned_data["first_name"]
            # lastname = user_form.cleaned_data["last_name"]
            # email = user_form.cleaned_data["email"]
            # password = make_password(user_form.cleaned_data["password"])
            # user = User(username=username, first_name=firstname, last_name=lastname, email=email, password=password)
            # user.save()

        return HttpResponseRedirect(reverse("login"))
