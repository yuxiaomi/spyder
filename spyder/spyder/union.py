import time,json,lxml,re
from lxml import etree
from bs4 import BeautifulSoup
import requests

def dateparse(local):
    tuptime = time.localtime(local)
    standartime = time.strftime("%Y-%m-%d", tuptime)
    return standartime

maxprice = None
maxdate = None
mindate = None
minprice = None
current=None
# 得到最高最低价格的地址然后搜索
def historypriceinfo(url):
    global maxdate
    global maxprice
    global mindate
    global minprice
    global current
    print("这是历史价格查询！！")
    res = requests.get(
        url="http://p.zwjhl.com/price.aspx?url="+url,
        headers={
            'User-Agent': 'Mozilla/5.0(Macintosh;Intel Mac 05 X 10_11_4)AppleWebKit/537.36(KHTML,like Gecko)Chrome/52.0.2743.116 Safari/537.36'
        })
    soup = BeautifulSoup(res.text, 'lxml')
    minprice=soup.find(attrs={'class':'bigwordprice'}).text.replace('\n','').replace(' ','').replace('\r','')
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
    maxdate = time.strftime("%Y/%m/%d", tuptime)
    print(minprice,mindate,current,maxprice,maxdate)


jdcom=[]
def jdinfo(keys):
    print("这是京东购物的搜索！！")
    re = requests.get(
        url="https://search.jd.com/Search?keyword=" + keys + "&enc=utf-8&",
        headers={
            'User-Agent': 'Mozilla/5.0(Macintosh;Intel Mac 05 X 10_11_4)AppleWebKit/537.36(KHTML,like Gecko)Chrome/52.0.2743.116 Safari/537.36'
        })
    re.encoding = 'utf-8'
    soup = BeautifulSoup(re.text, 'html.parser')
    li = soup.find(attrs={'class': 'gl-warp clearfix'}).find_all(attrs={'class': "gl-item"})
    flag = 1
    global jdcom
    shopname =None
    for list in li:
        shop = list.find(class_="p-shop").select("span a")[0].get('title')
        if (flag >3):
            break
        # 同一家店铺只保存一次
        if (shopname != shop):
            shopname=shop

            # print(list)
            imgattrs = list.find(name='div').find(attrs={'class': "p-img"}).select("a img")
            imgsrc = imgattrs[0].get('src')

            a = list.find(class_="p-name").select("a")
            url = a[0].get('href')
            historypriceinfo(url)

            em = list.find(class_="p-name").select("a em")
            title = em[0].text

            iprice = list.find(class_="p-price").select("strong i")
            price = iprice[0].text


            location = "京东搜索"
            temp = ( imgsrc,url, title,price,maxprice, maxdate, minprice, mindate, None, shop, location)
            jdcom.append(temp)
            # print(jdcom)
            flag = flag + 1
        else:
            continue

    # print(jdcom)

tianmaos=[]
def tianmao(keys):
    re = requests.get(
        url="https://list.tmall.com/search_product.htm?q=" + keys + "&type=p&vmarket=&spm=875.7931836%2FB.a2227oh.d100&from=mallfp..pc_1_searchbutton",
        headers={
            'Accept': '*/*',
            'Accept-Language': 'zh-CN',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'
        },
    )
    soup = BeautifulSoup(re.text, 'lxml')
    li = soup.find_all(attrs={'class': "product"})
    global tianmaos
    flag = 1
    for item in li:
        suk=item.find(class_="productStatus").find(attrs={'data-icon':"small"}).get('data-item')
        # print(suk)
        suk=str(suk)+"-83"
        href = item.find(class_="productImg-wrap").select("a")[0].get('href')
        historypriceinfo(href)
        imgurl = item.find(class_="productImg-wrap").select("a img")[0].get('src')
        title = item.find(class_="productTitle").select("a")[0].get('title')
        price = item.find(class_="productPrice").select("em")[0].get('title')
        shop = item.find(class_="productShop").select("a")[0].text.replace(" ", "").replace("\n", "").replace("\r","")
        deal = item.find(class_="productStatus").select("span em")[0].text.replace(" ", "").replace("\n","").replace( "\r", "")
        location = "天猫商城"
        temp = (imgurl, href, title, price, maxprice, maxdate, minprice, mindate, deal,shop, location)
        tianmaos.append(temp)
        flag = flag + 1
        if (flag >3):
            break
    # print(tianmaos)


def snparse(urls):
    res = requests.get(
        url="https://www.gwdang.com/trend?url=" + urls + "&days=60&crc64=1",
        headers={
            'cookie':'cookie: index_big_banner=1; GWD_ACCESS_TOKEN=04889ce9561e2aa25fbd721404b0f285; __utma=188916852.1560941891.1587714303.1589290981.1589296346.7; __utmc=188916852; __utmz=188916852.1589296346.7.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; Hm_lvt_7705e8554135f4d7b42e62562322b3ad=1588866582,1589181527,1589290981,1589296347; fp=0a4d4089b2a140351864124a079476e2; dfp=0H88kUZeEUmM0CPQ0H8Q6H820CT8kUTikUtM0CMNkUZM0H82EVZM0H820UZM0UM=EUZ86Ut80c55; __utmt=1; __utmb=188916852.8.10.1589296346; Hm_lpvt_7705e8554135f4d7b42e62562322b3ad=1589297091',
            'User-Agent': 'Mozilla/5.0(Macintosh;Intel Mac 05 X 10_11_4)AppleWebKit/537.36(KHTML,like Gecko)Chrome/52.0.2743.116 Safari/537.36'})
    # print(res.text)
    soup = BeautifulSoup(res.text, 'lxml')
    try:
        dpid = soup.find(name="div", class_="collect").select("a")[0].get("url")
        text_uid = dpid.split("&")[0].split("=")[1]
    except Exception as e:
        print(e)
    return text_uid

sncom=[]
def suning(keys):
    print("这是苏宁的搜索")
    re = requests.get(
        url="https://search.suning.com/" + keys + "/",
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
        img = list.find(class_="product-box").select("div div a img")[0].get("src")
        url = list.find(class_="product-box").find(name='div', class_="title-selling-point").select("a")[0].get("href")
        # 通过连接去访问里历史价格
        duk=snparse(url)
        # print(duk)
        historypriceinfo(url)
        titles = list.find(class_="product-box").find(name='div', class_="title-selling-point").select("a")[0].text
        title=titles.replace('\n','').replace(' ','').replace('\r','')
        deal = list.find(name='div', class_="info-evaluate").select("a i")[0].text
        shop = list.find(name='div', class_="store-stock").select("a")[0].text
        location = "苏宁搜索"
        temp = (img, url, title, current, maxprice, maxdate, minprice, mindate, deal, shop, location)
        sncom.append(temp)
        flag = flag + 1
        if (flag >3):
            break
    # print(sncom)

if __name__ == '__main__':
    info=[]
    jdinfo("台灯")
    # maxminprice_list("100007958784-3")
    tianmao("台灯")
    suning("台灯")
    info=tianmaos+jdcom+sncom
    print(info)
