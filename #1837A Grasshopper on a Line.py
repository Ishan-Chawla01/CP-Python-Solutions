import sys

# Number of test cases
n = int(sys.stdin.readline())

# Loop through each test case
for _ in range(n):
    x, k = map(int, sys.stdin.readline().split())
    
    # Case 1: If x is NOT divisible by k
    # This automatically covers your "x < k" scenario and "x > k where x % k != 0"
    if x % k != 0:
        print(1)
        print(x)
        
    # Case 2: If x IS divisible by k (which means x >= k)
    else:
        # We split x into two jumps: (x - 1) and 1
        # Since x is a multiple of k, (x - 1) will never be a multiple of k.
        # Since k >= 2, 1 is never a multiple of k.
        step1 = x - 1
        step2 = 1
        
        print(2)
        print(f"{step1} {step2}")