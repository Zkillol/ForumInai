from  django.urls import path
from  . import views


urlpatterns = [
    path('chat/', views.chat, name= 'chat'),
    path('friend/<str:pk>', views.chat_view, name ='chat_view'),
]