#Kinda like DFS
#Lol. Fucked up quite bad by going that

#After seeing the editorial as well as the solution
import sys
for _ in range(int(input())):
    n=(sys.stdin.readline())
    idx1=idx2=0
    pos=["00","25","50","75"]
    arr=[]
    for t in pos:
        sptr=len(n)-1;ans=0
        while sptr>=0 and n[sptr]!=t[1]:
            sptr-=1
            ans+=1
        if sptr>=0:
            sptr-=1
        else:
            continue
        while sptr>=0 and n[sptr]!=t[0]:
            sptr-=1
            ans+=1
        arr.append(ans)
    print(min(arr)-1)

            
        