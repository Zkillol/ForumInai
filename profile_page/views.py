from django.shortcuts import render, redirect, get_object_or_404
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
        # profile = Profile.objects.get(user_id=id)
        profile = get_object_or_404( Profile , user_id=id)
        posts = Posts.objects.filter(user_id=id).order_by("created_at")
        return render(request, 'profile/profile.html', {"profile": profile, "posts": posts})
    else:
        messages.success(request, ("You Must Be Logged In To View This Page..."))
        return redirect('home')



def update_user(request, pk):
    # Use get_object_or_404 to retrieve the Profile object or raise a 404 error
    profile_user = get_object_or_404(Profile, user__id=pk)

    if request.method == 'POST':
        user_form = UserCreationForm(request.POST, instance=request.user)
        profile_form = ProfilePicForm(request.POST, request.FILES, instance=profile_user)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)
            messages.success(request, "Your Profile Has Been Updated!")
            return redirect('profile')

    else:
        user_form = UserCreationForm(instance=request.user)
        profile_form = ProfilePicForm(instance=profile_user)

    return render(
        request,
        "profile/update_user.html",
        {'user_form': user_form, 'profile_form': profile_form}
    )
