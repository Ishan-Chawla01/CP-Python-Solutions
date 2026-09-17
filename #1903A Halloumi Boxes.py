import sys
num=int(sys.stdin.readline())
for x in range(num):
    n,k=map(int, sys.stdin.readline().split())
    a=list(map(int, sys.stdin.readline().split()))
    if k==1:
        if a!=sorted(a):
            print("NO")
        else:
            print("YES")
    else:
        print("YES")