import youtube_dl
from .models import History

locals()
def save_in_history(song_url, meta_data):
    history = History(history_url=song_url, history_title=meta_data['title'])
    history.save()


def youdl_manage(url):
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
        meta = ydl.extract_info(url, download=True)
        return meta

