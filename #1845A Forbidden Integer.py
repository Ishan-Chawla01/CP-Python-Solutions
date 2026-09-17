import sys
num=int(sys.stdin.readline())
for x in range(num):
    ans=[]
    n,k,x=map(int, sys.stdin.readline().split())
    if x!=1:
        print("YES")
        for x in range(n):
            ans.append(1)
        print(len(ans))
        print(*ans)
    elif n%k!=x and n%k<=k and k!=x:
        print("YES")
        while(sum(ans)!=n-n%k):
            ans.append(k)
        if(n%k!=0):
            ans.append(n%k)
        print(len(ans))
        print(*ans)
    elif n%k-1!=x and n%k<=k-1 and k!=1 and k==x: #k==x is giving the problem
        print("YES")
        while(sum(ans)!=n-n%(k-1)):
            ans.append(k)
        if(n%(k-1)!=0):
            ans.append(n%(k-1))
        print(len(ans))
        print(*ans)
    else:
        print("NO")
