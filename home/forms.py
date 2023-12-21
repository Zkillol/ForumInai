from .models import Posts
from django.forms import ModelForm, TextInput, Textarea, ImageField


class PostForm(ModelForm):
    class Meta:
        model = Posts
        fields = ["title", "description", "image"]
        widgets = {
            "title": TextInput(
                attrs={
                'class': 'form-control',
                'placeholder' : 'Title'
                }),
                'description': Textarea(attrs={
                'class': 'form-control',
                 'placeholder': 'Description'
                }),
        }
        exclude = ("user", "likes",)
