#EASY Got TLE lol
#Had to use Ai, VIPS
import sys
t=int(sys.stdin.readline())
for x in range(t):
    n,k=map(int,sys.stdin.readline().split())
    a=list(map(int,sys.stdin.readline().split()))
    ans=[]
    for i in range(n):
        if a[i]%k!=0:
            a[i]=a[i]%k
        else:
            a[i]=k
    ind=[(a[i],i+1) for i in range(n)]
    #ind=sorted(ind, reverse=True)# Causes problesm due to reverse=True
    ind=sorted(ind, key=lambda x:(-x[0],x[1]))
    #print(ind)
    ans= [index[1] for index in ind ]
    print(*ans)
