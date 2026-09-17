import sys
t=int(sys.stdin.readline())
for x in range(t):
    n,p=map(int,sys.stdin.readline().split())
    a=list(map(int,sys.stdin.readline().split()))
    b=list(map(int,sys.stdin.readline().split()))
    c=[]
    for i in range(n):
        c.append((b[i],a[i]))
    c=sorted(c)# Sorted in min costs
    #print(c)
    tcost=0
    i=0
    tcost+=p
    n-=1
    while n>0:
        #print(f"tcost is{tcost}")
        '''tcost+=p
        n-=1
        if n==0:
            break''' #Here was mistake, SELF IDENIFIED, instead of making this guy talk to everyone when one person had informed others, others inform themselves
        people=c[i][1]
        if c[i][0]<p:
            #print("First if block entered")
            if people<=n:
                #print("Second if block entered")
                n-=people
                tcost+=c[i][0]*c[i][1]
                i+=1
            else:
                #print(f"c[i][0] {c[i][0]}")
                tcost+=c[i][0]*n
                break ## Added later with AI help, the only thing added with AI, to escape TLE
        else:
            tcost+=n*p
            break
    print(tcost)

