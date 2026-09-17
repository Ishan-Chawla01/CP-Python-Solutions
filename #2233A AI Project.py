import sys
import math
num=int(sys.stdin.readline())
for x in range(num):
    n,x,y,z=map(int,sys.stdin.readline().split())
    if (n/(x+y))<((z+n/(10*y+x))): #If project ends before ai model is set up< work ends there.
        print(math.ceil(n/(x+y)))
        continue
    else:
        print(math.ceil(z+max(0,(n-z*x)/(10*y+x))))

    
    