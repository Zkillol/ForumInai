from django.urls import path, include
from registration.views import Register
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('person/', views.person_view, name='person'),
    path('register/', Register.as_view(), name='register'),


]