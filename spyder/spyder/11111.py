#京东做了反爬措施。直接抓取html内容不成功，所以要找到请求接口输入skuIds（商品代号），得到json字符串
import urllib
from bs4 import BeautifulSoup
import requests

jd = "https://p.3.cn/prices/mgets?callback=jQuery6710688&type=1&area=1&pdtk=&pduid=1132198894&pdpin=&pin=null&pdbp=0&skuIds=J_5089225%2CJ_3319787%2CJ_4911001%2CJ_6027746%2CJ_771942%2CJ_899777%2CJ_5524603%2CJ_20178448828%2CJ_5338456%2CJ_11010467023%2CJ_11170365589&ext=11100000&source=item-pc"
#苏宁也做了反爬，打开浏览器调试器找到接口，获取一段json字符串
SuNing="https://pas.suning.com/nspcsale_0_000000000690105188_000000000690105188_0000000000_10_010_0100101_20089_1000000_9017_10106_Z001___R1901001_0.39_0_.html?callback=pcData&_=1528718505339"
#唯品会可以直接通过html内容抓取价格
WeiPinghui="https://detail.vip.com/detail-2959674-534092575.html"

#解析网址或解析请求接口信息
request_data1=urllib.request.urlopen(jd)
request_data2=urllib.request.urlopen(SuNing)
request_data3=urllib.request.urlopen(WeiPinghui)
contentx1=request_data1.read().decode("UTF-8")
contentx2=request_data2.read().decode('utf-8')
contentx3=request_data3.read().decode('utf-8')

#取得key=’p‘对应的值，得到京东上 iphone8 价格
price1=str(contentx1).split('\"p\":\"')[1]
price1=price1.split('\"')[0]

#苏宁返回的json字符串较复杂，直接还原成字符串，split（）分离出想要的结果，效果等同于从多层嵌套的列表和字典中找到key为promotionPrice的值
price2=str(contentx2).split('promotionPrice\":\"')[1]
# price2=price2.split('\"')[0]
print(price2)

#通过bs库BeautifulSoup（）进行html语法解析
# soup3=BeautifulSoup(contentx3,"html.parser")

#通过bs库find_all（）过滤得到价格区间字符串。
# 中间有～字符，所以先split（）过滤一次，取第一个有效字符串得到唯品会 iPhone8 价格
# price3=soup3.find_all('span',attrs={"class":"J-price"})[0].string.split('~')[0]


price1 = float(price1)
# price2 = float(price2)
# price3 = float(price3)
