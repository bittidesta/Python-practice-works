import urllib
import xml.etree.ElementTree as ET

url = raw_input('Entr url ')

tree = ET.fromstring(urllib.urlopen(url).read())
counts = tree.findall('comments/comment')
print "Count: ", len(counts)
counr = 0
for count in counts:
    counr += int(count.find('count').text)
print "Sum: ", counr
