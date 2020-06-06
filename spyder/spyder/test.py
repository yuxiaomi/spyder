import requests
from bs4 import  BeautifulSoup



def download(url):
    response = requests.get(url)
    response.encoding = 'UTF-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    div=soup.find(name='div',attrs={'class':'downurl'})
    a=div.find(name='a')
    # print(a.get(name='wreryqan'))
    print(a.get('thunderhref'))


def get(url):
    response=requests.get(url)
    response.encoding='UTF-8'
    # print(response.text)
    soup=BeautifulSoup(response.text,'html.parser')
    div=soup.find(name='div',attrs={'class':'item'})
    ul=div.find(name='ul')
    liall=ul.find_all(name='li')
    for info in liall:
        a=info.find(name='a')
        href="http://99aat.com"+a.get('href')
        download(href)
        # print(href)


# print(liall)
if __name__ == '__main__':
   url="http://99aat.com/mlvideolist.x?tagid=3"
   get(url)