from django.urls import path
from .views import *

app_name = 'music'

urlpatterns = [
    path('', home_view, name='home'),
    path('playlists/', playlists_view, name='playlists'),
    path('search/', search_view, name='search'),
    path('likes/', likes_view, name='likes')
]
