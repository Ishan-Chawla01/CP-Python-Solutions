#Incorrect solution earlier, cause it's a 4 step process not 2 step, and also, the jumps do not alternate
import sys
ans=[]
for x in range(int(input())):
    x0,n=map(int,sys.stdin.readline().split())
    #If starting position is even, it moves to start-n//2 steps after n number of jumps where n is even
    # If starting position is odd, it moves to start+n//2 steps after n number of jumps where n is even
    n0=0
    if n%4==0:
        n0=0
    elif n%4==1:
        n0=-n
    elif n%4==2:
        n0=1
    else:
        n0=n+1

    if x0%2==0:
        ans.append(x0+n0)
    else:
        ans.append(x0-n0)
print(*ans)