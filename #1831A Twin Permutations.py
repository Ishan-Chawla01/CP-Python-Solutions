import sys
n=int(sys.stdin.readline())
def maximum(l:list)->int:
    index=a[0]
    for i in range(len(a)):
        if a[i]>index:
            index=a[i]
    return index
for x in range(n):
    length=int(sys.stdin.readline())
    a=list(map(int,sys.stdin.readline().split()))
    c=sorted(a)
    b=[0]*length
    ##Finding max in a
    
    for j in range(length):
        index_1=a.index(maximum(a))
        b[index_1]=c[j]
        a[index_1]=-99999999999

    ##################
    print(*b)

