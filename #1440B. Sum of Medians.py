#after seeing a java solution just above me
import sys
import math
for _ in range(int(input())):
    n,k=map(int,sys.stdin.readline().strip().split())
    a=list(map(int,sys.stdin.readline().strip().split()))
    pointer=n*k;summ=0
    while(k>0):
        k-=1
        pointer-=(n//2 +1) #This is another way in whic deifinition of the median can be interpreted
        summ+=a[pointer]
    print(summ)