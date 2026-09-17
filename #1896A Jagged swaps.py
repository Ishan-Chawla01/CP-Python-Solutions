#1896A Jagged swaps
import sys

n=int(sys.stdin.readline())# Number of test cases
for x in range(n):
    p=int(sys.stdin.readline())# Number of elements in the permutation
    arr=list(map(int,sys.stdin.readline().split()))# The permutation
    if arr[0]==1:
        print("YES")
    else:    
        print("NO")