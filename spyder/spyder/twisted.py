"""
原来
import requests
url_list = ['http://www.bing.com', 'http://www.baidu.com', ]
for item in url_list:
    response=response.get(item)
    print(response.text)
"""

from twisted.web.client import getPage, defer
from twisted.internet import reactor
"""
非阻塞，不等待（把请求全发出去 不等待链接成功  之后在处理返回）
异步，回调  （成功之后会有通知 体现在callback函数上）
事件循环，（一直循环socket任务 检查状态（是否连接成功，是否返回信息））
    基于事件循环的异步非阻塞的模块
    一个线程 同时可以向多个http发送请求
"""
# 第一部分：代理开始接受任务
def callback(contents):
    print(contents)

deferred_list = []
url_list = ['http://www.bing.com', 'http://www.baidu.com', ]
for url in url_list:
    deferred = getPage(bytes(url, encoding='utf8'))
    deferred.addCallback(callback)
    deferred_list.append(deferred)

# 第二部分：代理执行完任务后，停止
dlist = defer.DeferredList(deferred_list)
def all_done(arg):
    reactor.stop()
dlist.addBoth(all_done)

# 第三部分：代理开始处理
reactor.run()
