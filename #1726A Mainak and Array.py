#After seeing editorial, was jsut one step away from solution
import sys
def solve():
    t=int(sys.stdin.readline())
    for x in range(t):
        n=int(sys.stdin.readline())-1
        a=list(map(int,sys.stdin.readline().split()))
        '''maxx=max(abs(a[n]-a[0]),abs(a[n]-min(a)),abs(max(a)-a[0]))
        for i in range(n): #The check that I had missed
            if abs(a[i+1]-a[i])>maxx:
                maxx=abs(a[i+1]-a[i])
        print(maxx)'''
        ##Was quite far away from the solution
        maxx1=a[n]-min(a)
        maxx2=max(a)-a[0]
        '''for x in range(1,n+1):
            maxx2=max(maxx2,a[x]-a[x-1])'''
        maxx3=0
        '''for i in range(0,n):
            maxx3=max(maxx3,a[n]-a[i])
        maxx4=0
        for i in range(1,n+1):
            maxx4=max(maxx4,a[i]-a[0])'''
        for i in range(n+1):
            maxx3=max(maxx1,maxx2,a[i-1]-a[i])
        print(maxx3)
solve()