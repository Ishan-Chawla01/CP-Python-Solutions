#Notice that a&b is always <=min(a,b) AND!! since the final element in arbitrary range, is going to be operated and changed acc to first element
#Of range, every element can be swapped with minimum of array, hence giving a global minimum
#After seeing a solution from a specialist
import sys
for _ in range(int(input())):
    n=int(sys.stdin.readline())
    a=list(map(int,sys.stdin.readline().strip().split()))
    x=min(a)
    res=float('inf')
    for num in a:
        res=min(num & x,res)
    print(res)
    