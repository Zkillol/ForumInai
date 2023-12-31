from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import logout
from comments.forms import CommentForm
from .models import Posts
from .forms import PostForm


def home(request):
    posts = Posts.objects.order_by('-id')
    return render(request, 'home.html', {'title': 'Главная страница сайта', 'posts': posts})


def logout_user(request):
    logout(request)
    messages.success(request, ("You Have Been Logged Out..."))
    return redirect('home')


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST , request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()

    context = {
        'form': form,
    }
    return render(request, 'post_detail_CRUD/create.html', context)


def post_like(request, id):
    if request.user.is_authenticated:
        post = get_object_or_404(Posts, id=id)
        if post.likes.filter(id=request.user.id):
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return redirect(request.META.get("HTTP_REFERER"))
    else:
        messages.success(request, ("You Must Be Logged In To View That Page..."))
        return redirect('home')


def post_show(request, id):
    post = get_object_or_404(Posts, id=id)
    comments = post.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = post
            new_comment.save()
            messages.success(request, "Comment added successfully.")
            return redirect('post_show', id=id)
        else:
            messages.error(request, "Error while adding a comment.")
    else:
        form = CommentForm()

    return render(request, "post_detail_CRUD/post_details.html", {'post': post, 'comments': comments, 'form': form})

