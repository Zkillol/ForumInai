from django.shortcuts import render, redirect
from django.contrib import messages
from django import forms
from .models import Profile
from home.models import Posts
from registration.forms import UserCreationForm
from .forms import ProfilePicForm
from django.contrib.auth import login, logout
from registration.models import User

def profile(request, id):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=id)
        posts = Posts.objects.filter(user_id=id).order_by("created_at")
        return render(request, 'profile/profile.html', {"profile": profile, "posts": posts})
    else:
        messages.success(request, ("You Must Be Logged In To View This Page..."))
        return redirect('home')



def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        profile_user = Profile.objects.get(user__id=request.user.id)

        if request.method == 'POST':
            user_form = UserCreationForm(request.POST, instance=current_user)
            profile_form = ProfilePicForm(request.POST or None, request.FILES or None, instance=profile_user)
            if user_form.is_valid() and profile_form.is_valid():
                user = user_form.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()

                login(request, current_user)
                messages.success(request, ("Your Profile Has Been Updated!"))
                return redirect('profile')

        return render(request, "profile/update_user.html", { 'profile_form': profile_form})
    else:
        messages.success(request, ("You Must Be Logged In To View That Page..."))
        return redirect('home')
