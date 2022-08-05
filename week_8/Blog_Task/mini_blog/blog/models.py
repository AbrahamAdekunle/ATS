from django.utils.text import slugify
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect



# Create your models here.
class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_delete=False)

class DeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_delete=True)


class Tags(models.Model):
    name_of_tag = models.CharField(max_length=15, help_text="Enter a suitable tag to help find the post",
                                   default="news")

    def __str__(self):
        return self.name_of_tag


class Niche(models.Model):
    name_of_niche = models.CharField(max_length=20, default="Entertainment",
                                     help_text="Kindly enter the Niche of your post")

    def __str__(self):
        return self.name_of_niche


class Author(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    author_picture = models.ImageField(upload_to="author_images", null=True, blank=True)
    country = models.CharField(max_length=50)
    villain_story = models.TextField()
    date_of_registration = models.DateField(auto_now_add=True)

    # slug = models.SlugField(unique=True, null=False, blank=False)

    def __str__(self):
        return f" {self.lastname}, {self.firstname}"

    def get_absolute_url(self):
        return reverse("blog:author-details", args=[self.id])


class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, help_text="Kindly input your name ", null=True)
    slug = models.SlugField(unique=True, null=False, blank=False)
    body = models.TextField()
    image = models.ImageField(upload_to="article_images", null=True, blank=True)
    date_uploaded = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    niche = models.ManyToManyField(Niche)
    tags = models.ManyToManyField(Tags, blank=True)
    is_delete = models.BooleanField(default=False)

    objects = models.Manager()
    active_objects = ActiveManager()
    deleted_objects = DeleteManager()


    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-date_uploaded"]
        unique_together = ["title", "author"]

    def save(self):
        self.slug = slugify(self.title)
        return super().save()

    def get_absolute_url(self):
        return HttpResponseRedirect(reverse("blog:article-details", args=[self.slug]))

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, editable=False, null=True)
    comment = models.TextField()
    date_of_comment = models.DateTimeField(auto_now_add=True)
    commenter_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, editable=False)
    is_delete = models.BooleanField(default=False)

    objects = models.Manager()
    active_objects = ActiveManager()
    deleted_objects = DeleteManager()

    class Meta:
        ordering = ["-date_of_comment"]
        unique_together = ["article", "comment", "commenter_name"]

    def __str__(self):
        return f"{self.date_of_comment}"

    def comment_description(self):
        return self.comment[:50]

