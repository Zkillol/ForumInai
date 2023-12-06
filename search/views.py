from home.models import Posts
from django.shortcuts import render

def search_posts(request):
    query = request.GET.get('q')
    if query:
        results = Posts.objects.filter(title__icontains=query) | Posts.objects.filter(description__icontains=query)
        return render(request, 'search/search.html', {'results': results, 'query': query})
    else:
        return render(request, 'search/search.html')
