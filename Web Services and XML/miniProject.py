import  urllib
import  BeautifulSoup
from  BeautifulSoup import *
url='http://python-data.dr-chuck.net/comments_223364.xml'
dat=urllib.urlopen(url)
dat
data=dat.read()
data
tree=ET.fromstring(data)
import  xml.etree.ElementTree as ET
tree=ET.fromstring(data)
tree
lst=data.findall('commentinfo/comments/comment')
lst=tree.findall('commentinfo/comments/comment')
len(lst)
lst=tree.findall('commentinfo/comments')
len(lst)
lst=tree.findall('comment')
len(lst)
tree
data
tree=ET.fromstring(data)
lst=tree.findall('commentinfo')
len(lst)
lst=tree.findall('commentinfo')
len(lst)
lst=tree.findall('commentinfo/comments')
len(lst)
#not   working   trying now with  XPath selector
counts=tree.findall('.//count')
len(counts)
counts[0].text
sum=0
for   c in counts :
    sum+=int(c.text)
sum
%history miniProject.py
%history -f miniProject.py
