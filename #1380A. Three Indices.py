import sys

    #After seeing the editorial
import sys
for _ in range(int(input())):
    n=int(sys.stdin.readline())
    p=list(map(int,sys.stdin.readline().strip().split()))
    flag=False
    for i in range(n-2):
        if p[i]<p[i+1] and p[i+1]>p[i+2]:
            print("YES")
            flag=True
            print(f"{i+1} {i+2} {i+3}")
            break
    if not flag:
        print("NO")