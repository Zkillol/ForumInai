from .models import Posts
from django.forms import ModelForm , TextInput , Textarea , ImageField


class PostForm(ModelForm):
    class Meta:
        model = Posts
        fields = ["title" , "description", "image"]
        widgets = {
            "title": TextInput(attrs={
            'class': 'form-control',
            'placeholder' : 'Введите название'
        }),
            'description': Textarea(attrs={
            'class': 'form-control',
            'placeholder' : 'Введите описание'
        }),
                   }