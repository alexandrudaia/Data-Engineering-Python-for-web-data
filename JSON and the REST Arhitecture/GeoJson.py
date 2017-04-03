import urllib
import json
serviceurl='http://maps.googleapis.com/maps/api/geocode/json?'
data='http://python-data.dr-chuck.net/geojson'
data=urllib.urlopen(data).read()
data
len(data)
data[1]
address='Moscow Institute of Physics & Technology'
url=serviceurl+urllib.urlencode({'sensor':'false','address':adress})
url=serviceurl+urllib.urlencode({'sensor':'false','address':address})
url
uh=urlib.urlopen(url)
uh=urllib.urlopen(url)
uh
data=uh.read()
data
js=json.loads(str(data))
js
js['place_id']
print(json.dumps(js,indent=4))
js['results'][0]["place_id"]
str(js['results'][0]["place_id"])
%history -f GeoJson.py
