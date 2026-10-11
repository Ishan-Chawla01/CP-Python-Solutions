import sys
import statistics
for _ in range(int(input())):
    n,k=map(int,sys.stdin.readline().strip().split())
    a=list(map(int,sys.stdin.readline().strip().split()))
    #A special patchwork for when size of array is 2:
    summ=0
    if n==2:
        i=0
        while i<(n*k):
            summ+=a[i]
            i+=2
        print(summ)
        continue
    left=0;right=len(a)-1;length=(n-1)//2;summ=0
    i=k
    while i<right+1:
        
        summ+=a[i]
        i=i+(n-1)
    print(summ)