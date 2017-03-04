import  re
data='From alexandru130586@yandex.com Sat Jan 13.05.2017 21:13:13 marian@ domain.com popesci@pymc .ro '
atpos=data.find('@')
print('Sign @ is   found  at position :',atpos)
stop_pos=data.find(' ',atpos)# finds the   undex of first occurennce of sign starting  from some position
print('Stop position  of  host is  at index :',stop_pos)
host=data[atpos+1:stop_pos]
print(host)
###################Method    2  with splitting ################################
words=data.split()
print("words splitted    by   space are :")
print(words)
email=words[1]
print(email)
pieces=email.split('@')

print(pieces)

print(pieces[1])# because split returns  a list

#####################Implementing  with  the REGEX VERSION #####################

domain=re.findall('@([^ ]*)',data)
print(domain)

#this means  :

#1 @ start extracting until  you   find    #  sign

#2 [^ ] match everything except  non  blank  characters (^ means starting with   blank  and [] non blank . Applying  to   that
#negation means  the what is  starting  after @ and is the set of all characters  that are not blank

###########################Spam CONFIDENCE#####################################

hand=open('mbox-short.txt')

numlist=list()
for line in hand :
    line=line.rstrip()
    print("Searching in the following line: ")
    print(line)
    studd=re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line)
    if len(studd)!=1: continue
    num=float(studd[0])
    numlist.append(num)

print('maximum ', max(numlist))

#for  symbols   in regular  expressions to behave like   normally   must be  prefixed with  '\'

x="We just received $10.23 for cookies and 23$ for beer and  $13.5for python"
y=re.findall('\$[0-9.]+',x)
print(y)







