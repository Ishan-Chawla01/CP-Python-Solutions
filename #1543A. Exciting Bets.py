#after seeing the editorial
#WTF, need to rpove
import sys
from math import gcd
for _ in range(int(input())):
    a,b=map(int,sys.stdin.readline().split())
    if a==b:
        print("0 0")
    else:
        g=abs(a-b)
        moves=min(a%g,g-a%g)
        print(f"{g} {moves}")