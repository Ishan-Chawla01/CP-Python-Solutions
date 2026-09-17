'''import sys
t=int(sys.stdin.readline())
for x in range(t):
    n,rounds=map(int,sys.stdin.readline().split())
    n*=2
    s=list(sys.stdin.readline().strip())
    while rounds>0:
        for i in range(0,n):
            if i==n-1:
                if s[i]=='1' and s[0]=='0':
                    s[i]='0'
                    s[0]='1'
                continue
            if s[i]=='1' and s[i+1]!='1':
                s[i]='0'
                s[i+1]='1'
        rounds-=1
    even_score=0
    odd_score=0
    for i in range(n):
        if (i+1)%2!=0 and s[i]=='1':
            even_score+=1
        elif (i+1)%2==0 and s[i]=='1':
            odd_score+=1
    print(f"{odd_score} {even_score}")
            '''
import sys
t=int(sys.stdin.readline())
for x in range(t):
    n,rounds=map(int,sys.stdin.readline().split())
    n*=2
    s=list(sys.stdin.readline().strip())
    for i in range(n):
        if i==n-1:
            if s[i]=='1' and s[0] !='1':
                s[i],s[0]=s[0],s[i]
            continue
        if s[i]!=s[i+1]:
            s[i],s[i+1]=s[i+1],s[i]
    red_teams=0 #add to it if odd index is 1
    blue_teams=0 # add to it if even index is 1
    for i in range(n):
        if i%2!=0 and s[i]=='1':
            red_teams+=1
        elif i%2==0 and s[i]=='1':
            blue_teams+=1
    print(f"{red_teams} {blue_teams}")
