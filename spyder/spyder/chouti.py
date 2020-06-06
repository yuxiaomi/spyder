from bs4 import BeautifulSoup
import requests

#----------------抽屉网-------------
def chouti():
    re=requests.get(
        url='https://dig.chouti.com/',
        headers={
            'User-Agent': 'Mozilla/5.0(Macintosh;Intel Mac 05 X 10_11_4)AppleWebKit/537.36(KHTML,like Gecko)Chrome/52.0.2743.116 Safari/537.36'    }
    )
    print(re.text)
    soup=BeautifulSoup(re.text,'html.parser')
    content_list=soup.find(name='div',id='content-list')
    item_list=content_list.find_all_next(name='div',attrs={'class':'item'}) #一个列表
    for item in item_list:
        part1=item.find(name='div',attrs={'class':'part1'})
        a=part1.find(name='a')
        print(a.text.strip())


def bullpeople():
    re=requests.get('http://www.bullpeople.cn/')
    soup=BeautifulSoup(re.text,'html.parser')
    ul=soup.find(name='ul',id='detail')
    li_list=ul.find_all_next(name='li')
    for info in li_list:
        a=info.find(name='a')
        print(a.text)

def zhihu():
    re=requests.get(
        url='https://www.zhihu.com/search?type=content&q=%E4%B8%AD%E5%9B%BD',
    headers={
        'User-Agent': 'Mozilla/5.0(Macintosh;Intel Mac 05 X 10_11_4)AppleWebKit/537.36(KHTML,like Gecko)Chrome/52.0.2743.116 Safari/537.36'
    }
    )
    print(re.text)


if __name__ == '__main__':
    # bullpeople()
    # chouti(
    zhihu()
