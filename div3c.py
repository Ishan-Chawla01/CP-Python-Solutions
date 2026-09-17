import sys
num=int(sys.stdin.readline())
for x in range(num):
    count=0
    a,b,x=map(int,sys.stdin.readline().split())
    a1,b1=a,b
    while(a1!=b1):
        if(a1>b1):
            a1+=1
            b1//=x
            count+=1
        else:
            b1+=1
            a1//=x
            count+=1
    print(count)
'''from collections import deque

def min_operations(a, b, x):
    # If they are already equal, 0 operations are needed
    if a == b:
        return 0
        
    # If x is 1, dividing does nothing but stall. 
    # The only useful operation is adding 1 to the smaller number.
    if x == 1:
        return abs(a - b)

    max_limit = max(a, b) + 1

    def get_distances(start):
        # dict to store {number: min_operations_to_reach_it}
        dist = {start: 0}
        queue = deque([start])
        
        while queue:
            curr = queue.popleft()
            current_dist = dist[curr]
            
            # Option 1: Add 1
            nxt_add = curr + 1
            if nxt_add <= max_limit and nxt_add not in dist:
                dist[nxt_add] = current_dist + 1
                queue.append(nxt_add)
                
            # Option 2: Divide by x
            nxt_div = curr // x
            if nxt_div not in dist:
                dist[nxt_div] = current_dist + 1
                queue.append(nxt_div)
                
        return dist

    # Find all reachable states and distances from both a and b
    dist_a = get_distances(a)
    dist_b = get_distances(b)

    # Find the intersection state `v` that minimizes (dist_a[v] + dist_b[v])
    min_total_ops = float('inf')
    
    for node in dist_a:
        if node in dist_b:
            min_total_ops = min(min_total_ops, dist_a[node] + dist_b[node])
            
    return min_total_ops

# Example Usage:
# print(min_operations(5, 14, 3))'''