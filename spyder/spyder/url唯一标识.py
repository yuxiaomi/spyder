from scrapy.utils.request import request_fingerprint
from scrapy.http import Request
url1="http:///www.baidu.com?k1=123&k2=456"
rep1=Request(url=url1)
url2="http:///www.baidu.com?k2=456&k1=123"
rep2=Request(url=url2)

fd1=request_fingerprint(request=rep1)
fd2=request_fingerprint(request=rep2)