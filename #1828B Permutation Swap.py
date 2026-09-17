#Reise! Its a very that sort of problem.
import sys
import math
#Learnt this
fin_ans=[]
from functools import reduce
t=int(sys.stdin.readline())
for x in range(t):
    arr=[]
    n=int(sys.stdin.readline())
    p=list(map(int,sys.stdin.readline().split()))
    for i,val in enumerate(p):
        arr.append(abs(val-i-1))
    ans=reduce(math.gcd,arr)
    fin_ans.append(ans)
print(*fin_ans)