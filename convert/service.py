import youtube_dl


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

