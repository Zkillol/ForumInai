from django import forms
from .models import Profile
from django.contrib.auth.forms import UserChangeForm


class ProfilePicForm(UserChangeForm):
	profile_image = forms.ImageField(label="Profile Picture" )
	profile_bio = forms.CharField(label="Profile Bio", widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Profile Bio'}))

	class Meta:
		model = Profile
		fields = ('profile_image', 'profile_bio')
