import requests
"""
# 1.方法
requests.requests(method="post")
# 2.参数
2.1 url
2.2 headers
2.3 cookies
2.4 params
2.5 data 传请求体
    request.post(
    .....
    data={'user':'root','pwd':'123'}
    )
    GET /index  http1.1\r\n host:c1.com\r\n\r\nuser=root&ped=123
2.6 json 传请求体
 request.post(
    .....
    json={'user':'root','pwd':'123'}
    )
    GET /index  http1.1\r\n host:c1.com\r\nContent-Type:application/json\r\n{"user":"root","pwd":"123"}
2.7代理
    #无验证
    proxies_dict = {"http": "61.172.249.96:80","https": "http://61.185.219.126:3128",} 设置代理的ip
    proxies_dict = {'http://10.20.1.128': 'http://10.10.1.10:5323'}设置代理的ip 端口
    ret = requests.get("http://www.proxy360.cn/Proxy", proxies=proxies_dict) 使用http的代理 https 使用https的代理
    print(ret.headers)
    
    #带验证的代理
    from requests.auth import HTTPProxyAuth
    proxyDict = {'http': '77.75.105.165','https': '77.75.105.165'}
    auth = HTTPProxyAuth('username', 'password')
    r = requests.get("http://www.google.com",data={'xxx':'fff'} proxies=proxyDict, auth=auth) 通过给的账户 密码验证
    print(r.text)
2.8文件上传（代码上传 发布）
        发送文件
        file_dict = {'f1': open('xxx.log', 'rb')}
        file_dict = {'f1': ('test.txt', open('readme', 'rb'))} 发送文件，定制文件名 test.txt
        file_dict = {'f1': ('test.txt', "hahsfaksfa9kasdjflaksdjf")} 发送定制文件名 test.txt
        file_dict = {'f1': ('test.txt', "hahsfaksfa9kasdjflaksdjf", 'application/text', {'k1': '0'})}
        requests.request(method='POST',url='http://127.0.0.1:8000/test/',files=file_dict)
2.9认证 auth（浏览器的弹窗做的）
    内部：
    用户名和密码加密(base64 basic)放在请求头中，传给后台。
    "用户|密码"  base64("用户:密码") "basic base64("用户:密码")" 请求头：Authorization "basic base64("用户:密码")"
    from requests.auth import HTTPBasicAuth, HTTPDigestAuth
    HTTPBasicAuth 会自动构造basic base64("用户:密码")
    ret = requests.get('https://api.github.com/user', auth=HTTPBasicAuth('admin', 'admin')) 
    print(ret.text)

    # ret = requests.get('http://192.168.1.1',
    # auth=HTTPBasicAuth('admin', 'admin'))
    # ret.encoding = 'gbk'
    # print(ret.text)
2.10超时 timeout  
    ret = requests.get('http://google.com/', timeout=1) 
    ret = requests.get('http://google.com/', timeout=(5, 1)) 链接时间5秒 返回信息时间1秒
    print(ret)

2.11允许重定向 allow_redirects
    ret = requests.get('http://127.0.0.1:8000/test/', allow_redirects=False) 不允许重定向
    print(ret.text)

2.12 大文件下载 stream
    # ret = requests.get('http://127.0.0.1:8000/test/', stream=True)
    # print(ret.content)
    # ret.close()
    
    # 一点一点的取数据
    from contextlib import closing
    with closing(requests.get('http://httpbin.org/get', stream=True)) as r:
    # 在此处理响应。
    for i in r.iter_content():
        print(i)

2.13证书 cert
#现在很多网站  系统会自动下载证书
    自定义证书
    ret = requests.get('http://127.0.0.1:8000/test/', cert=("xxx/xxx/xxx.pem","xxxx.key"))

2.14确认 verify=False
"""
"""
requests.get(
    url='http://www.baidu.com',
    head={},
    cookies={},
    params={'k1':'v1','k2':'v2'} #http://www.baidu.com?k1=v1&k2=v2
)
requests.post(
    url='xxx',
    head={},
    cookies={},
    params={'k1':'v1','k2':'v2'}, #http://www.baidu.com?k1=v1&k2=v2
    data={}
)
"""

# session相关
# session=requests.sessions()
# session.get()
# session.post()

