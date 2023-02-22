from __future__ import unicode_literals
import youtube_dl
import urllib.request
import re

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

with open("music.txt", 'r', encoding="utf-8") as mc:
    for song in mc:
        query = urllib.parse.quote(song)
        html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={query}")

        video = re.findall(r"watch\?v=(\S{11})", html.read().decode())[0]  # first link of youtube search

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f"https://www.youtube.com/watch?v={video}"])
