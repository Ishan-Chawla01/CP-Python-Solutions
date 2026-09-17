##WTF, the solution doesn't match the editorial at all as far as I can see...
import sys
from collections import Counter
from collections import defaultdict
n=int(sys.stdin.readline())
for x in range(n):
    s,t=map(str, sys.stdin.readline().split())
    s_count=Counter(s)
    t_count=Counter(t)
    ans="YES"
    for a in s:
        if s_count[a]-t_count[a]<0:
            ans="NO"
            break
    if ans=="NO":
        print(ans)
        continue
    idx=0
    res=[]
    '''for char in s:
        if idx<len(t) and char==t[idx]:
            res+=char
            idx+=1
    if idx==len(t):
        ans="YES"
    else:
        ans="NO"
    print(ans)'''
    for char in reversed(s):
        if t_count[char]>0:
            res.append(char)
            t_count[char]-=1
        else:
            continue
    res=reversed(res)
    res="".join(res)
    if res==t:
        ans="YES"
    else:
        ans="NO"
    print(ans)
    