file=open('mbox-short.txt')
import  re
#method 1 -  where   we search   all occurences
#no_occurence1=0
#for line in file :
#    line=line.rstrip()
#    if  re.search('From:',line):
#        print(line)
#        no_occurence1+=1
#method 2 -  where we introudce  special character ^ meaning at  begining
no_occurence2=0
for  line in file :
    line=line.rstrip()
    if re.search('^From:',line):
        print(line)
        no_occurence2+=1

#print("first method  brings   a number of   occurences =" ,no_occurence1)
print("second  method brings a number of occurences =",no_occurence2)



