from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time
from sql import sqlhelper
import requests
browser=Chrome()
browser.get("https://www.jd.com/")
browser.find_element_by_xpath('//*[@id="key"]').send_keys('手机',Keys.ENTER)
while browser.current_url.startswith("https://www.jd.com/"):
    print("等着")
    time.sleep(1)
time.sleep(2)

js="document.documentElement.scrollTop=10000" #滚动到最下面
browser.execute_script(js)

items=browser.find_element_by_class_name('gl-warp').find_elements_by_class_name("gl-item")
# print(items)
goods=[]
# 定义爬取的数量
num=10
for a in range(num):
    for i in items:
        href=i.find_element_by_class_name("p-name").find_element_by_tag_name("a").get_attribute("href")
        # print(href)

        title=i.find_element_by_class_name("p-name").find_element_by_tag_name("em").text
        # print(title)

        img=i.find_element_by_class_name("p-img").find_element_by_tag_name("img").get_attribute("src")
        # print(img)

        shop=i.find_element_by_class_name("p-shop").find_element_by_tag_name("a").get_attribute('title')
        # print(shop)

        price=i.find_element_by_class_name("p-price").find_element_by_tag_name("i").text
        # print(price)

        deal=i.find_element_by_class_name("p-commit").find_element_by_tag_name("a").text
        # print(deal)

        location="jd"
        temp=(href,title,img,shop,price,deal,location)
        goods.append(temp)

print(goods)
# obj=sqlhelper.SQLHELPER()
# obj.multiple_modify('insert into taobao values(%s,%s,%s,%s,%s,%s,%s)',goods)
print("insert success!!")