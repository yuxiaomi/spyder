from bs4 import BeautifulSoup
import requests,time
import lxml
from selenium.webdriver import Chrome
def tianmao(type,keys,num):
    if(type=="search"):
        re = requests.get(
            url="https://list.tmall.com/search_product.htm?q="+keys+"&type=p&vmarket=&spm=875.7931836%2FB.a2227oh.d100&from=mallfp..pc_1_searchbutton",
            headers={
                'Accept': '*/*',
                'Accept-Language': 'zh-CN',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'
            },
        )
        # print(re.text)
        soup = BeautifulSoup(re.text, 'lxml')
        li = soup.find_all(attrs={'class': "product"})
        # print(li)
        tianmao=[]
        flag=1
        for item in li:
            href=item.find(class_="productImg-wrap").select("a")[0].get('href')
            imgurl=item.find(class_="productImg-wrap").select("a img")[0].get('src')
            title=item.find(class_="productTitle").select("a")[0].get('title')
            price=item.find(class_="productPrice").select("em")[0].get('title')
            shop=item.find(class_="productShop").select("a")[0].text.replace(" ","").replace("\n","").replace("\r","")
            deal=item.find(class_="productStatus").select("span em")[0].text.replace(" ","").replace("\n","").replace("\r","")
            location="天猫搜索"
            temp = (href, title, imgurl, shop, price, deal, location)
            tianmao.append(temp)
            flag = flag + 1
            if (flag > int(num)):
                break
    print(tianmao)
# tianmao("search","女装",12)
# price()


tbcars = []
def spider_taobao():
    browser = Chrome()
    browser.get("https://login.taobao.com/")
    while browser.current_url.startswith("https://login.taobao.com/"):
        print("等着淘宝的登录")
        time.sleep(1)
    browser.get("https://cart.taobao.com/")  # 淘宝购物车的网址
    time.sleep(1)
    items = browser.find_element_by_id("J_OrderList").find_elements_by_class_name("J_OrderHolder")
    global tbcars
    for i in items:
        try:
            title = i.find_element_by_class_name("item-basic-info").find_element_by_tag_name("a").get_attribute("title")
            print(title)
        except Exception as e:
            continue

        try:
            url = i.find_element_by_class_name("item-basic-info").find_element_by_tag_name("a").get_attribute("href")
        # 处理ulr得到uid
            taobaosdk = url.split("=")[1]
            # print("淘宝sdk",taobaosdk)
            requid = str(taobaosdk) + "-83"
            # maxminprice_list(requid)
            print(url)
        except Exception as e:
            continue

        try:
            imgurl = i.find_element_by_class_name("item-pic").find_element_by_tag_name("img").get_attribute("src")
            hight_img="https://img.alicdn.com/bao/uploaded/i4"+imgurl.split("/i",1)[1].split("jpg_",1)[0]+"jpg_430x430.jpg"
            print(hight_img)
        except Exception as e:
            continue

        try:
            price = i.find_element_by_class_name("td-inner").find_element_by_tag_name("em").text.split("¥", 1)[1]
            print(price)
        except Exception as e:
            continue

        # try:
        #     shop = i.find_element_by_class_name("shop-info").find_element_by_tag_name("a").text
        # except Exception as e:
        #     continue

        # temps = (hight_img, url, title, price, maxprice, maxdate, minprice, mindate, None, "淘宝购物车", "淘宝")
        # temps = (hight_img, url, title, price,None, "淘宝购物车", "淘宝")
        # tbcars.append(temps)
    # print(tbcars)
    browser.close()

spider_taobao()