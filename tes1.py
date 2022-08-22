# 193.58.168.68:1051:Mv47Xq:OLwHrOlBug
# 45.142.252.243:1051:Mv47Xq:OLwHrOlBug
import requests
import urllib

proxies = {
    "http":"http://Mv47Xq:OLwHrOlBug@193.58.168.68:1051",
    "https":"https://Mv47Xq:OLwHrOlBug@193.58.168.68:1050"}
ses = requests.Session()
ses.proxies = proxies
# session = requests.Session()
# session.proxies.setdefault('http', 'http://127.0.0.1:9009')
# session.proxies.update(proxies)
data = ses.get("https://ipinfo.io/json")
print(data.text)
# proxies = {"http":"http://Mv47Xq:OLwHrOlBug@193.58.168.68:1051"}
#
# r = requests.get("http://www.example.com/", proxies=proxies)
#
# print(r.content)