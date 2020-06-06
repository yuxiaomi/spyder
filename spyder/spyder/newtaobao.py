# 1.安装selenium 安装chrome驱动
# 2.应用selenium中的chrome
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time
from sql import sqlhelper
import requests

# 3.创建浏览器
browser=Chrome()

# 设置显示的大小
# browser.set_window_size(200,200)

# 4.打开淘宝
browser.get("https://www.taobao.com/")
# 5.找到搜索框 输入内容 并搜索
browser.find_element_by_xpath('//*[@id="q"]').send_keys("女装",Keys.ENTER)

# 6.让程序等待  用户手动登录
while browser.current_url.startswith("https://login.taobao.com/"):
    print("等着")
    time.sleep(1)

n=1
dd_list=[]
# 7.找到页面中的所有的item
if n<=1:
    items=browser.find_element_by_class_name("m-itemlist").find_elements_by_class_name("item")
    for i in items:
        src_path=i.find_element_by_class_name("pic-box").find_element_by_tag_name("img").get_attribute("data-src")
        img_path="http:"+src_path

        url=i.find_element_by_class_name("ctx-box").find_element_by_class_name("J_ClickStat").get_attribute("href")

        title=i.find_element_by_class_name("ctx-box").find_element_by_class_name("J_ClickStat")
        title1=title.text
        # print(title1)

        deal=i.find_element_by_class_name('ctx-box').find_element_by_class_name("deal-cnt")
        deal1=deal.text
        # print(deal1)

        shop=i.find_element_by_class_name('ctx-box').find_element_by_class_name("shopname")
        shop1=shop.text
        # print(shop1)

        location=i.find_element_by_class_name('ctx-box').find_element_by_class_name("location")
        location1=location.text
        # print(location1)

        price=i.find_element_by_class_name('ctx-box').find_element_by_class_name("price")
        price1=price.text
        # print(price1)

        temp=(url,title1,img_path,shop1,price1,deal1,location1)
        # temp=(url,title1,img_path,shop1,deal1,location1)
        dd_list.append(temp)
#8.保存信息  下载图片
        # open(f"{n}.jpg",mode="wb").write(requests.get(img_path).content)
        # n+=1
    # browser.find_element_by_class_name("m-page").find_element_by_class_name("next").click()
    # time.sleep(2)
    # print("下一页")
    # n+=1
print(dd_list)
# obj=sqlhelper.SQLHELPER()
# obj.multiple_modify('insert into taobao values(%s,%s,%s,%s,%s,%s,%s)',dd_list)
# print("insert success!!")


