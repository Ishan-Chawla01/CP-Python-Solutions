import sys
t=int(sys.stdin.readline())
for x in range(t):
    n=int(sys.stdin.readline())
    a=list(map(int,sys.stdin.readline().split()))
    if n%2==0:
        print(2)
        print(f"{1} {n}")
        print(f"{1} {n}")
        # print(f"{n-1} {n}")
        # print(f"{n-1} {n}")
    else:
        print(4)
        print(f"{1} {n}")
        print(f"{1} {n-1}")
        print(f"{n-1} {n}")
        print(f"{n-1} {n}")
        

    