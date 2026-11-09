import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip("\r\n")


def solve():
    n,c=sys.stdin.readline().strip().split()
    n=int(n)
    s=sys.stdin.readline().strip()
    ans=0
    carr=[idx for idx,char in enumerate(s) if char==c]
    s=s+s
    for idx in carr:
        start=idx;str=idx;end=(n-1)*2;e=(n-1)*2;mid=(start+end)//2;m=(start+end)//2
        while start<end:
            if s[mid]!="g":
                start=mid+1
            else:
                break
        if s[mid]=="g":
            ans=max(ans,mid-idx)
        while str<e:
            if s[m]!="g":
                e=m-1
            else:
                break
        if s[m]=="g":
            ans=max(ans,m-idx)
        
    print(ans)


for _ in range(int(input())):
    solve()
