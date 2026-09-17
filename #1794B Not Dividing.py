import sys
def solve():
    t=int(sys.stdin.readline())
    for x in range(t):
        n=int(sys.stdin.readline())
        a=list(map(int,sys.stdin.readline().split()))
        for i in range(n):
            if a[i]==1:
                a[i]+=1
        for i in range(n-1):
            if a[i+1]%a[i]==0:
                a[i+1]+=1
        print(*a)
solve()