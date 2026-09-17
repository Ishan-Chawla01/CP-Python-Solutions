import sys
n=int(sys.stdin.readline())
for x in range(n):
    num=int(sys.stdin.readline())
    def fun(a:int)->int:
        if a<10:
            return a
        else:
            return 9+fun(a//10)
    print(fun(num))
        
