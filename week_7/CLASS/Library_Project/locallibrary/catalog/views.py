from django.shortcuts import render, get_object_or_404
from .models import Book, BookInstance, Genre, Author
from django.views import generic
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from .forms import RenewBookForm
import datetime
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
@login_required
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count

    num_instances_available = BookInstance.objects.filter(status__exact="a").count()
    num_authors = Author.objects.all().count()

    num_visits = request.session.get("num_vists", 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        "num_visits": num_visits
    }

    return render(request,"index.html",context)


class BookListView(LoginRequiredMixin,generic.ListView):
    model = Book
    template_name = "book_list.html"
    context_object_name = "book_list"
    queryset = Book.objects.all()
    paginate_by = 1


@login_required
def BookDetailView(request, pk):
    book = get_object_or_404(Book, pk=pk)
    context = {
        'book':book
    }
    return render(request, "catalog/book_detail.html", context)


class AuthorListView(LoginRequiredMixin,generic.ListView):
    model = Author
    template_name = 'author_list.html'
    queryset = Author.objects.all()
    context_object_name = "author_list"


@login_required
def AuthorDetail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    context = {
        "author" : author
    }
    return render(request, "catalog/author_detail.html", context)


class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    model = BookInstance
    template_name ='catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10
    # context_object_name =

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


class LoanedBooks(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = "catalog/borrowedbook_list.html"
    queryset =  BookInstance.objects.filter(status__exact="o").order_by("due_back")
    context_object_name = "borrowed_book"
    # permission_required = 'catalog.can_mark_returned'


@login_required
@permission_required('catalog.can_renew', raise_exception=True)
def renew_book_librarian(request, pk):
    book_instance = get_object_or_404(BookInstance, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = RenewBookForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse("catalog:borrowed-book") )

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        'book_instance': book_instance,
    }

    return render(request, 'catalog/book_renew_librarian.html', context)


class AuthorCreate(LoginRequiredMixin,CreateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']


class AuthorUpdate(LoginRequiredMixin,UpdateView):
    model = Author
    fields = '__all__' # Not recommended (potential security issue if more fields added)


class AuthorDelete(LoginRequiredMixin,DeleteView):
    model = Author
    success_url = reverse_lazy('catalog:author')


class BookCreate(LoginRequiredMixin,CreateView):
    model = Book
    fields = ["title", "author", "summary", "isbn", "genre", "language"]


class BookUpdate(LoginRequiredMixin,UpdateView):
    model = Book
    fields = "__all__"


class BookDelete(LoginRequiredMixin,DeleteView):
    model = Book
    success_url = reverse_lazy("catalog:book")
