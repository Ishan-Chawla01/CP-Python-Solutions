import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    
    buildings=[[a[i],i] for i in range(len(a))]
    buildings.sort(key=lambda x:x[0], reverse=True)
    ans=0
    ans_coord=[0]*(n+1)
    dist=1
    
    for idx,(visits,ori_idx) in enumerate(buildings):
        coord=dist if idx%2==0 else -dist
        if idx%2!=0:
            dist+=1
        ans+=2*abs(coord)*visits
        ans_coord[ori_idx]=coord

    print(ans)
    print(*ans_coord[::-1])

    '''
    14
0 2 -1 1
78
0 -2 -1 1 2 3
18
0 1 -1 2 -2 3
0
0 1
'''