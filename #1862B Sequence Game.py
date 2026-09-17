import sys
num=int(sys.stdin.readline()) # Number of test cases
for x in range(num):
    n=int(sys.stdin.readline()) # Length of sequence b
    b=list(map(int,sys.stdin.readline().split())) # The sequence b
    m=0 # Length of sequence a
    a=[] # The sequence we need as answer
    if n==1:
        print(1)
        print(b[0])
        continue
    a.append(b[0])
    for i in range(1,n):
        if b[i]>=b[i-1]: #Greater than equals to ka condition lagana bhool gya tha lol
            a.append(b[i])
        else:
            a.append(1)
            a.append(b[i])
    print(len(a))
    print(*a)#TLE de rha hai verna
