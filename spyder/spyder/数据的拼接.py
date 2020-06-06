from urllib.parse import urlencode

v={
    'k1':'v1',
    'k2':'v3',
}
result=urlencode(v)
print(result)