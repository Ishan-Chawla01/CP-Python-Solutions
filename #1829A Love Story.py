import sys
n=int(sys.stdin.readline())
for x in range(n):
    s=sys.stdin.readline()
    c="codeforces"
    count=0
    for x in range(10):
        if c[x]!=s[x]:
            count+=1
    print (count)