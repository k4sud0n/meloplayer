from convert import convert
from crawl import crawl
from download import download
from player import player

if __name__ == '__main__':
    crawl()
    download()
    convert()

player()
