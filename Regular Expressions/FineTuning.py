#WE  CAN REFINE   re.findall() and  to  determine  what portion
#of  match  is to be extracted  by using  parentheses
import  re
text='From stephen.marquard@uct.az.za Sat Jan 04:02:2018'
y=re.findall('\S+@\S+', text)
#print(y)
#S means non   white space  and  + at least one  non white space
#means get text  that  has  at  list 1 nonspace or  more
#contains @ and after that   at leat  one  not white space
#Example  with   greedy  and non  greedy

text='The daia.alexandru@yahoo.com  bla bla From marian@yandex.com hahaha'
#y=re.findall('\S+@\S+',text)
#print('Greedy  evaluation  -gets  longest  sequence')
print(text)
#print(y)
#parantheses  they contain the match   for  the string
y=re.findall('(The|From) (\S+@\S+)',text)
print(y)



