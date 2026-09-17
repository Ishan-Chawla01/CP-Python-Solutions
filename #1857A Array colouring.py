#First try done
import sys
x=int(sys.stdin.readline())
for y in range(x):
    n=int(sys.stdin.readline())
    a=list(map(int,sys.stdin.readline().split()))
    summ=sum(a)
    colour=0
    if n<=2 and a[0]%2!=a[1]%2:
        print("NO")
        continue
    elif n<=2 and a[0]%2==a[1]%2:
        print("YES")
        continue
    for i in range(n):
        if (colour+a[i])%2==(summ-a[i])%2:
            colour+=a[i]
            summ-=a[i]
        else:
            continue
    if colour>0:
        print("YES")
    else:
        print("NO")