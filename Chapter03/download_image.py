import urllib2
import re
from os.path import basename
from urlparse import urlsplit

url = 'https://www.packtpub.com/'

response = urllib2.urlopen(url)
source = response.read()
file = open("packtpub.txt", "w")
file.write(source)
file.close()

patten = '(http)?s?:?(\/\/[^"]*\.(?:png|jpg|jpeg|gif|png|svg))'
for line in open('packtpub.txt'):
    for m in re.findall(patten, line):
        print('https:' + m[1])
        fileName = basename(urlsplit(m[1])[2])
        print(fileName)
        try:
            img = urllib2.urlopen('https:' + m[1]).read()
            file = open(fileName, "w")
            file.write(img)
            file.close()
        except:
            pass
        break
