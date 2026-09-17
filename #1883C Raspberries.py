import sys
t=int(sys.stdin.readline())
ans=[]
for x in range(t):
    n,k=map(int,sys.stdin.readline().split())
    a=list(map(int,sys.stdin.readline().split()))
    evens=0
    for i in range(n):
        if a[i]%2==0:
            evens+=1
        a[i]=(k-a[i]%k)%k
    ops_for_two_evens=99999999
    if k == 4:
            if evens >= 2:
                ops_for_two_evens = 0
            elif evens == 1:
                ops_for_two_evens = 1
            else:
                ops_for_two_evens = 2
    minn=min(a)
    ans.append(min(minn,ops_for_two_evens))
print(*ans)