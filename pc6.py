import urllib.request as url
import zipfile
import re

url.urlretrieve('http://www.pythonchallenge.com/pc/def/channel.zip', 'channel.zip')
channel = zipfile.ZipFile('channel.zip')

i = '90052'
nothing = []
comments = []
while i != '':
    text = channel.open(i+'.txt').read()
    nothing.append(text)

    comment = channel.getinfo(i+'.txt').comment
    comments.append(comment)

    i = "".join(re.findall('[0-9]', str(text)))

c = []
for i in comments:
    c.append(i.decode("utf-8"))

print("".join(c))
