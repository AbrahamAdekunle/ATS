from django.contrib import admin
from .models import Book, Author, BookInstance, Genre
# Register your models here.


class BookInstanceInline(admin.StackedInline):
    model = BookInstance
    extra = 1

class BookInline(admin.StackedInline):
    model = Book
    extra = 1


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "date_of_birth", "date_of_death")

    fields = ["first_name", 'last_name', ("date_of_birth", "date_of_death")]
    inlines = [BookInline]

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", Genre.display_genre, "language")

    inlines = [BookInstanceInline]

class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ("due_back", "status")
    list_display = ("book", "status", 'due_back', "borrower","id")

    fieldsets = ((None,{"fields":('book', 'imprint', 'id')}),
                 ("AVAILABILITY",{"fields":("status", "borrower", "due_back")})
                 )

class GenreAdmin(admin.ModelAdmin):
    pass


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(BookInstance,BookInstanceAdmin)
admin.site.register(Genre, GenreAdmin)