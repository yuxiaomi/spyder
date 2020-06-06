import requests
from bs4 import BeautifulSoup

#得到cookie1 和authenticity_token
r1=requests.get(
    url='https://github.com/login',
    headers={
        'User-Agent': 'Mozilla/5.0(Macintosh;Intel Mac 05 X 10_11_4)AppleWebKit/537.36(KHTML,like Gecko)Chrome/52.0.2743.116 Safari/537.36'})
soup=BeautifulSoup(r1.text,'html.parser')
form=soup.find(name='form')
token=form.find(attrs={'name':'authenticity_token'})
authenticity_token=token.get('value')
cookie1=r1.cookies.get_dict()
r1.close()
# print(authenticity_token)

#登录
from_data={
    'authenticity_token': authenticity_token,
    "utf-8":"",
    "commit":"sign in",
    'login': 'yuxiaomi',
    'password': '52067.lt',
}
r2=requests.post('https://github.com/session',data=from_data,cookies=cookie1)
cookie2=r2.cookies.get_dict()
cookie1.update(cookie2)#把第二次得到的cookies加到第一次的值上面

r3=requests.get('https://github.com/settings/emails',cookies=cookie1)
f=open('r3.html','w',encoding='utf-8')
# f.write(r3.text)
# f.close()
# print("写入完成")
# print(r3.text)
soup=BeautifulSoup(r3.text,'html.parser')
div=soup.find(name='li',attrs={'class':'Box-row'})
email=div.find(name='h4')
print('email:',email.text)





# r2=requests.post(
# url='https://github.com/session',
#     headers={
#         'User-Agent': 'Mozilla/5.0(Macintosh;Intel Mac 05 X 10_11_4)AppleWebKit/537.36(KHTML,like Gecko)Chrome/52.0.2743.116 Safari/537.36'
#     },
#     data={
#         'authenticity_token':authenticity_token,
#         'login': 'yuxiaomi',
#         'password': '52067.lt',
#     }
# )
# print(r2.text)
# # print(r2.cookies.get_dict())
# #到自己的主页
# r3=requests.get(
#     url='https://github.com/settings/emails',
# headers={
#     'User-Agent': 'Mozilla/5.0(Macintosh;Intel Mac 05 X 10_11_4)AppleWebKit/537.36(KHTML,like Gecko)Chrome/52.0.2743.116 Safari/537.36'
# },
#     cookies=r2.cookies.get_dict()
# )
# print(r3.text)
# soup=BeautifulSoup(r3.text,'html.parser')
# div=soup.find(name='div',attrs={'class':'Subhead'})
# print(div)
