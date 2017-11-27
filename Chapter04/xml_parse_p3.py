from urllib.request import urlopen
from xml.etree.ElementTree import parse

url = urlopen('http://feeds.feedburner.com/TechCrunch/Google')
xmldoc = parse(url)
xmldoc.write('output.xml')
for item in xmldoc.iterfind('channel/item'):
    title = item.findtext('title')
    desc = item.findtext('description')
    date = item.findtext('pubDate')
    link = item.findtext('link')

    print(title)
    print(desc)
    print(date)
    print(link)
    print('---------')
