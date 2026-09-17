#After editorial
import sys
t=int(sys.stdin.readline())
ans=[]
for x in range(t):
        n,k,x=map(int,sys.stdin.readline().split())
        min_sum=k*(k+1)//2
        max_sum= (n*(n+1)-(n-k)*(n-k+1))//2
        if x in range(min_sum,max_sum+1):
                ans.append("yes")
        else:
                ans.append("no")
print(*ans)