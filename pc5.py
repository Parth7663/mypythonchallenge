import urllib.request as url
import pickle

req = url.Request('http://www.pythonchallenge.com/pc/def/banner.p')
with url.urlopen(req) as response:
    banner = response.read()

peak = pickle.loads(banner)

u = []
for i in peak:
    v = ''
    for j in i:
        v = v + j[0]*j[1]
    u.append(v)

for i in u:
    print(i)
