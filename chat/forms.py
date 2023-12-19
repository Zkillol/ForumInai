from django import forms
from django.forms import ModelForm

from chat.models import ChatMessage


class ChatMessageForm(ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={ 'placeholder' : 'Type message here'}))
    class Meta:
        model = ChatMessage
        fields = ['body']