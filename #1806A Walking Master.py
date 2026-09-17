#Will need to see this one
import sys
n=int(sys.stdin.readline())
for x in range(n):
    a,b,c,d=map(int,sys.stdin.readline().split())
    if d>=b and a-b>=c-d:
        print((d-b)+((a+d-b)-c))
    else:
        print(-1)
    