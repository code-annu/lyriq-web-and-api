from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request, 'music/home.html')


def playlists_view(request):
    return render(request, 'music/playlists.html')

def search_view(request):
    return render(request, 'music/search.html')

def likes_view(request):
    return render(request, 'music/likes.html')