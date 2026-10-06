import sys
from math import gcd
for _ in range(int(input())):
    a,b=map(int,sys.stdin.readline().split())
    if a==b:
        print(f"0 0")
        continue
    a1,b1=a,b
    g=gcd(a,b)
    g1=g
    ops=0
    while g!=abs(a-b) or g!=abs(a1-b1):
        a+=1;b+=1;a1-=1;b1-=1
        g=gcd(a,b)
        g1=gcd(a1,b1)
        if a1==0 and b1!=0:
            g1=max(g1,b)
        ops+=1
    if abs(a1-b1)==g1:
        print(f"{g1} {ops}")
    else:
        print(f"{g} {ops}")
        
    