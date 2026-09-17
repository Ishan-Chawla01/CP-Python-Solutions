import sys
a=list(map(int,sys.stdin.readline().split()))
a.sort()
#print(a)
if a[1]+a[2]>a[3] or a[0]+a[1]>a[2]:
    print("TRIANGLE")
elif a[0]+a[1]==a[2] or a[1]+a[2]==a[3]:
    print("SEGMENT")
else:
    print("IMPOSSIBLE")