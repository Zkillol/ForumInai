from . import views
from django.urls import path, include


urlpatterns = [
    path('profile/<int:id>/', views.profile, name='profile'),
    path('update_user/', views.update_user, name='update_user'),
    path('', include('home.urls')),
]
