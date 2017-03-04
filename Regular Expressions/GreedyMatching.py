import  re
x='From using the : character,From Alexandru :'
y=re.findall('F.+:',x)
#meaning  :
#1 first  character in matching is an  F
#2 THE . and : means  last  character in matching is :
#3THE + means  one ore more characters  between F and :
print(y)
#to   suppres the  greedy matching we add ? to  say  do non  greedy match
yy=re.findall('F.+?:',x)
print(x)
print(yy)
#Observation : greedy   tackes  the longest  sequence
