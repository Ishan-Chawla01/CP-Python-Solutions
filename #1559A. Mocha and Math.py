
#After seeing a solution from an expert
import sys
for _ in range(int(input())):
    n=int(sys.stdin.readline())
    a=list(map(int,sys.stdin.readline().strip().split()))
    res=a[0]
    for num in a:
        res=res & num
    print(res)    