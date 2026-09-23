import sys
ans=[]
for x in range(int(input())):
    x0,n=map(int,sys.stdin.readline().split())
    #If starting position is even, it moves to start-n//2 steps after n number of jumps where n is even
    # If starting position is odd, it moves to start+n//2 steps after n numer of jumps where n is even
    n_ini=n
    Is_odd=False
    if n%2!=0:
        Is_odd=True
        n-=1
    if x0%2==0:
        x0=x0-(n//2)
    else:
        x0=x0+(n//2)
    if Is_odd:
        if abs(x0)%2==0:
            x0=x0-n_ini
        else:
            x0=x0+n_ini
    ans.append(x0)
print(ans)