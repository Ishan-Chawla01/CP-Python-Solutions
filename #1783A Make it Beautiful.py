import sys
n=int(sys.stdin.readline())
for x in range(n):
    length=int(sys.stdin.readline())
    a=list(map(int,sys.stdin.readline().split()))
    a=sorted(a)
    if(length==2 and a[0]==a[1]):
        print("NO")
        continue
    if(a[0]==a[length-1]):
        print("NO")
        continue
    else:
        a[0],a[length-1]=a[length-1],a[0]
        print("YES")
        if a[0]==a[1]:
            i=1
            index=-1
            while a[i]==a[1] and i<length:
                i+=1
            index=i
            a[1],a[index]=a[index],a[1]
        print(*a)
    