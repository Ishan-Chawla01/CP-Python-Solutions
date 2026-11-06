import sys
from collections import Counter
input = lambda: sys.stdin.readline().rstrip("\r\n")
 
 
def solve():
    n=int(input())
    s=input()
    c=Counter(s)
    right,left=0,0
    ans=0;summ=0
    right=len(c.keys())
    c1={}
    for char in s:
        c[char]-=1
        if char in c1: c1[char]+=1
        else: c1[char]=1
        if c[char]>0:
            summ=len(c1.keys())+right
        else:
            summ=len(c1.keys())+right-1
            right-=1 # Got this after AI's hint
        ans=max(ans,summ)
    print(ans)
for _ in range(int(input())):
    solve()