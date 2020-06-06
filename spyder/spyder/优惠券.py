import requests,datetime
from bs4 import BeautifulSoup


def good_goods():
    url = 'http://www.123yuan.com/index.php?r=l'
    headers = {
        'User-Agent': 'Mozilla/5.0(Macintosh;Intel Mac 05 X 10_11_4)AppleWebKit/537.36(KHTML,like Gecko)Chrome/52.0.2743.116 Safari/537.36'}
    response = requests.get(url, headers)
    response.encoding = 'utf-8'
    # print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    div = soup.find(name='div', attrs={'class': 'year-bg'})
    # ul=soup.find(name='ul',attrs={'class':'clearfix','id':'goodsItems'})
    # ul=div.find(name='ul')
    print(div)
    # li_list=ul.find(name='li')
    # for item in li_list:
    #     a=item.find(name='a')
    #     href=a.get('href')
    #     img=a.find(name='img')
    #     img_url=img.get('src')
    #     title=img.get('alt')
    #     print('title:', title, 'href:', href, 'img:', img_url)


def save():
    # 图片保存路径\static\img\图片名
    import pymysql
    conn = pymysql.connect('localhost', user="root", passwd="yuxiaomi", db="dd")
    cursor = conn.cursor()
    cursor.execute()


def dateparse(local):
    tuptime = time.localtime(local)
    standartime = time.strftime("%Y-%m-%d", tuptime)
    return standartime


maxprice = None
maxdate = None
mindate = None
minprice = None
import json, time


def maxminprice_list(id):
    res = requests.get(
        url='https://www.gwdang.com/trend/data_www?dp_id=' + id + '&show_prom=true&v=2&get_coupon=1',
        headers={
            'method': 'GET',
            # 'path':'/trend/data_www?dp_id='+id+'&show_prom=true&v=2&get_coupon=1',
            'scheme': 'https',
            'referer': 'https://www.gwdang.com/trend/',
            'dnt': '1',
            'sec - fetch - site': 'same-origin',
            'accept - encoding': 'gzip, deflate, br',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept - language': 'zh - CN, zh;q = 0.9, en - US;q = 0.8, en;q = 0.7',
            "authority": 'www.gwdang.com',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36 Edg/81.0.416.68',
        }
    )
    print(res.text)
    # text = json.loads(res.text)
    # if (text.get("series")[0] is not None):
    #     series = text.get("series")[0]  # 这是json转换过后的第一个dict
    #     print(series)
    #     global maxdate
    #     global maxprice
    #     global mindate
    #     global minprice
    #     maxprice = series["max"] / 100
    #     maxprice_date = series["max_stamp"]
    #     maxdate = dateparse(maxprice_date)
    #     print("最高价格：",maxprice/100,"最高价格日期：",maxdate)
    #
    #     minprice = series["min"] / 100
    #     minprice_date = series["min_stamp"]
    #     mindate = dateparse(minprice_date)
    #     print("最低价格",minprice/100,"最低价格日期",mindate)


def test(id):
    res = requests.get(url='https://www.gwdang.com/trend/data_www?dp_id='+id+'&show_prom=true&v=2&get_coupon=1',
                       headers={'authority': 'www.gwdang.com',
                                'method': 'GET',
                                'cache-control': 'max -age=0',
                                'cookie':'index_big_banner=1; __utmz=188916852.1587714303.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; fp=6b739e7f82ff5b23fc16c14f4224f442; __utmc=188916852; Hm_lvt_7705e8554135f4d7b42e62562322b3ad=1587738453,1587974861,1588853850,1588853878; __utma=188916852.1560941891.1587714303.1588853850.1588855723.5; dfp=0H88kUZe0Cc+kUP26VmMEUJM0CP=6W8+EH8VkUPe0z88kUZM0CM8kUZM0CZ8kUZe6VJ80UcN0UP5; __utmb=188916852.6.10.1588855723; Hm_lpvt_7705e8554135f4d7b42e62562322b3ad=1588856054',
                                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36 Edg/81.0.416.68',
                                })
    print(res.text)

def hisprice(url):
    res = requests.get(
        url="https://www.gwdang.com/trend?url=" + url + "&days=60&crc64=1",
        headers={
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
        if (before == flag or num < 4):
            num = num + 1
            # print("输出第",num)
            # print("循环中的before==flag", before, flag)
            try:
                href = item.find(name="div", class_="dp-img pic1").select("a")[0].get("href")
                if (href.startswith('/union/go')):
                    href = "https://www.gwdang.com/" + href
            except Exception as e:
                # continue
                href = None

            try:
                data_dp = item.find(name="div", class_="dp-item").get("data-dp-id")
                print(data_dp)
                maxminprice_list(data_dp)
            except Exception as e:
                # continue
                print(e)

            try:
                title = item.find(name="div", class_="dp-img pic1").select("a")[0].get("title")
            except Exception as e:
                # continue
                title = None

            try:
                imgurl = item.find(name="div", class_="dp-img pic1").select("a img")[0].get("data-original")
            except Exception as e:
                # continue
                imgurl = None

            try:
                eva = item.find(name="div", class_="promos").select("span")[0].text
            except Exception as e:
                # continue
                eva = None

            try:
                pricenow = item.find(name="div", class_="bottom").find(name="span", class_="price").text
            except Exception as e:
                # continue
                pricenow = None

            try:
                shop = item.find(name="div", class_="product-site").select("span")[0].text
            except Exception as e:
                shop = None

            # 保存基本信息然后传给前端
            coms = (imgurl, href, title, pricenow, maxprice, maxdate, minprice, mindate, eva, shop, flag)
            print(flag, title, pricenow, maxprice,maxdate,minprice,mindate,eva, shop, href, imgurl)
        elif (before == flag):
            # print("before==flag",before,flag)
            continue
        else:
            # print("before!=flag", before, flag)
            before = flag
            num = 0




if __name__ == '__main__':
    # good_goods()
    # test('5028795-3')
    hisprice("http://item.jd.com/1543721098.html")
    # maxminprice_list('8530986-223')
