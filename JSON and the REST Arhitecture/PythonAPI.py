import  urllib
import json
serviceurl='http://maps.googleapis.com/maps/api/geocode/json?'
adress='Ann Arbor,MI'
url=serviceurl+urllib.urlencode({'sensor':'false','address':adress})
url
adress='Ann Arbor, MI'
url=serviceurl+urllib.urlencode({'sensor':'false','address':adress})
url
uh=urllib.urlopen(url)
uh
data=uh.read()
data
js=json.loads(str(data))
js
print(json.dumps(js,indent=4))
adress='Strada Corneliu Coposu, GJ'
url=serviceurl+urllib.urlencode({'sensor':'false','address':adress})
URL
url
uh=urllib.urlopen(url)
data=uh.read()
js=json.loads(str(data))
js
print(json.dumps(js,indent=4))
from  twurl  import  augment
from  twurl  import  augment
from  twurl  import  augment
from  twurl  import  augment
url=augemnt('https://api.twitter.com/1.1/statuses/user_timeline.json',
{'screen_name':'drchuck','count':'2'})
url=augment('https://api.twitter.com/1.1/statuses/user_timeline.json',
{'screen_name':'drchuck','count':'2'})
url
connection=urllib.urlopen(url)
url=augment('https://api.twitter.com/1.1/statuses/user_timeline.json',
{'screen_name':'Alexandru_Daia','count':'2'})
connection=urllib.urlopen(url)
import json
%history -f  PythonAPI.py
