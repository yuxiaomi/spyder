from bs4 import BeautifulSoup
import requests
def jd(type,keys,num):
    if(type=="search"):
        re = requests.get(
            url="https://search.jd.com/Search?keyword="+keys+"&enc=utf-8&",
            headers={
                'User-Agent': 'Mozilla/5.0(Macintosh;Intel Mac 05 X 10_11_4)AppleWebKit/537.36(KHTML,like Gecko)Chrome/52.0.2743.116 Safari/537.36'
            })
        re.encoding='utf-8'
        # print(re.text)
        soup=BeautifulSoup(re.text,'html.parser')
        li=soup.find(attrs={'class':'gl-warp clearfix'}).find_all(attrs={'class':"gl-item"})
        # print(li_list)
        jdsearch=[]
        flag=1
        for list in  li:
            imgattrs=list.find(name='div').find(attrs={'class':"p-img"}).select("a img")
            imgsrc=imgattrs[0].get('source-data-lazy-img')
            # print(imgsrc)

            a=list.find(class_="p-name").select("a")
            url=a[0].get('href')
            # print(url)

            em=list.find(class_="p-name").select("a em")
            title=em[0].text
            # print(title)

            iprice=list.find(class_="p-price").select("strong i")
            price=iprice[0].text
            # print(price)

            acomment=list.find(class_="p-commit").select("strong a")
            deal=acomment[0].text
            # print(deal)

            ashop=list.find(class_="p-shop").select("span a")
            if (ashop):
                shop = ashop[0].get('title')
            else:
                shop=" "
            location="京东搜索"
            temp=(url,title,imgsrc,shop,price,deal,location)
            jdsearch.append(temp)
            flag = flag + 1
            if (flag > int(num)):
                break
    print(jdsearch)

if __name__ == '__main__':
    jd("search","女装",10)