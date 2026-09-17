import sys
t=int(sys.stdin.readline())
ans=[]
for x in range(t):
    n,m=map(int,sys.stdin.readline().split())
    a=sorted(list(map(int,sys.stdin.readline().split())))
    b=sorted(list(map(int,sys.stdin.readline().split())))
    '''j=0
    flag=True
    for i in range(len(a)):
        if not flag:
            flag=True
            continue
        if j>=len(b):
            break
        if i+1<len(a):
            #print(f"i{i},j{j}")
            if b[j]>a[i] and b[j]<a[i+1]:
                j+=1
                flag=False
            
                
                
    if j>=len(b):
        ans.append("yes")
    else:
        ans.append("no")
print(ans)'''
    #building from editorial
    #I never thought that the elements being appended to the original array could be used to form a group as well

    if not n>=2*m:
        print("NO")
        continue
    #Notice the simple brilliance over here!!
    #HW: Find out why it works
    i=0
    while i<m and a[i]<b[i] and b[i]<a[n-m+i]:
        i+=1
    if i<m:
        print("NO") #IF loop terminated due to any of the aboe conditions failing print false, brilliant! (for my newbie ass at least) 
    else:
        print("YES")#If loop terminated after completion (all m elements of b were traversed, that means they can be made equal to a, so true) 
