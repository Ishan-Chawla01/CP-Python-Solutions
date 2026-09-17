#also implemented a custom judge for this constructive algorithm problem.
'''def checker(a:list):
    n=len(a)
    chk=[]
    for i in range(n):
        if a[i]-i in set(chk):
            return False
        else:
            chk.append(a[i]-i)
    return True
import sys
t=int(sys.stdin.readline())
for x in range(t):
    n=int(sys.stdin.readline())
    a=list(map(int,sys.stdin.readline().split()))
    if checker(a):
        print(*a)
        continue
    if n==1:
        print(a[0])
        continue
    if n==2:
        print(f"{a[1]} {a[0]}")
        continue
    tmp=a.pop()
    a.insert(0,tmp)
    tmp=a.pop()
    a.insert(0,tmp)
    print(*a)
    #print(checker(a))
'''
# wtf how did I not realize that?!?!
def checker(a:list): #I initially did this using lists which was taking o(n^2) time in the checker too
    n=len(a)
    chk=set()
    for i in range(n):
        if a[i]-i in chk:
            return False
        else:
            chk.add(a[i]-i)
    return True
import sys
t=int(sys.stdin.readline())
for x in range(t):
    n=int(sys.stdin.readline())
    a=list(map(int,sys.stdin.readline().split()))
    a=sorted(a,reverse=True)
    print(*a)
