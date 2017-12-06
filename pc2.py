import urllib.request as url
import re

req = url.Request('http://www.pythonchallenge.com/pc/def/ocr.html')
with url.urlopen(req) as response:
    text = str(response.read())

text = re.findall(r'\<!--([^-]+)--\>', text)[1]
text = text.replace(r'\n', '')

count = {}
for c in text[0]:
    count[c]=count.setdefault(c, 0)+1

print(count)
