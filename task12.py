import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

tags = soup('span')
count = 0
for tag in tags:
    nums = int(tag.contents[0])
    count = count + nums
print count
