#1881A - Don't try to count
# Think, why can't it be greater than 5??
import sys
num=int(sys.stdin.readline()) # Number of test cases
for i in range(num):
    n,m=map(int,sys.stdin.readline().split())# n= number of letters in x, m= number of letters in s
    x=sys.stdin.readline().strip() # String x
    s=sys.stdin.readline().strip() # String s
    for i in range(6):
        if s in x:
            print(i)
            break
        x+=x
    if s not in x:
        print(-1)
        
""" # GOT A TLE here
count=0
if s in x:  
    print(0)
    continue
for j in range(0,m//n+1):
    x+=x
    count+=1
    if s in x:
        print(count)
        break
else:
    print(-1)"""
