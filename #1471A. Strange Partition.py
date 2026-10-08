#So easy!
import sys
import math
for _ in range(int(input())):
    n,x=map(int,sys.stdin.readline().split())
    a=list(map(int,sys.stdin.readline().strip().split()))
    minn=math.ceil(sum(a)/x)
    maxx=0
    for i in a:
        maxx+=math.ceil(i/x)
    print(f"{minn} {maxx}")