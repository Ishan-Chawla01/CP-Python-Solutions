import sys
n=int(sys.stdin.readline())
for x in range(n):
    n,a,b=map(int,sys.stdin.readline().split())
    if n==a and a==b :
        print("YES")
        continue
    elif n-a-b>=2:
        print("YES")
    else:
        print("NO")