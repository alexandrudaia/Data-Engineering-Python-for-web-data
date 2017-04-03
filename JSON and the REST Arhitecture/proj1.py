import  urllib
import json
url='http://python-data.dr-chuck.net/comments_223368.json'
data=urllib.urlopen(url).read()
data
js=jsoan.load(str(data))
js=json.load(str(data))
js=json.loads(str(data))
js
for item in js :
    print item['count']
for item in js['comments'] :
    print item['count']
sum=0
for item in js['comments'] :
    print item['count']
    sum+=int(item['count'])
sum
$history -f proj1.py
%history -f proj1.py
