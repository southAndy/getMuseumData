import urllib.request as req

url = 'https://www.ptt.cc/bbs/Stock/index.html'

try:
    response = req.urlopen(url)
    print(url)
finally:
    # response.close()
    print('hello world')
