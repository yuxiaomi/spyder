import requests
from bs4 import BeautifulSoup

response=requests.get("https://www.autohome.com.cn/news/")
response.encoding='gbk'
# print(response.text)

soup=BeautifulSoup(response.text,'html.parser')
div=soup.find(name='div',attrs={'id':'auto-channel-lazyload-article'})
lilist=div.find_all_next(name='li')
for li in lilist:
    title=li.find(name='h3')
    if not title:  #不存在title的时候  则继续
        continue
    p=li.find(name='p')
    a=li.find(name='a')
    img=li.find(name='img')
    img_src="https:"+img.get('src')#img.get 会直接调用 attrs的方法
    # print(title)#这样取得是标签对象
    print(title.text)#这样才是取值
    print(p.text)
    print("https:"+a.attrs.get('href'))#attrs 拿到是字典  这样就可以只取 href
    print(img_src)

    #再次发起请求 下载图片
    # filename=img_src.rsplit('/',maxsplit=1)[1]
    # ret=requests.get(img_src)
    # with open(filename,'wb')as f:
    #    f.write(ret.content)