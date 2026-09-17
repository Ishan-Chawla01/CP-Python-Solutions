import sys
t=int(sys.stdin.readline())
for x in range(t):
    n=int(sys.stdin.readline())
    a=list(map(int,sys.stdin.readline().split()))
    switch=True
    count=0
    for i in range(1,n+1):
        if a[i-1]!=0 and switch==True:
            count+=1
            switch=False
        elif a[i-1]==0:
            switch=True
    if count<2:
        print(count)
    else:
        print(2)