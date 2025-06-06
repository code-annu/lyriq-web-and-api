# Generated by Django 5.2 on 2025-05-02 10:24

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('img_url', models.URLField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('tracks_count', models.IntegerField()),
                ('cover_url', models.URLField(max_length=500)),
                ('artists', models.ManyToManyField(related_name='albums', to='music.artist')),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('duration', models.DecimalField(decimal_places=3, max_digits=10)),
                ('cover_url', models.URLField(max_length=500)),
                ('audio_url', models.URLField(max_length=500)),
                ('lyrics', models.TextField(blank=True)),
                ('likes_count', models.IntegerField(default=0)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='music.album')),
                ('artists', models.ManyToManyField(related_name='tracks', to='music.artist')),
            ],
        ),
    ]
