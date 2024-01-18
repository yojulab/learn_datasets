import requests

url = 'http://httpbin.org/get' # get()
url = 'http://httpbin.org/post' # post()
url = 'http://httpbin.org/put' # put()
url = 'http://httpbin.org/delete' # delete()
url = 'http://blog.naver.com/otter35'
url = 'https://www.coupang.com/'
# https://www.whatismybrowser.com/detect/what-is-my-user-agent

params = {'first':'data_one', 'second':'data_two'}
header = {'User-Agent': '', 'Content-Type':'application/json; charset=utf-8', 'add-data':'something'}

# Try coutinue 3 times without headers-> Timeout
res = requests.get(url=url, params=params, headers=header)

# datas = {'first':'data_one', 'second':'data_two'}
# res = requests.post(url=url, params=params, headers=header, data=datas)

print(type(res), res)
# <class 'requests.models.Response'> <Response [200]>

print(res.status_code)
if(res.status_code == 200):
    with open('datas/response01.html', 'w') as fp:
        fp.write(res.text)