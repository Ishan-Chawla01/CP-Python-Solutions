import sys
from collections import defaultdict
for _ in range(int(input())):
    n,k=map(int,sys.stdin.readline().strip().split())
    a=list(map(int,sys.stdin.readline().strip().split()))
    d=defaultdict(int) # DIct for counting number of occurances
    count=0 #For seeing how many odd values are there
    odds=[] #Which keys are having odd frequencies par say... They need to be matched amongst one another
    ans=0
    for key in a:
        d[key]+=1
    for key,value in d.items():
        if value%2!=0:
            count+=1
            odds.append(key)
    
    if count>1:
        ops=float('inf')
        minn=-1
        for i in range(0,len(odds)):
            for j in range(i+1,len(odds)):
                if abs(odds[i]-odds[j])%k==0:
                    ops1=ops
                    ops=min(ops,abs(odds[i]-odds[j])//k)
                    if ops1>ops:
                        minn=j
                        count-=2
            d[min(odds[i],odds[minn])]-=1
            d[max(odds[i],odds[minn])]+=1
            if ops==float('inf'):continue
            ans+=ops
            ops=float('inf')
            if count==1:
                break
    if count>1:
        print(-1)
    else:
        print(ans)
        