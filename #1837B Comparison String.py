#Very easy
import sys
t=int(sys.stdin.readline())
for x in range(t):
    n=int(sys.stdin.readline())
    s=sys.stdin.readline()
    maxx=1
    length=1
    if '>' not in s:
        print(len(s))
        continue
    elif '<' not in s:
        print(len(s))
        continue
    for i in range(0,len(s)-1):
        
        if s[i]==s[i+1]:
            length+=1
        else:
            length=1
        if length>maxx:
            maxx=length
    
    print(maxx+1)
        