import sys
n=int(sys.stdin.readline())
for x in range(n):
    n,k=map(int,sys.stdin.readline().split())
    if n%2==0:
        print("YES")
    else:
        if k%2==0:
            print("NO")
        else:
            print("YES")
#DId 3 problems under 20 minutess
