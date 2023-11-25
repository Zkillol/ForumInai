from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label = ('Email'),
        max_length = 254,
        widget = forms.EmailInput(attrs={'autocomplete': 'email'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', )
