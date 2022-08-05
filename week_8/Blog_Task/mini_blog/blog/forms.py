from django import forms
from .models import Comment, User, Author


class CommentOnArticle(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["date_of_comment", "is_delete"]


class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password"]


class UpdateAuthor(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"

class UpdateUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email" ]

class ChangePassword(forms.Form):
    password = forms.PasswordInput()
