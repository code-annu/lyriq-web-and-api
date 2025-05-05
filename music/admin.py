from django.contrib import admin
from .models import Artist,Album, Track
# Register your models here.

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'gender','dob','img_url')

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'release_date','tracks_count','cover_url','get_artists')
    
    def get_artists(self, obj):
        return ", ".join(artist.name for artist in obj.artists.all())

@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'album','release_date','duration','cover_url','audio_url','lyrics','likes_count','get_artists')
    
    def get_artists(self, obj):
        return ", ".join(artist.name for artist in obj.artists.all())
    get_artists.short_description = 'Artists'

    
    
    
