from __future__ import unicode_literals
from django.db import models
import youtube_dl

# Create your models here.


class History(models.Model):
    history_url = models.CharField(max_length=200)
    history_title = models.TextField(null=True)

    def __str__(self):
        return self.history_title


    def download_song(self, song_url):
        ydl_opts = {
            'format': 'bestaudio/best',
            'noplaylist': True,
            'forcetitle': True,
            'postprocessors': [
                {'key': 'FFmpegExtractAudio',
                 'preferredcodec': 'mp3',
                 'preferredquality': '192'},
            ],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            meta = ydl.extract_info(song_url, download=True)
            q = History(history_url=song_url, history_title=meta['title'])
            q.save()



