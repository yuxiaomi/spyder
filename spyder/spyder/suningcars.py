from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException,NoSuchElementException
import time
from sql import sqlhelper
import requests
browser=Chrome()
browser.get("https://passport.suning.com/ids/login?")

while browser.current_url.startswith("https://passport.suning.com/ids/login?"):
    print("等着")
    time.sleep(1)

browser.get("https://shopping.suning.com/cart.do")
time.sleep(1)

items=browser.find_element_by_class_name("m-cart-body").find_elements_by_class_name("item-main")
# print(items)
sncars=[]
for i in items:
    imgurl=i.find_element_by_class_name("item-pic").find_element_by_tag_name("img").get_attribute("src")
    # print(imgurl)
    title=i.find_element_by_class_name("item-info").find_element_by_tag_name("a").text
    # print(title)
    href=i.find_element_by_class_name("item-info").find_element_by_tag_name("a").get_attribute("href")
    # print(href)
    price=i.find_element_by_class_name("price-line").text
    location="suningcars"
    temp=(href,title,imgurl,price,location)
    sncars.append(temp)
print(sncars)
obj=sqlhelper.SQLHELPER()
obj.multiple_modify('insert into taobao(url,title,img,price,location) values(%s,%s,%s,%s,%s)',sncars)
print("insert success!!")