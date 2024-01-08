from django import forms
from .models import Dweet

class DweetForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Enter recipe here...",
                "class": "textarea is-medium",
            }
        ),
        label="",
    )
    cover = forms.ImageField


    class Meta:
        model = Dweet
        exclude = ("user", )