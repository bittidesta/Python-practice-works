import urllib
import json

surl = 'http://python-data.dr-chuck.net/geojson?'

while True:
	address = raw_input('Enter loaction: ')
	if len(address) < 1: break

	url = surl + urllib.urlencode({'sensor':'false', 'address': address})
	print 'Retrieving: ', url
	data = urllib.urlopen(url).read()
	print 'Retrieved:', len(data), 'characters'

	try: js = json.loads(str(data))
	except: js = None
	if 'status' not in js or js['status'] != 'OK':
		print '==== Failure To Retrieve ==='
		print data
		continue
	
	print 'Place id: ', js["results"][0]["place_id"]	
