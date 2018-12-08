import requests
res = requests.get('https://news.sina.com.cn/china/')
#打印编码
#res.encoding
res.encoding="utf-8"
print(res.text)
