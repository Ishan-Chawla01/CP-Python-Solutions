import sys
n=int(sys.stdin.readline())
for x in range(n):
    length=int(sys.stdin.readline())
    a=sys.stdin.readline()
    m=int(sys.stdin.readline())
    b=sys.stdin.readline()
    c=sys.stdin.readline()
    for i in range(m):
        if c[i]=='V':
            a=str(b[i])+a
        else:
            a=a.strip()+str(b[i])
    print(a)
