#Was close, but couldn't think of from where the comment starts
import sys
from collections import Counter
for _ in range(int(input())):
    n=int(sys.stdin.readline())
    a=list(map(int,sys.stdin.readline().split()))
    sums=[]
    ans=0
    for x in range(n-4):
        sums.append(a[x]+a[x+2]-a[x+4])
    d=Counter(sums)
    for maxx in d.values():
        ans+=maxx*(maxx-1)//2
    ##This is the additional pair remmoval logic, simple, but yikes...
    for start, love in enumerate(sums):
        if start+2<len(sums) and sums[start+2]==love:
            ans-= 1
        if start+4 <len(sums) and sums[start+4]==love:
            ans-= 1
    print(ans)