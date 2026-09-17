import sys
num=int(sys.stdin.readline())
for x in range(num):
    n,k=map(int,sys.stdin.readline().split())
    s=sys.stdin.readline()
    flag=True
    
    #print(f"N-K is{n-k}")
    '''for i in range(0,n-k):
        if (s[i]=='1' and s[i+k]=='1') or(s[i]=='0' and s[i+k]=='0'):
     #       print(s[i])
      #      print(s[i+k])
            continue
        else:
            flag=False
            break'''
    for beg in range(k):
        count=0
        for i in range(beg,n,k):
            if s[i]=='1':
                count+=1
        if count%2!=0:
            print("NO")
            flag=False
            break
    if flag==True:
        print("YES")    
