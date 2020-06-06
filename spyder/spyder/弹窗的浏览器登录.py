import requests
from requests.auth import HTTPBasicAuth, HTTPDigestAuth

ret = requests.get('http://192.168.1.44/', auth=HTTPBasicAuth('admin', '123'))
print(ret.text)