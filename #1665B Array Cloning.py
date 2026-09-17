import sys
from collections import Counter
a=sys.stdin.read()
t=int(sys.stdin.readline())
for x in range(t):
    n=int(sys.stdin.readline())
    a=list(map(int,sys.stdin.readline().split()))
    #Found for array length greater than 2 it is taking m+2 deistint operations where m is the number of distinct elements of the array.
    '''a1=set(a)
    if len(a1)==2:
        print(len(a1))
        continue
    elif len(a1)==1:
        print(0)
        continue'''
    # The simulation gives TLE on Test case 16     
    #Done by simulation, by self 100% no AI
    operations=0
    counter=Counter(a)
    maxx=max(counter.values())
    count=maxx
    while maxx<n:
        #Tryna optimise after seeing editorial
        d=min(n-maxx,maxx)
        operations+=1+d
        maxx+=d
        #Simulation works but igves TLE
        '''while temp>0 and count<n:
            count+=1
            temp-=1
            operations+=1
        maxx=maxx_new'''
    print(operations)
    
