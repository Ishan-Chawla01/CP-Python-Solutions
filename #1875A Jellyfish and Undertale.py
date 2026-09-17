import sys
t=int(sys.stdin.readline())
ans=[]
for x in range(t):
    a,b,n=map(int,sys.stdin.readline().split())
    tools=list(map(int,sys.stdin.readline().split()))
    time=0
    i=0
    #Very inefficeint and has time complexity O(a*n) as loop relies on decrementing value of b one by one which can be as large as 10**9
    '''while b>0:
        if i<len(tools) and b==1:
            b=min(b+tools[i],a)
            i+=1
        b-=1
        time+=1
    ans.append(time)'''  
    #O(n) solution This loop instead relies on n which can be <=100 only so time decreases from 10**9 operations to 100 operations per loop
    time=b
    for i in tools:
        time+=min(i,a-1)
    ans.append(time)
print(*ans)