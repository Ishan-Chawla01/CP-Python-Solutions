import sys
from collections import Counter
t=int(sys.stdin.readline())
ans=[]
for x in range(t):
    n,k=map(int,sys.stdin.readline().split())
    s=sys.stdin.readline().strip()
    if n==1: 
        ans.append("YES")
        continue
    d=Counter(s)
    count=0
    for i in d:
        if d[i]%2!=0:
            count+=1
    if count-k>1:
        ans.append("NO")
        
    else:
        ans.append("YES")
print(*ans)