import sys
t=int(sys.stdin.readline())
for x in range(t):
    a,b=map(int,sys.stdin.readline().split())
    count=0
    if a==b:
        print(0)
        continue
    if b>a:
        a,b=b,a
    while a>b:
        if a/2==float(b) or a/4==float(b) or a/8==float(b):
            count+=1
            a=b
            break
        else:
            count+=1
            if a%8==0:
                a//=8
                continue
            if a%4==0:
                a//=4
                continue
            if a%2==0:
                a//=2
            else:
                break
            

    if a!=b:
        print(-1)
        #print(f"a:{a} b:{b}")
    else:
        print(count)
