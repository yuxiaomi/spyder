import requests
from bs4 import  BeautifulSoup

response=requests.get("https://www.bilibili.com/video/av53878299")
# print(response.text)
soup=BeautifulSoup(response.text,'html.parser')
div=soup.find(name='div',attrs={'id':'viewbox_report'})
h1=div.find(name='h1',attrs={'class':'video-title'})
title=h1.get('title')
print(title)