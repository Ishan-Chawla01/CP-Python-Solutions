import sys
for _ in range(int(input())):
    n=int(sys.stdin.readline())
    a=list(map(int,sys.stdin.readline().strip().split()))
    res=[]
    left=0;right=n-1
    while left<=right:
        res.append(a[left]&a[right])
        left+=1
        right-=1
    print(min(res))