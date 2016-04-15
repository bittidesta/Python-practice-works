import urllib
import re
from BeautifulSoup import *

url = raw_input('Entr url ')
position = int(raw_input('Enter position: '))
count = int(raw_input('Enter count: '))
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags = soup('a')

while count >= 0:
    print 'Retriving:'+url
    url = tags[position-1].get('href', None)
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    count = count - 1
