import urllib.request as url
import re
import pandas as pd

req = url.Request('http://www.pythonchallenge.com/pc/def/linkedlist.php')
with url.urlopen(req) as response:
    link = str(response.read())

link = re.findall('href="([^"]+)', link)[1]
link = link[:-5]

a = 0
nothin = ['12345']
while a < 400:
    req = url.Request('http://www.pythonchallenge.com/pc/def/' + link + str(nothin[a]))
    nothin.append("".join(re.findall('[0-9]', str(url.urlopen(req).read()))))
    a += 1

df = pd.DataFrame(nothin)
df.to_csv('~/Workspace/python/pc4-2.csv')
