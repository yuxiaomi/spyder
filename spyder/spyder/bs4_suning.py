from bs4 import BeautifulSoup
import requests


def sn(type,keys,num):
    if(type=="search"):
        re = requests.get(
            url="https://search.suning.com/"+keys+"/",
            headers={
                'Accept': '*/*',
                'Accept-Language': 'zh-CN',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'
            },
        )
        re.encoding='utf-8'
        # print(re.text)
        soup = BeautifulSoup(re.text, 'html.parser')
        li=soup.find(class_="general clearfix").find_all(attrs={'doctype':"1"})
        # print(li)
        sncom=[]
        flag=1
        for list in li:
            img=list.find(class_="product-box").select("div div a img")
            imgurl=img[0].get("src")
            # print(imgurl)

            url=list.find(class_="product-box").find(name='div',class_="title-selling-point").select("a")
            href=url[0].get("href")

            name=list.find(class_="product-box").find(name='div',class_="title-selling-point").select("a")
            title=name[0].text
            # print(title)

            # sprice=list.find(name='div',class_="price-box").select("span")
            # sprice=list.find(name='div',class_="price-box")
            # price=sprice[0].text
            # print(sprice)

            eval=list.find(name='div',class_="info-evaluate").select("a i")
            if(eval):
                deal=eval[0].text
            else:
                continue
            # print(deal)

            ashop=list.find(name='div',class_="store-stock").select("a")
            shop=ashop[0].text
            # print(shop)

            location="苏宁搜索"
            price=""
            temp = (href, title, imgurl, shop, price, deal, location)
            sncom.append(temp)
            flag = flag + 1
            if (flag > int(num)):
                break
    print(sncom)

sncom=[]
def price():
    re = requests.get(
        url="https://product.suning.com/0000000000/11222350513.html?safp=d488778a.13701.productWrap.52&safc=prd.0.0&safpn=10007",
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'
        },
    )
    re.encoding = 'utf-8'
    print(re.text)
    soup = BeautifulSoup(re.text, 'html.parser')
    price1=soup.find(name='div',id="priceDom",class_="proinfo-focus clearfix").find(name='span',class_="mainprice")
    print(price1)

def spider_suning(type, key, num):
    if (type == "search"):
        print("这是苏宁的搜索")
        re = requests.get(
            url="https://search.suning.com/" + key + "/",
            headers={
                'Accept': '*/*',
                'Accept-Language': 'zh-CN',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'
            },
        )
        re.encoding = 'utf-8'
        soup = BeautifulSoup(re.text, 'html.parser')
        li = soup.find(class_="general clearfix").find_all(attrs={'doctype': "1"})
        flag = 1
        global sncom
        for list in li:
            img = list.find(class_="product-box").select("div div a img")
            imgurl = img[0].get("src")

            url = list.find(class_="product-box").find(name='div', class_="title-selling-point").select("a")
            href = url[0].get("href")

            name = list.find(class_="product-box").find(name='div', class_="title-selling-point").select("a")
            title = name[0].text

            # sprice=list.find(name='div',class_="price-box").select("span")
            # price=sprice[0].text
            # print(sprice)
            price = None

            eval = list.find(name='div', class_="info-evaluate").select("a i")
            if (eval):
                deal = eval[0].text
            else:
                continue

            ashop = list.find(name='div', class_="store-stock").select("a")
            shop = ashop[0].text

            location = "苏宁搜索"
            price = ""
            temp = (href, title, imgurl, shop, price, deal, location)
            sncom.append(temp)
            flag = flag + 1
            if (flag > int(num)):
                break
        print(sncom)


# sn("search","手机",12)
# price()
spider_suning("search","山灵耳机",12)