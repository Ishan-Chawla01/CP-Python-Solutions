import sys
n=int(sys.stdin.readline())
for x in range(n):
    length=int(sys.stdin.readline())
    a=list(map(int,sys.stdin.readline().split()))
    print(max(a)-min(a)+1) 