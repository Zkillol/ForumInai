from django.contrib import admin
from .models import Friend, ChatMessage

admin.site.register([Friend , ChatMessage])
