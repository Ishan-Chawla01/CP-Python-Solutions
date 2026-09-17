#DIV 4C problem lol
import sys
t=int(sys.stdin.readline())
ans=[]
for x in range(t):
    n=int(sys.stdin.readline())
    s=sys.stdin.readline().strip()
    j=n
    for i in range(0,n//2):
        if s[i]!=s[n-i-1] and len(s)!=1:
            j-=2
        elif s[i]==s[n-i-1]:
            break
    ans.append(j)
print(*ans)