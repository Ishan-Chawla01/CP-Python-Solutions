import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip("\r\n")


def solve():
    n,c=sys.stdin.readline().strip().split()
    n=int(n)
    s=sys.stdin.readline().strip()
    ans=0
    carr=[idx for idx,char in enumerate(s) if char==c]
    garr=[idx for idx,char in enumerate(s) if char=="g"]
    last_g=-1
    s=s+s
    for i in range((n-1)*2,-1,-1):
        if s[i]=="g":
            last_g=i
        elif s[i]==c:
            ans=max(ans,last_g-i)
    s=s+s
    print(ans)


for _ in range(int(input())):
    solve()
