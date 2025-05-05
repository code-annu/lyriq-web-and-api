from django.db import models
import uuid

class Artist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    dob = models.DateField()
    img_url = models.URLField()
    GENDER_CHOICES = [
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    ]
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES)

    def __str__(self):
        return str(self.id)
    

class Album(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    artists = models.ManyToManyField(Artist, related_name='albums')
    release_date = models.DateField()
    tracks_count = models.IntegerField()
    cover_url = models.URLField(max_length=500)

    def __str__(self):
        return self.title
    


class Track(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='tracks')
    artists = models.ManyToManyField(Artist, related_name='tracks')
    release_date = models.DateField()
    duration = models.DecimalField(max_digits=10, decimal_places=3)  # Duration in minutes
    cover_url = models.URLField(max_length=500)
    audio_url = models.URLField(max_length=500)
    lyrics = models.TextField(blank=True)
    likes_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title