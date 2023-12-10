from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('post_like/<int:id>/', views.post_like, name='post_like'),
    path('post_show/<int:id>', views.post_show, name="post_show"),
    path('logout_user', views.logout_user, name="logout_user"),
]
