import sys
n=int(sys.stdin.readline())
for x in range(n):
    length=int(sys.stdin.readline())
    a=list(map(int, sys.stdin.readline().split()))
    if a!=sorted(a):
        print(0)
        continue

    mindif=float('inf')
    index=0
    for i in range(length-1):
        if abs(a[i]-a[i+1])<mindif:
            mindif=abs(a[i]-a[i+1])
    if mindif==0:
        print(1)
        
    else:
        print(mindif//2+1)
