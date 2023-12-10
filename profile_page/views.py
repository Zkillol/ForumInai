from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Profile
from home.models import Posts
from .forms import ProfilePicForm
from django.contrib.auth import login, logout
from django.views import generic
from home.forms import PostForm
from django.urls import reverse, reverse_lazy


def profile(request, id):

    if request.user.is_authenticated:
        profile = get_object_or_404(Profile , user_id=id)
        posts = Posts.objects.filter(user_id=id).order_by("created_at")
        return render(request, 'profile/profile.html', {"profile": profile, "posts": posts})
    else:
        messages.success(request, ("You Must Be Logged In To View This Page..."))
        return redirect('home')





def update_user(request, id):
    profile_user = get_object_or_404(Profile, user_id=id)


    if request.method == 'POST':

        profile_form = ProfilePicForm(request.POST, request.FILES, instance=profile_user)

        if profile_form.is_valid():

            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            login(request, request.user)
            messages.success(request, "Your Profile Has Been Updated!")
            return redirect('profile',  id=id)

    else:

        profile_form = ProfilePicForm(instance=profile_user)

    return render(
        request,
        "profile/update_user.html",
        { 'profile_form': profile_form}
    )

class PostDeleteView(generic.DeleteView):
    template_name = "post_detail_CRUD/confirm_delete.html"

    def get_object(self, **kwargs):
        post_id = self.kwargs.get("id")
        return get_object_or_404(Posts, id=post_id)

    def get_success_url(self):
        user_id = self.request.user.id
        return reverse_lazy('profile', kwargs={'id': user_id})

class PostEditView(generic.UpdateView):
    template_name = "post_detail_CRUD/post_edit.html"
    form_class = PostForm

    def get_object(self, **kwargs):
        post_id = self.kwargs.get("id")
        return get_object_or_404(Posts, id=post_id)

    def form_valid(self, form):
        return super(PostEditView, self).form_valid(form=form)

    def get_success_url(self):
        return reverse("post_show", kwargs={"id": self.object.id})
