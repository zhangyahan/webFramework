import urllib.request


url = "http://www.meituba.com/xinggan/"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64)"
                       "AppleWebKit/534.57.2 (KHTML, like Gecko)"
                       "Version/5.1.7 Safari/534.57.2"}

req = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(req)
if response.getcode() == 200:
    print(response.geturl())
    # print(response.read().decode('gbk'))