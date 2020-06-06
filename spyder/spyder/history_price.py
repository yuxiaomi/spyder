import requests,re
from bs4 import BeautifulSoup

# def gitinfo():
#     r1=requests.get(
#         url="https://tool.manmanbuy.com/m/lsjgcx.aspx?siteurl=http%3a%2f%2fitem.jd.com%2f1378536.html",
#         headers={
#             'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36',
#             'Host':'tool.manmanbuy.com',
#         })
#     print(r1.text)
    # soup=BeautifulSoup(r1.text,'html.parser')
    # ul=soup.find(name='ul',id='feed-main-list')
    # li_all=ul.find_all(name='li',attrs={'class':'feed-row-wide'})


jxcom = []

def spider_jx(num):
    import re
    res = requests.get(
        url='https://www.gwdang.com/promotion/zhi',
        headers={
            'method': 'GET',
            'scheme': 'https',
            'dnt': '1',
            'sec - fetch - dest': 'document',
            'sec - fetch - mode': 'navigate',
            'sec - fetch - site': 'none',
            'sec - fetch - user': '?1',
            'upgrade - insecure - requests': '1',
            'cache - control': 'max - age = 0',
            'path': '/promotion/zhi',
            'authority': 'www.gwdang.com',
            'User-Agent': 'Mozilla/5.0(Macintosh;Intel Mac 05 X 10_11_4)AppleWebKit/537.36(KHTML,like Gecko)Chrome/52.0.2743.116 Safari/537.36'})
    print(res.text)
    soup = BeautifulSoup(res.text, 'html.parser')
    list = soup.find_all(name="li", class_="zdm_li pos_r")
    global jxcom
    flag = 1
    for item in list:
        img = item.find(name="div", class_="section-1").select("a img")[0]
        imgurl = img.get("data-original")

        title = item.find(name="div", class_="section-2").select("div a")[0].get("title")

        price = item.find(name="div", class_="section-2").find(name="span", class_="price").text

        shop = item.find(name="div", class_="site-info pos_a").find(name="span", class_="site-name").text

        str = item.find(name="a", isconvert="1", class_="btn btn-buy pos_a").get("href")
        if (str.startswith('/union/go')):
            href = "https://www.gwdang.com/" + str
        else:
            href = str

        temp = (href, title, imgurl, price, shop)

        jxcom.append(temp)
        flag = flag + 1
        if (flag > int(num)):
            break
    print(jxcom)

import time,json,datetime
def dateparse(local):
    tuptime = time.localtime(local)
    standartime = time.strftime("%Y-%m-%d", tuptime)
    return standartime

def maxminprice_list(id):
    res = requests.get(
        url='https://www.gwdang.com/trend/data_www?dp_id=' + id + '&show_prom=true&v=2&get_coupon=1&price=',
        headers={
            'method': 'GET',
            'scheme': 'https',
            'dnt': '1',
            'sec - fetch - dest': 'document',
            'sec - fetch - mode': 'navigate',
            'sec - fetch - site': 'none',
            'sec - fetch - user': '?1',
            'cache - control': 'max - age = 0',
            'upgrade - insecure - requests': '1',
            'accept - encoding': 'gzip, deflate, br',
            'accept - language': 'zh - CN, zh;q = 0.9, en - US;q = 0.8, en;q = 0.7',
            'authority': 'www.gwdang.com',
            'User-Agent': 'Mozilla/5.0(Macintosh;Intel Mac 05 X 10_11_4)AppleWebKit/537.36(KHTML,like Gecko)Chrome/52.0.2743.116 Safari/537.36'}
    )
    text = json.loads(res.text)
    if (text.get("series")[0] is not None):
        series = text.get("series")[0]  # 这是json转换过后的第一个dict
        # print(series)
        global maxdate
        global maxprice
        global mindate
        global minprice
        maxprice = series["max"] / 100
        maxprice_date = series["max_stamp"]
        maxdate = dateparse(maxprice_date)
        print("最高价格：",maxprice/100,"最高价格日期：",maxdate)

        minprice = series["min"] / 100
        minprice_date = series["min_stamp"]
        mindate = dateparse(minprice_date)
        print("最低价格",minprice/100,"最低价格日期",mindate)


searchcom = []
commondity = []
price = []
pricecompare = []
def hisprice(url):
    res = requests.get(
        url="https://www.gwdang.com/trend?url=" + url + "&days=60&crc64=1",
        headers={
            'method': 'GET',
            'scheme': 'https',
            'dnt': '1',
            'sec - fetch - dest': 'empty',
            'sec - fetch - mode': 'cors',
            'sec - fetch - site': 'same-origin',
            'accept - encoding': 'gzip, deflate, br',
            'accept - language': 'zh - CN, zh;q = 0.9, en - US;q = 0.8, en;q = 0.7',
            'authority': 'www.gwdang.com',
            'User-Agent': 'Mozilla/5.0(Macintosh;Intel Mac 05 X 10_11_4)AppleWebKit/537.36(KHTML,like Gecko)Chrome/52.0.2743.116 Safari/537.36'})
    # print(res.text)
    soup = BeautifulSoup(res.text, 'lxml')
    list = soup.find_all(name="div", class_="b2c")
    num = 0
    temp = None
    before = "京东商城自营"
    for item in list:
        # 找到便签查找个数
        flag = item.find(name="img", class_="site-icon").get("alt")
        if (before == flag and num <9):
            num = num + 1
            # print("输出第",num)
            # print("循环中的before==flag", before, flag)
            try:
                href = item.find(name="div", class_="dp-img pic1").select("a")[0].get("href")
                if (href.startswith('/union/go')):
                    href = "https://www.gwdang.com/" + href
            except Exception as e:
                continue

            try:
                data_dp = item.find(name="div", class_="dp-item").get("data-dp-id")
                # print(data_dp)
                maxminprice_list(data_dp)
            except Exception as e:
                continue

            try:
                title = item.find(name="div", class_="dp-img pic1").select("a")[0].get("title")
            except Exception as e:
                continue

            try:
                imgurl = item.find(name="div", class_="dp-img pic1").select("a img")[0].get("data-original")
            except Exception as e:
                continue

            try:
                eva = item.find(name="div", class_="promos").select("span")[0].text
            except Exception as e:
                continue

            try:
                pricenow = item.find(name="div", class_="bottom").find(name="span", class_="price").text
            except Exception as e:
                continue

            try:
                shop = item.find(name="div", class_="product-site").select("span")[0].text
            except Exception as e:
                continue

            # 保存基本信息然后传给前端
            coms = (imgurl, href, title, pricenow, maxprice, maxdate, minprice, mindate, eva, shop, flag)
            # print(flag, title, pricenow, maxprice,maxdate,minprice,mindate,eva, shop, href, imgurl)
            global searchcom
            searchcom.append(coms)

            #     将查询到的信息插入到数据库中
            commos = (href, title, imgurl, shop, eva, shop)
            global commondity
            commondity.append(commos)

            nowdate = datetime.datetime.now()
            priceinfo = (href, nowdate, pricenow)
            global price
            price.append(priceinfo)

            compareinfo = (href, maxprice, maxdate, minprice, mindate)
            global pricecompare
            pricecompare.append(compareinfo)


        elif (before == flag):
            # print("before==flag",before,flag)
            continue
        else:
            # print("before!=flag", before, flag)
            before = flag
            num = 0
    print(searchcom)



# spider_jx(2)
# maxminprice_list('100004253893-3')
hisprice("https://detail.tmall.com/item.htm?id=595242316346")