import sys
t=int(sys.stdin.readline())
for x in range(t):
    k=int(sys.stdin.readline())
    c=list(map(int,sys.stdin.readline().split()))
    count=0
    count_op=0
    flag=False
    for i in range(len(c)):
        if c[i]>=2:
            count+=1
        if i>0 and c[i]!=c[i-1]:
            count_op+=1
        if  c[i]>=3: #Error here in previous submission
            print("YES")
            flag=True
            break
        elif count>=2:
            print("YES")
            flag=True
            break
    if flag==False:
        print("NO")
           
        
            