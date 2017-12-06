import urllib.request as url
import re

req = url.Request('http://www.pythonchallenge.com/pc/def/equality.html')
with url.urlopen(req) as response:
    text = str(response.read())

text = re.findall(r'\<!--([^-]+)--\>', text)[0]
text = text.replace(r'\n', '')

result = re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', text)

print("".join(result))
