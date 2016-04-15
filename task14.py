import json
import urllib

address = raw_input('Enter url: ')
if len(address) < 1 : print 'No url entered'

data = urllib.urlopen(address).read()

js = json.loads(data)
print 'Num of comments: ', len(js["comments"])

total = 0
for item in js["comments"]:
	total += int(item["count"])

print 'Totola: ', total
