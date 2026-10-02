import math
import sys
for x in range(int(input())):
    n=int(sys.stdin.readline())
    a=list(map(int,sys.stdin.readline().split()))
    maxx=[-1,float('-inf')]
    minn=[-1,float('inf')]
    for i in range(len(a)):
        if a[i]>maxx[1]:
            maxx=[i,a[i]]
        if a[i]<minn[1]:
            minn=[i,a[i]]
    while maxx[1]<minn[1]:
        minn[1]+=max(a[minn[0]],a[minn[0]+1],a[minn[0]-1])
    dif=abs(minn[1]-maxx[1])
    dif=min(dif,abs(minn[1]-max(a[minn[0]],a[minn[0]+1],a[minn[0]-1])-maxx[1]))
    minn[1]=minn[1]-max(a[minn[0]],a[minn[0]+1],a[minn[0]-1])
    dif=min(dif,maxx[1]-minn[1]+a[minn[0]+1],maxx[1]-minn[1]+a[minn[0]-1])
    print(dif)
        
    