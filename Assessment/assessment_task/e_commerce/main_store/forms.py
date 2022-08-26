from django import forms

from .models import Checkout


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        exclude = ("user","checkout_date",)
