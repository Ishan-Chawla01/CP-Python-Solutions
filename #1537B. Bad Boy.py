###DONe, 1st attempt at home! No AI at all! Only pen, paper, patterns and meeee!!!
import sys
for _ in range(int(input())):
    n,m,i,j=map(int,sys.stdin.readline().strip().split())
    edges=[(1,1),(n,1),(n,m),(1,m)]
    e1,e2=None,None
    if n-i>i:
        e1=edges[1]
    else:
        e1=edges[0]
    if m-j>j:
        e2=edges[2]
    else:
        e2=edges[3]
    if  (e1[0]-i,e1[1],j)>(e2[0]-i,e2[1],j):
        maxx=e1
    else:
        maxx=e2
    corr=(float('inf'),float('inf'))
    if maxx==edges[0]: corr=edges[2]
    elif maxx==edges[2]: corr=edges[0]
    elif maxx==edges[1]: corr=edges[3]
    elif maxx==edges[3]: corr=edges[1]
    print(f"{maxx[0]} {maxx[1]} {corr[0]} {corr[1]}")