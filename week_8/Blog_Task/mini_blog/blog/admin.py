from django.contrib import admin
from .models import Article, Author, Niche, Tags


# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "country")
    fields = ["firstname", "lastname", "villain_story", "country"]


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date_uploaded")
    prepopulated_fields = {"slug": ("title",)}

    list_filter = ("title", "author", "date_uploaded")


admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Niche)
admin.site.register(Tags)
