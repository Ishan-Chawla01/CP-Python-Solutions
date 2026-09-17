import sys
t=int(sys.stdin.readline())
ans=[]
for x in range(t):
    n,k=map(int,sys.stdin.readline().split())
    a=sorted(list(map(int,sys.stdin.readline().split())))
    if n<=1:
        ans.append(0)
        continue
    #Finding the longest subarray which matches condition
    maxx=0
    count=1
    for right in range(1,n):
        if a[right]-a[right-1]>k:
            maxx=max(maxx,count)
            count=1
        else:
            count+=1
    maxx=max(maxx,count)
    ans.append(n-maxx)
print(*ans)
        