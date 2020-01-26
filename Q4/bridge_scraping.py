import requests
import io
from random import randrange
from bs4 import BeautifulSoup

wiki_bridge = "https://en.wikipedia.org/wiki/Bridge"
result = requests.get(wiki_bridge)

if result.status_code == 200:
    soup = BeautifulSoup(result.content, "html.parser")

myimgs = soup.findAll("img", {"class": "thumbimage"})
img_url = 'https:' + myimgs[randrange(len(myimgs))]['src']
img = requests.get(img_url, stream=True)
file = open("outputs/2.jpg",'wb')
for block in img.iter_content(1024):
    if not block:
        break
    file.write(block)