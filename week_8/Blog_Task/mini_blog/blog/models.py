from django.utils.text import slugify
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
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
    country = models.CharField(max_length=50)
    villain_story = models.TextField()
    date_of_registration = models.DateField(auto_now_add=True)

    # slug = models.SlugField(unique=True, null=False, blank=False)

    def __str__(self):
        return f" {self.lastname}, {self.firstname}"


class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, help_text="Kindly input your name ", null=True)
    slug = models.SlugField(unique=True, null=False, blank=False)
    body = models.TextField()
    image = models.ImageField(upload_to="blog/", null=True, blank=True)
    date_uploaded = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    niche = models.ManyToManyField(Niche)
    tags = models.ManyToManyField(Tags, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["date_uploaded"]

    def save(self):
        self.slug = slugify(self.title)
        return super().save()

    def get_absolute_url(self):
        return


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, editable=False, null=True)
    comment = models.TextField()
    date_of_comment = models.DateTimeField(auto_now_add=True)
    commenter_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, editable=False)

    class Meta:
        ordering = ["date_of_comment"]

    def __str__(self):
        return f"{self.comment}"
