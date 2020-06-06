import time,json,lxml,re
from lxml import etree
from bs4 import BeautifulSoup
import requests


def maxdateparse(times):
    text=int(times)/1000
    tuptime = time.localtime(text)
    standartime = time.strftime("%Y/%m/%d", tuptime)
    return standartime



def info(url):
    print("这是历史价格查询！！")
    res = requests.get(
        url="http://p.zwjhl.com/price.aspx?url="+url,
        headers={
            'User-Agent': 'Mozilla/5.0(Macintosh;Intel Mac 05 X 10_11_4)AppleWebKit/537.36(KHTML,like Gecko)Chrome/52.0.2743.116 Safari/537.36'
        })
    soup = BeautifulSoup(res.text, 'lxml')
    minprice=soup.find(attrs={'class':'bigwordprice'}).text.replace('\n','').replace(' ','')
    textall=soup.find(class_='bigwidth').text
    mindate = re.search('(?<=\()[^()]*(?=\))', textall)[0]
    current = re.search('(?<=\：)(.*)(?=\.)', textall)[0]

    etrees=etree.HTML(res.text)
    maxtext=etrees.xpath('/html/body/div[2]/div/div/div[1]/script')[0].text
    result = re.findall('(?<=\[)(.*?)(?=\])', maxtext)[0]
    jg = result.split(',', 2)
    maxdate = int(jg[0])
    maxprice = jg[1]

    tuptime = time.localtime(maxdate/1000)
    maxpricedate = time.strftime("%Y/%m/%d", tuptime)

    print(minprice,mindate,current,maxprice,maxpricedate)


if __name__ == '__main__':
    info("http://item.jd.com/100008348532.html")
