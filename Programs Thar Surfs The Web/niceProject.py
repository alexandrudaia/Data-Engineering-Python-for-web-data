for i in  range(4):
    html=urllib.urlopen(url).read()
    soup=BeautifulSoup(html)
    tags=soup('a')
    tag3=tags[2]
    print(tag3.text)
    url=str(ta
    g3.get('href',None))
    print(url)
url='http://python-data.dr-chuck.net/known_by_Jodi.html'
import urllib2
from bs4 import BeautifulSoup

url='http://python-data.dr-chuck.net/known_by_Jodi.html'

count = int(raw_input("Enter count: "))
position = int(raw_input("Enter position: "))

names = []

while count > 0:
    print "retrieving: {0}".format(url)
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)
    anchors = soup('a')
    name = anchors[position-1].string
    names.append(name)
    url = anchors[position-1]['href']
    count -= 1


print names[-1]
import urllib2
from bs4 import BeautifulSoup

url=http://python-data.dr-chuck.net/known_by_Fikret.html

count = int(raw_input("Enter count: "))
position = int(raw_input("Enter position: "))

names = []

while count > 0:
    print "retrieving: {0}".format(url)
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)
    anchors = soup('a')
    name = anchors[position-1].string
    names.append(name)
    url = anchors[position-1]['href']
    count -= 1


print names[-1]
import urllib2
from bs4 import BeautifulSoup

url='http://python-data.dr-chuck.net/known_by_Fikret.html'

count = int(raw_input("Enter count: "))
position = int(raw_input("Enter position: "))

names = []

while count > 0:
    print "retrieving: {0}".format(url)
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)
    anchors = soup('a')
    name = anchors[position-1].string
    names.append(name)
    url = anchors[position-1]['href']
    count -= 1


print names[-1]
url='http://python-data.dr-chuck.net/known_by_Fikret.html'
for i in range(4):
    html=urllib.urlopen(url).read()
    soup=BeautifulSoup(html)
    tags=soup('a')
    tag3=tags[2]
    url=str(tag3.get('href',None))
    print(url)
    print(tag3.text)
import urllib
for i in range(4):
    html=urllib.urlopen(url).read()
    soup=BeautifulSoup(html)
    tags=soup('a')
    tag3=tags[2]
    url=str(tag3.get('href',None))
    print(url)
    print(tag3.text)
url='http://python-data.dr-chuck.net/known_by_Fikret.html'
for i in range(7):
    html=urllib.urlopen(url).read()
    soup=BeautifulSoup(html)
    tags=soup('a')
    tag3=tags[17]
    url=str(tag3.get('href',None))
    print(url)
    print(tag3.text)
url='http://python-data.dr-chuck.net/known_by_Rowan.html'
for i in range(7):
    html=urllib.urlopen(url).read()
    soup=BeautifulSoup(html)
    tags=soup('a')
    tag3=tags[17]
    url=str(tag3.get('href',None))
    print(url)
    print(tag3.text)
url='http://python-data.dr-chuck.net/known_by_Rowan.html'
%history project2.py
%history -f  niceProject.py
