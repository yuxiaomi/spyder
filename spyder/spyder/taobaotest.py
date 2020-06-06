from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time

with open('html.html',encoding='utf-8') as f:
    content=f.read()
html=content
items = html('#item item').items()
for item in items:
    product = {
        'href': item.find('.pic .pic-link').attr('data-recommend-nav href'),
        'image': item.find('.pic .img').attr('src'),
        'price': item.find('.price').text(),
        'deal': item.find('.deal-cnt').text(),
        'title': item.find('.row row-2 title').text(),
        'shop': item.find('.shop').text(),
        'location': item.find('.location').text()
    }
    print(product)