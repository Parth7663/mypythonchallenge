import urllib.request
import re
import bz2

req = urllib.request.Request('http://www.pythonchallenge.com/pc/def/integrity.html')
page = urllib.request.urlopen(req).read().decode("utf-8")

key = re.findall("<!--([^-]+)", page)[0].split("'")

un = key[1].encode("latin-1").decode("unicode-escape").encode("latin1")
pw = key[3].encode("latin-1").decode("unicode-escape").encode("latin1")

print("un: " + bz2.decompress(un).decode("latin1"))
print("pw: " + bz2.decompress(pw).decode("latin1"))
