import sys
t=int(sys.stdin.readline())
for x in range(t):
    x,y,k=map(int,sys.stdin.readline().split())
    #x= Number of sticks you can buy using 1, y=number of sticks for one coal, k= number of torches
    #Wrong formula print( (k*(y+x)-1)//(x-1) )
    print((k*(y+1)-1+x-2)//(x-1)+k)