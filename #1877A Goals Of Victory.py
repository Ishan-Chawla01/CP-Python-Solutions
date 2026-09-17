import sys
n=int(sys.stdin.readline())
for i in range(n):
    num=int(sys.stdin.readline()) # Number of teams
    eff=list(map(int,sys.stdin.readline().split())) # Efficiencies of n-1 teams
    print(sum(eff)*-1) ## Found by pattern observation by myself!!!!!!!