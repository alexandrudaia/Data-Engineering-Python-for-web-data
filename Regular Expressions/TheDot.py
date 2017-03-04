# THe  dot   Is from  Whild -Card  Characters
# Example  ^X:=MATCH THE  START OF  THE LINE
#          ^X.:=THE DOT MEANS  ,MACH  ANY CHARACTER
#          ^X.*:=MEANS  MANY TIMES
#PUTTING  ALL TOGHETER :
# ^X.* MEANS :
#Interested of text  where  at the  begining of line starts with X
# followed  by any character  as many times  it occurs
# if  we put  ^X.*: means  it  must end  with :
#example
import   re
file=open('mbox-short.txt')
for line  in file.read() :
    line=line.rstrip()
    print(re.findall('^X.*',line))
x="My  2  favorite numbers  are   13  and 12"
oneDigit=re.findall('[0-9]',x)
print(oneDigit)
allDigits=re.findall('[0-9]+',x)
print(allDigits)




