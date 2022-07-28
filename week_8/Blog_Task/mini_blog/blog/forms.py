from django import forms
from .models import Comment


class CommentOnArticle(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ["date_of_comment"]