# 爬取京东购物车的东西
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time
from sql import sqlhelper
import requests
browser=Chrome()
browser.get("https://passport.jd.com/new/login.aspx?")
while browser.current_url.startswith("https://passport.jd.com/new/login.aspx?"):
    print("等着")
    time.sleep(1)

browser.get("https://cart.jd.com/cart?")
time.sleep(2)
items=browser.find_element_by_class_name('item-list').find_elements_by_class_name("item-give")
# print(items)
cargoods=[]
for i in items:
    href=i.find_element_by_class_name("item-form").find_element_by_class_name("goods-item").find_element_by_tag_name("a").get_attribute("href")
    print(href)

    title=i.find_element_by_class_name("item-form").find_element_by_class_name("p-name").find_element_by_tag_name("a").text
    print(title)

    img=i.find_element_by_class_name("item-form").find_element_by_class_name("goods-item").find_element_by_tag_name("img").get_attribute("src")
    print(img)

    price = i.find_element_by_class_name("plus-switch").find_element_by_tag_name("strong").text
    print(price)

    # discount=i.find_element_by_class_name("mt5").find_element_by_tag_name("span").text
    # discount=i.find_element_by_class_name("item-form").find_element_by_class_name("mt5").is_displayed()
    # if discount:
    #     count = i.find_element_by_class_name("mt5").find_element_by_tag_name("span").text
    # else:
    #     count="没有折扣"
    # print(count)
    location="jdcars"
    temp=(href,title,img,price,location)
    cargoods.append(temp)

# print(cargoods)
obj=sqlhelper.SQLHELPER()
obj.multiple_modify('insert into taobao(url,title,img,price,location) values(%s,%s,%s,%s,%s)',cargoods)
print("insert success!!")