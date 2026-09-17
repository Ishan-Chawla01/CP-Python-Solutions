##Did they just accept a square polynomial time solution?!?! CRAZYYY!
import sys
t=int(sys.stdin.readline())
ans=[]
for x in range(t):
    n=int(sys.stdin.readline())
    a=list(map(int,sys.stdin.readline().split()))
    flag=False
    
    for x in range(0,2**8):
        b=[]
        for i in range(0,n):
            b.append(a[i]^x)
        
        ini=b[0]
        for i in range(1,n):
            ini=ini^b[i]
        if ini==0:
            flag=True
            ans.append(x)
            break
    if not flag:
        ans.append(-1)
print(*ans)
