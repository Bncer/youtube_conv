import youtube_dl
from .models import History


def download_song(song_url):
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
