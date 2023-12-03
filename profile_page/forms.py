from django import forms
from .models import Profile


class ProfilePicForm(forms.ModelForm):
	profile_image = forms.ImageField(label="Profile Picture" )
	profile_bio = forms.CharField(label="Profile Bio", widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Profile Bio'}))

	class Meta:
		model = Profile
		fields = ('profile_image', 'profile_bio')
