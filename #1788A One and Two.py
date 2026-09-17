import sys
num=int(sys.stdin.readline())
for x in range(num):
    n=int(sys.stdin.readline())
    a=list(map(int,sys.stdin.readline().split()))
    
    new=1
    old=1
    flag=False
    for i in range(n):
        if a[i]==2:
            old*=2
    for i in range(n):
        if a[i]==2:
            new*=2
            old//=2
        if new==old:
            print(i+1)
            flag=True
            break
    if flag==False:
        print(-1)
        
