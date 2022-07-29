from django import forms
from .models import Comment, User


class CommentOnArticle(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["date_of_comment"]


class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password"]
        # groups
