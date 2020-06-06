from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time
from sql import sqlhelper
browser=Chrome()
browser.get("https://cart.taobao.com/")#淘宝购物车的网址
while browser.current_url.startswith("https://login.taobao.com/"):
    print("等着")
    time.sleep(1)
items=browser.find_element_by_id("J_OrderList").find_elements_by_class_name("J_Order")
# print(items)
cars=[]
for i in items:
    title=i.find_element_by_class_name("item-basic-info").find_element_by_tag_name("a").get_attribute("title")
    print(title)
    url=i.find_element_by_class_name("item-basic-info").find_element_by_tag_name("a").get_attribute("href")
    print(url)
    imgurl=i.find_element_by_class_name("item-pic").find_element_by_tag_name("img").get_attribute("src")
    print(imgurl)
    price=i.find_element_by_class_name("item-price").find_element_by_class_name("J_Price")
    price1=price.text
    print(price1)
    shop=i.find_element_by_class_name("shop-info").find_element_by_tag_name("a")
    shop1=shop.text
    print(shop1)
    source="淘宝购物车"
    temp=(url,title,imgurl,shop1,price1,source)
    cars.append(temp)
# print(cars)
obj=sqlhelper.SQLHELPER()
obj.multiple_modify('insert into taobao(url,title,img,shop,price,location) values(%s,%s,%s,%s,%s,%s)',cars)
print("insert success!!")