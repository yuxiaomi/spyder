import re

def jdimgparse(url):
    old=url.split("jfs",1)[1]
    head="https://img12.360buyimg.com/cms/jfs"
    newimgurl=head+old
    return newimgurl
    # print(new)

def getjdnow(price):
    old=price.split("¥",1)[1]
    print(old)

def taobaoimgparse(url):
    # old=re.search("i1(.*).jpg",url)
    old=url.split("/i",1)[1].split("jpg_",1)[0]
    print(old)
    new="https://img.alicdn.com/bao/uploaded/i4"+old+"jpg_430x430.jpg"
    print(new)

def suningparse(url):
    old=url.split("jpg_",1)[0]
    print(old)
    new=old+"jpg_800w_800h_4e"
    print(new)
https="//img10.360buyimg.com/cms/s80x80_jfs/t16303/312/96696437/192541/c3ceeeee/5a27ba9cN5d5a07e8.jpg"
# jdimgparse(https)
# getjdnow("¥6399.00")
url="https://img.alicdn.com/bao/uploaded/i3/2452099214/O1CN01kfwnEM2Hw3uY0lVWp_!!0-item_pic.jpg_80x80.jpg"
url="https://img.alicdn.com/bao/uploaded/i1/2204109094269/O1CN01ZRMaD11hPFOXygCzA_!!0-item_pic.jpg_80x80.jpg"
# taobaoimgparse(url)

suningparse("https://imgservice.suning.cn/uimg1/b2c/image/IURm-I23Kdpej-pxgkiY3w.jpg_100w_100h_4e")