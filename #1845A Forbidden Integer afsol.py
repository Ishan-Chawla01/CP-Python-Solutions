import sys
n=int(sys.stdin.readline())
for x in range(n):
    n,k,x=map(int, sys.stdin.readline().split())
    ans=[]
    if x!=1:
        print("YES")
        for x in range(n):
            ans.append(1)
        print(len(ans))
        print(*ans)
        continue
    elif k==1:
        print("NO")
        continue
    elif k==2 and n%2==0:
        print("YES")
        for x in range(n//2):
            ans.append(2)
        print(len(ans))
        print(*ans)
        continue
    elif k==2 and n%2!=0:
        print("NO")
        continue
    else:
        print("YES")
        if n%2==0:
            ans.append(2)
        else:
            ans.append(3)
        while(sum(ans)!=n):
            ans.append(2)
    print(len(ans))
    print(*ans)