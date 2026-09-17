import sys
t=int(sys.stdin.readline())
for x in range(t):
    n=int(sys.stdin.readline())
    a=list(map(int,sys.stdin.readline().split()))
    last=a[-1]
    i=len(a)-2
    count=0
    '''while i>=0:
        if last>a[i]:
            last=a[i]
            i-=1
        elif a[i]>0: #not a[i]>1
            a[i]//=2
            count+=1
        if a[i+1]==0:#  not => 'if a[i]==1 and not(a[i]<last):'
            count=-1
            break
    print(count)'''
    '''last=a[-1]
        count=0
        #First element is gonna be< than  div by 2*(n-0), second be n-1
        i=0
        while i<n:
            if not (a[i]<last//(2*(n-i))):
                a[i]//=2
                count+=1
            else:
                i+=1
            if a[i]==1 and i!=0:
                count=-1
                break
        print(count)'''
    #after editorial
    while i>=0:
        while a[i]>=a[i+1] and a[i]>0:
            count+=1
            a[i]//=2
        if a[i]==a[i+1]:
            count=-1
            break
        i-=1
        if a[i]==a[i+1]:
            break
    print(count)
            