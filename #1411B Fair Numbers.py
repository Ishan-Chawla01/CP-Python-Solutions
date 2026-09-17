#NO AI, INITIAL APPROACH WAS WRONG< BUT THIS APPROACH STRUCK TO ME BEFORE SUBMISSION
import sys
t=int(sys.stdin.readline())

for i in range(t):
    n=int(sys.stdin.readline())
    a=[2,3,4,5,6,7,8,9]
    i=0
    while i<len(a):
        if str(a[i]) not in str(n):
            i+=1
        else:
            if n%a[i]==0:
                i+=1
                continue
            else:
                n+=1
                i=0
    print(n)