from . import views
from django.urls import path, include


urlpatterns = [
    path('profile/<int:id>/', views.profile, name='profile'),
    path('update_user/<int:id>/', views.update_user, name='update_user'),
    path('', include('home.urls')),
    path('post_show/<int:id>/delete/', views.PostDeleteView.as_view()),
    path('post_show/<int:id>/edit/', views.PostEditView.as_view()),

]
