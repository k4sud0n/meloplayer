import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
req = requests.get('https://www.melon.com/chart/', headers=header)
html = req.text
parse = BeautifulSoup(html, 'html.parser')

titles = parse.find_all('div', {'class': 'ellipsis rank01'})
singers = parse.find_all('div', {'class': 'ellipsis rank02'})

title = []
singer = []

write_wb = Workbook()
write_ws = write_wb.active

for t in titles:
    title.append(t.find('a').text)

for s in singers:
    singer.append(s.find('span', {'class': 'checkEllipsis'}).text)

for i in range(50):
    write_ws.append([title[i], singer[i]])

write_wb.save("song.xlsx")
