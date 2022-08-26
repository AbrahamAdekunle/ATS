from django.shortcuts import render, reverse
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate, update_session_auth_hash
from django.views.generic import DetailView
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, AccessMixin

from .forms import MyUserCreationForm
from .models import User


# Create your views here.

class UserIsNotOwnerMixIn(UserPassesTestMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.id == kwargs['pk']:
            return super().dispatch(request, *args, **kwargs)
        else:
            return self.handle_no_permission()


def user_sign_in(request):
    email = request.POST.get("email")
    password = request.POST.get("password")
    page = "sign_in"

    if request.method == "POST":
        try:
            user = User.objects.get(email=email)

        except:
            messages.error(request, "Email does not exist, you should probably sign up or check your e-mail")
            return render(request, "nucleus/signin_signup.html", {"page": page})

        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("main_store:index"))
        messages.error(request, "Invalid login details")
        return render(request, "nucleus/signin_signup.html", {"page": page})

    elif request.method == "GET":
        return render(request, "nucleus/signin_signup.html", {"page": page})


def user_sign_out(request):
    logout(request)
    return HttpResponseRedirect(reverse("main_store:index"))


def sign_up(request):
    form = MyUserCreationForm()
    page = "sign_up"

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST, )

        if form.is_valid():
            my_user = form.save()

            login(request, my_user)
            return HttpResponseRedirect(reverse("main_store:index"))
        messages.error(request, 'An error occurred during details entry, please check ')

    context = {
        "form": form,
        "page": page
    }

    return render(request, "nucleus/signin_signup.html", context)


class UserProfile(LoginRequiredMixin, AccessMixin, DetailView):
    model = User
    template_name = "nucleus/profile.html"
    context_object_name = 'user'
    login_url = "nucleus:sign_in"


@login_required(login_url="nucleus:sign_in")
def user_update_details(request, pk):
    if request.user.id != pk:
        return HttpResponseForbidden()

    user = User.objects.get(id=pk)
    form = MyUserCreationForm(instance=user)
    page = "user_update_details"

    if request.method == "POST":
        form = MyUserCreationForm(request.POST, request.FILES, instance=user)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('nucleus:profile'))

        else:
            messages.error(request, 'Invalid detail entered')

    elif request.method == "GET":
        context = {
            "form": form,
            "page": page,
        }
        return render(request, "nucleus/profile_forms.html", context)


@login_required(login_url="nucleus:sign_in")
def change_password(request, pk):
    if request.user.id != pk:
        return HttpResponseForbidden()

    form = PasswordChangeForm(request.user)
    page = "change_password"

    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password Changed Successfully")
            return HttpResponseRedirect(reverse("nucleus:profile", args=[pk]))
        else:
            messages.error(request, "please correct the error below")

    context = {"form": form,
               "page": page,
               }
    return render(request, "nucleus/profile_forms.html", context)
