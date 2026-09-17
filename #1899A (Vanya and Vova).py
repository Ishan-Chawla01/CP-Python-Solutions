#1899A (Vanya and Vova)
import sys
t=int(sys.stdin.readline())
ans=[]
for i in range(t):
    n=int(sys.stdin.readline())
    if (n+1)%3==0 or (n-1)%3==0:
        ans.append("First")
    else:
        ans.append("Second")

for result in ans:
    print(result)