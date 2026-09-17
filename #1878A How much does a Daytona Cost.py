'''import sys
num=int(sys.stdin.readline())
for x in range(num):
    n,k=map(int,sys.stdin.readline().split())
    a=list(map(int,sys.stdin.readline().split()))
    ans=0
    for i in range(n):
        count=0
        for j in range(i,n):
            if a[j]==k:
                count+=1
            else:
                count-=1
            if count>0:
                ans+=1
    print(ans)'''

################
'''import collections
from collections import Counter
import sys
num=int(sys.stdin.readline())
for x in range(num):
    n,k=map(int,sys.stdin.readline().split())
    a=list(map(int,sys.stdin.readline().split()))
    cnt=Counter(a)
    if k==max(cnt):
        print("YES")
        
    else:
        print("NO")
        print(f"Max cnt is{max(cnt)}")'''
###################
import sys
num=int(sys.stdin.readline())
for x in range(num):
    n,k=map(int,sys.stdin.readline().split())
    a=list(map(int,sys.stdin.readline().split()))
    if k in a:
        print("YES")
    else:
        print("NO")