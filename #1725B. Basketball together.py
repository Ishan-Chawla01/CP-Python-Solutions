#By self, easy for 1000 rated
import sys


def solve():
    n,d=map(int,sys.stdin.readline().strip().split())
    arr=list(map(int,sys.stdin.readline().strip().split()))
    arr.sort()
    left,right=0,n-1;wins=0;temp=0
    while left<=right:
        #Patchwork for case 10
        if arr[right]>d:
            right-=1
            wins+=1
            continue
        ## Ptch over
        temp+=arr[right]
        while temp<=d:
            temp+=arr[right]
            left+=1
        if left<=right:
            wins+=1
        temp=0
        right-=1
    print(wins)

solve()
