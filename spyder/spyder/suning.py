from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException,NoSuchElementException
import time
from sql import sqlhelper
import requests
browser=Chrome()
browser.get("https://www.suning.com/")
browser.find_element_by_xpath('//*[@id="searchKeywords"]').send_keys('手机',Keys.ENTER)

# while browser.current_url.startswith("https://www.suning.com/"):
#     print("等着")
#     time.sleep(1)
time.sleep(2)

# time.sleep(2)
# js="document.documentElement.scrollTop=10000" #滚动到最下面
# browser.execute_script(js)
items=browser.find_element_by_id("product-list").find_elements_by_class_name("item-wrap")
print(items)
sngoods=[]
for i in items:
    imgurl=i.find_element_by_class_name("res-img").find_element_by_tag_name("img").get_attribute("src")
    # print(imgurl)
    title=i.find_element_by_class_name("title-selling-point").find_element_by_tag_name("a").text
    # print(title)
    href=i.find_element_by_class_name("title-selling-point").find_element_by_tag_name("a").get_attribute("href")
    # print(href)
    price=i.find_element_by_class_name("price-box").find_element_by_class_name("def-price").text
    try:
        deal=i.find_element_by_class_name("info-evaluate").find_element_by_tag_name("i").text
        # print(deal)
    except NoSuchElementException:
        deal=""
    shop=i.find_element_by_class_name("store-stock").text
    # print(shop)
    location="suning"
    temp=(href,title,imgurl,shop,price,deal,location)
    sngoods.append(temp)
print(sngoods)
obj=sqlhelper.SQLHELPER()
obj.multiple_modify('insert into taobao values(%s,%s,%s,%s,%s,%s,%s)',sngoods)
print("insert success!!")