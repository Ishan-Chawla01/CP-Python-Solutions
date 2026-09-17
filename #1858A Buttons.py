# DOne in 2 minutes
import sys
num=int(sys.stdin.readline())
for x in range(num):
    a,b,c=map(int,sys.stdin.readline().split())
    if a>b:
        print("First")
    elif a<b:
        print("Second")
    else:
        if c%2==0:
            print("Second")
        else:
            print("First")