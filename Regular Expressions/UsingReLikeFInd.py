hand=open('mbox-short.txt')
for line in  hand:
    line=line.strip()
    if line.find('From:')>=0:
        print(line)
