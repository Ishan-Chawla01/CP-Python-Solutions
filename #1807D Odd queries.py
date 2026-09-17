import itertools
import sys
#ans=[]
t=int(sys.stdin.readline())
for x in range(t):
    n,q=map(int,sys.stdin.readline().split())
    a=list(map(int,sys.stdin.readline().split()))
    prefix_sum=list(itertools.accumulate(a))
    for _ in range(q):
        
        l,r,k=map(int,sys.stdin.readline().split())
        #GOT TLE on test 6
        '''if k%2==0:
            count_odd=0
        else:
            count_odd=r-l+1
        for i in range(l-1): #had made an indexing error, taken l here
            if a[i]%2!=0:
                count_odd+=1
        for i in range(r,n): #another one here, had taken r+1 here.
            if a[i]%2!=0:
                count_odd+=1
        if count_odd%2!=0:
            ans.append("YES")
        else:
            ans.append("NO")'''
        #Relying on editorial to calculate prefix sum and solve based on that
        right_part = prefix_sum[r - 1]
        left_part = prefix_sum[l - 2] if l > 1 else 0
        
        original_range_sum = right_part - left_part
        replaced_range_sum = (r - l + 1) * k
        
        current_sum = prefix_sum[-1] - original_range_sum + replaced_range_sum
        if current_sum%2!=0:
            print("YES")
        else:
            print("NO")

#print(*ans)