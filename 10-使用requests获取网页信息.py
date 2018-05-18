import requests



url = "http://example.org/"
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
req = requests.get(url,headers=header)


print(req.content)
print('*'*100)
print(req.headers)
print('*'*100)
print(req.status_code)
# print(content)