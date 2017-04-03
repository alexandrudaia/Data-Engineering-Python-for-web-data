import xml
import xml.etree.ElementTree as ET
data='''
<person>
  <name>Alex</name>
  <phone type="intl">
     0768609734
  </phone>
  <email hide="yes"/>
</person>'''
tree=ET.fromstring(data)
tree
tree.find('name')
tree.find('name').text
tree.find('email').text
tree.find('email').get('hide')
input='''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Alex</name>
        </user>
        <user x="7">
             <id>009</id>
             <name>ion</name>
        </user>
    </users>
</stuff>'''
stuff=ET.fromstring(input)
stuff
lst=stuff.findall('users/user')
lst
len(lst)
for elem in list:
    print elem
for elem in lst:
    print elem
for elem in lst:
    print elem.name
lst[1]
lst[1].text
lst[1].find('name')
lst[1].find('name').text
lst[1].find('name').get("x")
lst[1]..get("x")
lst[1].get("x")
for  elem  in lst:
    print(elem.find('name').text)
for  elem  in lst:
    if elem.get("x")=='7':
        print(elem.find('name').text)
%save ParsingXML.py
%history  ParsingXML.py
%history -f  ParsingXML.py
