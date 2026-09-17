import sys
n=int(sys.stdin.readline())
ans=[]
for x in range(n):
    num=int(sys.stdin.readline())
    a=list(map(int,sys.stdin.readline().split()))
    summ=sum(a)
    pro=1
    count=0
    for i in range(num):
        pro*=a[i]
       
    i=0
    while summ<0 or pro<1 and i<num:
        if a[i]==-1:
            a[i]=1
            count+=1
            summ+=2
            #print(f"sum is:{summ}")
            pro*=(-1)
            #print(f"pro is:{pro}")
        i+=1
    ans.append(count)
print(*ans)