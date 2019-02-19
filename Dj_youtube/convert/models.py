from __future__ import unicode_literals
from django.db import models
import youtube_dl

# Create your models here.


class History(models.Model):
    history_text = models.CharField(max_length=200)

    def download_song(song_url):
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [
                {'key': 'FFmpegExtractAudio',
                 'preferredcodec': 'mp3',
                 'preferredquality': '192'},
            ],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([song_url])

    def __str__(self):
        return self.history_text
