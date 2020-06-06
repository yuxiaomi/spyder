import requests
from bs4 import BeautifulSoup

response=requests.get('https://www.dytt8.net/')
response.encoding='gb2312'
# print(response.text)
soup=BeautifulSoup(response.text,'html.parser')
div=soup.find(name='div',attrs={'class':'co_content8'})
tr=div.find_all(name='tr')
# for td in tr:
#     d=td.attrs.get(name=td)
#     print(d)
# td=tr.attrs.get('href')
# print(td)
# for li in tr:
#     if not li:
#         continue
#         print(li)
    # a=li.find(name='a')
#     if not a:
#         continue
#         print(a)
