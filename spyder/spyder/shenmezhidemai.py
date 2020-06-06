import requests,re
from bs4 import BeautifulSoup

#什么值得买的  历史低价
def history_low_price():
    r1=requests.get(
        url='https://search.smzdm.com/?c=home&s=%E5%8E%86%E5%8F%B2%E4%BD%8E%E4%BB%B7&v=a',
        headers={
            'User-Agent': 'Mozilla/5.0(Macintosh;Intel Mac 05 X 10_11_4)AppleWebKit/537.36(KHTML,like Gecko)Chrome/52.0.2743.116 Safari/537.36'})
    # print(r1.text)
    soup=BeautifulSoup(r1.text,'html.parser')
    ul=soup.find(name='ul',id='feed-main-list')
    li_all=ul.find_all(name='li',attrs={'class':'feed-row-wide'})
    # print(li_all)
    for list in li_all:
        div=list.find(name='div')
        tagclass = div.find(name='span').text# 是推荐的商品会有此标签
        # print(tagclass)
        if tagclass != "国内优惠":
            continue
        a=div.find(name='a')
        title=a.get('title')
        try:
            title=title.split(':',1)[1]
        except Exception as e:
            continue
        href=a.get('href')
        img=a.find(name='img')
        img_src=img.get('src')
        print('title:',title,'href:',href,'img:',img_src)

#什么值得买的精选
def jingxuan():
    r1 = requests.get(
        url='https://www.smzdm.com/jingxuan/',
        headers={
            'User-Agent': 'Mozilla/5.0(Macintosh;Intel Mac 05 X 10_11_4)AppleWebKit/537.36(KHTML,like Gecko)Chrome/52.0.2743.116 Safari/537.36'})
    # print(r1.text)
    soup = BeautifulSoup(r1.text, 'html.parser')
    ul = soup.find(name='ul', id='feed-main-list')
    li_all = ul.find_all(name='li', attrs={'class': 'feed-row-wide'})
    # print(li_all)
    for list in li_all:
        div1=list.find(name='div')
        div=div1.find(name='div')
        a=div.find(name='a')
        # print(type(a))
        a_text=str(a)
        title=re.search(".*pagetitle':'(.*)\',.*",a_text)
        # print(title.group(1))
        title=title.group(1)
        href=a.get('href')
        img = a.find(name='img')
        img_src = img.get('src')
        price=list.find(name='div',class_="z-highlight")
        # print(price)
        print('title:',title,'href:',href,'img:',img_src)
def reach():
    import re
    text="title':'13日0点：天王 雅仕系列 3502 男士石英腕表','PC所有AB测试集合"
    r=re.search(".*?e':'(.*)\',.*",text)
    s=text.split(':\'',1)[1]
    # print(s)
    print(r.group(1))


def history():
    resp = requests.get(
        url='https://search.smzdm.com/?c=faxian&s=%E5%8E%86%E5%8F%B2%E4%BD%8E%E4%BB%B7&v=b',
        headers={
            'User-Agent': 'Mozilla/5.0(Macintosh;Intel Mac 05 X 10_11_4)AppleWebKit/537.36(KHTML,like Gecko)Chrome/52.0.2743.116 Safari/537.36'})
    # print(r1.text)
    soup = BeautifulSoup(resp.text, 'html.parser')
    list = soup.find(name='ul', id='feed-main-list').find_all(name="li",class_="feed-row-wide")
    # print(list)
    hscom=[]
    for item in list:
        ahref=item.find(name="div",class_="z-feed-content").select("h5 a")
        href=ahref[0].get("href")
        title=ahref[0].text.replace(" ","").replace('\n',"").replace('\r',"")
        # print(href)
        # print(title)

        img=item.find(name="div",class_="z-feed-img").select("a img")
        imgurl=img[0].get("src")
        # print(imgurl)

        price=item.find(name="div",class_="z-highlight").text.replace(" ","").replace('\n',"").replace('\r',"")
        # print(price)

        desc=item.find(name="div",class_="feed-block-descripe").text.replace(" ","").replace('\n',"").replace('\r',"")
        text=re.search("低价(.*)",desc)[0]
        desc=text[0:45]
        temp=(href,title,imgurl,price,desc)
        hscom.append(temp)
    print(hscom)

def jx():
    resp = requests.get(
        url='https://www.smzdm.com/jingxuan/xuan/s0f0t0b0d1r0p1/',
        headers={
            'User-Agent': 'Mozilla/5.0(Macintosh;Intel Mac 05 X 10_11_4)AppleWebKit/537.36(KHTML,like Gecko)Chrome/52.0.2743.116 Safari/537.36'})
    print(resp.text)
    soup = BeautifulSoup(resp.text, 'html.parser')
    list = soup.find(name='ul', id='feed-main-list').find_all(name="li", class_="feed-row-wide")
    # print(list)
    jxcom = []
    for item in list:
        # ahref=item.find(name="div",class_="z-feed-content").select("h5 a")
        # href=ahref[0].get("href")
        # title=ahref[0].text.replace(" ","").replace('\n',"").replace('\r',"")
        # print(href,title)

        img=item.find(name="div",class_="z-feed-img").select("a img")
        imgurl=img[0].get("src")
        print(imgurl)

        price=item.find(name="div",class_="z-feed-conten").select("h5 a").next_siblings()
        print(price)








def test():
    import re
    text="标签：历史低价粉色镂空天鹅，空灵少女感气"
    res=re.search("低价(.*)",text)
    print(res[0])




if __name__ == '__main__':
    # history_low_price()
    # jingxuan()
    # re()
    # history()
    jx()
    # test()
