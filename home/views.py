from django.shortcuts import render, redirect
from .models import Posts
from .forms import PostForm

def home(request):
    tasks = Posts.objects.order_by('-id')[:5]
    return render(request, 'home.html' ,{'title': 'Главная страница сайта', 'tasks': tasks})






def create(request):
    error = ''
    if request.method == 'POST':
        form = PostForm(request.POST)
        form.save()
        return redirect('home')

    form = PostForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'postcreate/create.html', context)