## BY SELF< NO AI AT ALL!
import sys
t=int(sys.stdin.readline())
for x in range(t):
    n=int(sys.stdin.readline())
    m=[]
    a=[]
    summ=0
    for i in range(n):
        m.append(int(sys.stdin.readline()))
        a.append(sorted(list(map(int,sys.stdin.readline().split()))))
    if len(a)==1:
        print(min(a[0]))
        continue
    #Take max a[1] and shift a[0] of that array into array with minimum a[1].
    mina_ind=0
    maxa_ind=0
    for i in range(n):
        if a[mina_ind][1]>a[i][1]:
            mina_ind=i
    for i in range(n):
        if i!=mina_ind:
            temp=a[i].pop(0)
            a[mina_ind].append(temp)
    a[mina_ind]=sorted(a[mina_ind])
    for i in range(n):
        summ+=a[i][0]
    print(summ)
    