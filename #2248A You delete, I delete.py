import sys
t=int(sys.stdin.readline())
ans=[]
for x in range(t):
    a=""
    flag_0=False
    flag_1=False
    s=sys.stdin.readline().strip()
    #Very easy, but how could I not solve it in the contest?!?!
    index_0,index_1=0,0
    for i in range(len(s)):
        if s[i]=='0' and not flag_0:
            index_0=i
            flag_0=True
        if s[i]=='1' and not flag_1:
            index_1=i
            flag_1=True
        if flag_1 and flag_0:
            break
    
    for i in range(len(s)):
        #print(f"index_0{index_0}")
        #print(f"index_1{index_1}")
        if i!= index_0 and i!=index_1:
            a+=s[i]
         #   print(f"i is {i}")
    print(a)