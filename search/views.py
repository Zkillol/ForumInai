from django.shortcuts import render
from home.models import Posts
from profile_page.models import Profile
from django.contrib.auth.models import User



def search_users(request):
    query = request.GET.get('q')
    if query:
        results = User.objects.filter(username__icontains=query)
        return render(request, 'search/search.html', {'results': results, 'query': query})
    else:
        return render(request, 'search/search.html')





def search_posts(request):
    query = request.GET.get('q')
    if query:
        results = Posts.objects.filter(title__icontains=query) | Posts.objects.filter(description__icontains=query)
        return render(request, 'search/search.html', {'results': results, 'query': query})
    else:
        return render(request, 'search/search.html')
