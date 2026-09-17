import sys

# 1. Add the cache decorator

t=int(sys.stdin.readline())
ans=[]
for x in range(t):
    n=int(sys.stdin.readline())
    a=list(map(int,sys.stdin.readline().split()))
    b=list(map(int,sys.stdin.readline().split()))
    '''if n==1:
        if a[0]==b[0]:print(2)
        else:print(1)
        continue
    a1,b1={},{}
    for i in range(n-1):
        if a[i]==a[i+1]:
            if a[i] in a1:
                a1[a[i]][1]+=1
            elif a[i] not in a1: 
                a1[a[i]]=[1,1]
        else:
            if a[i] in a1 and a1[a[i]][1]>a1[a[i]][0]:
                a1[a[i]][0]=a1[a[i]][1]
            if a[i] in a1:
                a1[a[i]][1]=1
        if b[i]==b[i+1]:
            if b[i] in b1:
                b1[b[i]][1]+=1
            elif b[i] not in b1:
                b1[b[i]]=[1,1]
        else:
            if b[i] in b1 and b1[b[i]][1]>b1[b[i]][0]:
                b1[b[i]][0]=b1[b[i]][1]
            if b[i] in b1:
                b1[b[i]][1]=1
        if b[i] in b1 and b1[b[i]][1]>b1[b[i]][0]:
                b1[b[i]][0]=b1[b[i]][1]
        if a[i] in a1 and a1[a[i]][1]>a1[a[i]][0]:
                a1[a[i]][0]=a1[a[i]][1]
    if a1=={} and b1=={}:
        print(1)
    else:
        print(sum(max(a1.values() and b1.values())))'''
    
    def max_a(x:int,a:list)->int:
        count=0
        maxx=0
        for i in range(len(a)):
            if a[i]==x:
                count+=1
            else:
                count=0
            if count>maxx:
                maxx=count
        return maxx
    maxx=0
    for i in range(n):
        m=max_a(a[i],a)+max_a(a[i],b)
        m1=max_a(b[i],a)+max_a(b[i],b)
        if max(m,m1)>maxx:
            maxx=max(m,m1)
    ans.append(maxx)
print(*ans)