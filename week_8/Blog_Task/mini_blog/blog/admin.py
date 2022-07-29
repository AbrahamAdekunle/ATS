from django.contrib import admin
from .models import Article, Author, Niche, Tags, Comment


# Register your models here.

class Commentinline(admin.StackedInline):
    model = Comment
    extra = 1


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "country")
    fields = ["firstname", "lastname", "villain_story", "country"]


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date_uploaded")
    prepopulated_fields = {"slug": ("title",)}

    list_filter = ("title", "author", "date_uploaded")

    inlines = [Commentinline]


class CommentAdmin(admin.ModelAdmin):
    list_display = (Comment.comment_description, "article", "commenter_name", "date_of_comment")
    list_filter = ("commenter_name", "article", "commenter_name", "date_of_comment")


admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Niche)
admin.site.register(Tags)
admin.site.register(Comment, CommentAdmin)
