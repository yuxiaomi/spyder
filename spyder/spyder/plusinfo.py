from bs4 import BeautifulSoup
import requests,lxml,datetime
def getevaluate(urls):
    ret=requests.get(
        url=urls,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'
        },
    )
    # print(ret.text)
    bs=BeautifulSoup(ret.text,'lxml')
    eva=bs.find(name="div",id="comment-count").select("a")
    print(eva[0].text)

def long(url):
    num=len(url)
    print(num)
    if(len(url)>3):
        print("40")


if __name__ == '__main__':
    urls="https://item.jd.com/100006288373.html"
    # getevaluate(urls)
    long(urls)