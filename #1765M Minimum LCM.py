import sys
import math
t=int(sys.stdin.readline())
for x in range(t):
    n=int(sys.stdin.readline())
    '''low=1
    high=n-1
    lcm=n-1
    fin_l=1
    fin_h=n-1
    while low<high:
        low+=1
        high-=1
        a=math.lcm(low,high)
        if a<lcm:
            lcm=a
            fin_l=low
            fin_h=high
    print(f"{fin_l} {fin_h}")''' #Too brute force
    smallest_prime=n
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            smallest_prime=i    
            break
    a=n//smallest_prime
    b=n-a
    print(f"{a} {b}")
    