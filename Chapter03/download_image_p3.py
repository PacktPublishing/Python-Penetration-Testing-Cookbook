import urllib.request
import urllib.parse
import re
from os.path import basename

url = 'https://www.packtpub.com/'

response = urllib.request.urlopen(url)
source = response.read()
file = open("packtpub.txt", "wb")
file.write(source)
file.close()

patten = '(http)?s?:?(\/\/[^"]*\.(?:png|jpg|jpeg|gif|png|svg))'
for line in open('packtpub.txt'):
    for m in re.findall(patten, line):
        print('https:' + m[1])
        fileName = basename(urllib.parse.urlsplit(m[1])[2])
        print(fileName)
        try:
            img = urllib.request.urlopen('https:' + m[1]).read()
            file = open(fileName, "wb")
            file.write(img)
            file.close()
        except:
            pass
        break
