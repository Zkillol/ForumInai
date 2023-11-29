from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label = ('Email'),
        max_length = 254,
        widget = forms.EmailInput(attrs={'autocomplete': 'email'}) ,
        help_text=''
    )
    username = forms.CharField(label='Username', help_text='')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, help_text='')
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput, help_text='')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2' )
