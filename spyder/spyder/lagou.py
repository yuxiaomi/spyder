import requests
from bs4 import  BeautifulSoup

url='https://passport.lagou.com/login/login.html'
headers = {'User-Agent': 'Mozilla/5.0(Macintosh;Intel Mac 05 X 10_11_4)AppleWebKit/537.36(KHTML,like Gecko)Chrome/52.0.2743.116 Safari/537.36'}
r1=requests.get(url,headers)
print(r1.text)
# soup=BeautifulSoup(r1.text,'html.parser')
data={
"isValidate": True,
"username": 13212701015,
"password": '8c17658aa102e51020f3f2ded0148bde',
"request_form_verifyCode":" ",
'submit': '',
'challenge': 'c46e505b69afa295a6cb3c2422ef4e97',
}
head={'User-Agent': 'Mozilla/5.0(Macintosh;Intel Mac 05 X 10_11_4)AppleWebKit/537.36(KHTML,like Gecko)Chrome/52.0.2743.116 Safari/537.36',


}
url='https://passport.lagou.com/login/login.html'
r2=requests.post(url,headers,data)

requests.get(
    url='xxx',
    headers={},
    cookies={},
    params={'k1':'v1','k2':'v2'},#http://www.baidu.com?k1=v1/k2=v2
)
requests.post(
    url='xxx',
    headers={},
    cookies={},
    params={},
    data={},
)