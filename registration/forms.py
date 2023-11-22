from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms


User = get_user_model()


class UserCreationForm(UserCreationForm):

    email = forms.EmailField(
        label = ('Email'),
        max_length = 254,
        widget = forms.EmailInput(attrs={'autocomplete': 'email'})
    )
    profile_image = forms.ImageField(label="Profile Picture")
    profile_bio = forms.CharField(label="Profile Bio",
                                  widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Profile Bio'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'profile_image', 'profile_bio')
