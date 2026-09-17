import sys
import math
t=int(sys.stdin.readline())
ans=[]
for i in range(t):
    n,k,q=map(int,sys.stdin.readline().split())
    a=list(map(int,sys.stdin.readline().split()))
    i,j=0,0
    count=0
    while  j<n:# remove i<j or block
        if a[j]<=q:
            j+=1
        else:
            length=j-i
            if length>=k:
                count+=(length-k+1)*(length-k+2)//2
            j+=1
            i=j
    length = j - i
    if length >= k:
        count += (length - k + 1) * (length - k + 2) // 2
    '''while i < n:
            # If the starting day is invalid (too hot), move i forward
            if a[i] > q:
                i += 1
                continue
            
            # If the day is valid, use j to find where this valid block ends
            j = i
            while j < n and a[j] <= q:
                j += 1
            
            # We found a continuous valid block from index i to j-1
            length = j - i
            
            # If the block is long enough for a vacation (length >= k)
            if length >= k:
                # Number of ways to choose a subsegment of length >= k from a block of 'length'
                # Formula: (L - k + 1) * (L - k + 2) // 2
                count += (length - k + 1) * (length - k + 2) // 2
            
            # Move i to j to look for the next valid segment
            i = j'''
            
    ans.append(count)
print(*ans)