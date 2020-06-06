import requests,re
from bs4 import BeautifulSoup
from selenium import webdriver
import time

browser=webdriver.Chrome()
browser.get("https://login.taobao.com/member/login.jhtml?redirectURL=http%3A%2F%2Fcart.taobao.com%2Fcart.htm%3Fspm%3Da21bo.2017.1997525049.1.5af911d9iofkS1%26from%3Dmini%26pm_id%3D1501036000a02c5c3739")
time.sleep(10)
pagesouce=browser.page_source
cookie=browser.get_cookies()
print(pagesouce)
print('----------------------')
print(cookie)
# browser.close()