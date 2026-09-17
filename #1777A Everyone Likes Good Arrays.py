import sys
t=int(sys.stdin.readline())
for x in range(t):
    n=int(sys.stdin.readline())
    a=list(map(int,sys.stdin.readline().split()))
    count=0
    i=0
    while i<len(a)-1:
        if a[i]%2==a[i+1]%2:
            a1=a.pop(i)
            b1=a.pop(i)
            a.insert(i,a1*b1)
            count+=1
            continue
        i+=1
    print(count)