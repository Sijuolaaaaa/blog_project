from django import forms
from .models import UserPost

class Blogform(forms.ModelForm):

    class Meta:
        model= UserPost
        fields= [
            "title",
            "content",
            "status",
            "image",
            "category"
        ]