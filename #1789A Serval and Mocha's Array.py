import sys
n=int(sys.stdin.readline())
for x in range(n):
    length=int(sys.stdin.readline())
    a=list(map(int,sys.stdin.readline().split()))
    flag=False
    # Take one nnumber, find its pair number if found break loop else continue second loop, of nothing for it, continue searching by incrementing first loop. always calculate if the gcd of both numbers is <=2, if yes, pair found, set flag to true and break, else keep searching, if nothing found after this o n^2 operation, let flag be false 
import sys
import math

n = int(sys.stdin.readline())
for x in range(n):
    length = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    flag = False
    
    # --- Implemented Comment Logic ---
    # Outer loop to pick the first number
    for i in range(length):
        # Inner loop to find its pair number
        for j in range(i + 1, length): 
            # Calculate if the gcd of both numbers is <= 2
            if math.gcd(a[i], a[j]) <= 2:
                flag = True
                break  # Break the inner loop
        
        if flag:
            break  # Break the outer loop since a pair was found
            
    # You can now use the 'flag' variable here (e.g., print "YES" or "NO")
    if flag:
        print("YES")
    else:
        print("NO")