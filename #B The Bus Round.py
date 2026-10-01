import sys
for x in range(int(input())):
    a,b,m=map(int,sys.stdin.readline().split())
    if m>=b:
        summ=(m-1)*m//2
        x=b%m
        summ+=x*(x+1)//2
        print(summ)
    else:
        summ=(b*b+1)//2
        print(summ)