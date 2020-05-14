import os

import pytube
import requests
from bs4 import BeautifulSoup
from openpyxl import load_workbook
from pytube import YouTube


def download():
    load_wb = load_workbook('song.xlsx', data_only=True)
    load_ws = load_wb['Sheet']

    song_title = []
    song_artist = []

    URL = 'https://www.youtube.com/results'

    for row in load_ws['A1':'B50']:
        row_value = []

        for cell in row:
            row_value.append(cell.value)

        song_title.append(row_value[0])
        song_artist.append(row_value[1])

    for i in range(50):
        params = {'search_query': '%s %s' % (song_artist[i], song_title[i])}
        response = requests.get(URL, params=params)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        try:
            watch_url = soup.find_all(class_='yt-uix-sessionlink spf-link')[0]['href']
        except IndexError:
            pass
        except pytube.exceptions.RegexMatchError:
            pass

        try:
            youtube = YouTube('https://www.youtube.com' + watch_url)
            videos = youtube.streams.first()
            videos.download(os.getcwd() + "\\songs")
        except KeyError:
            pass
