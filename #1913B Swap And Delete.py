import sys
t=int(sys.stdin.readline())
for x in range(t):
    s=sys.stdin.readline().strip()
    count0,count1,rem=0,0,0
    if len(s)==1:
        print(1)
        continue
    '''for i in range(len(s)):
        if s[i]=='0':
            count0+=1
        elif s[i]=='1':    
            count1+=1
    print(abs(count1-count0))''' # Balancing logic doesn't apply here
    n=len(s)
    for i in range(n):
        if s[i]=='0':
            count0+=1
            #print(f"count of 0 is:{count0}")
        elif s[i]=='1':
            count1+=1
            #print(f"count of 1 is:{count1}")
    if count0==count1:
        print(0)
        continue 
    for i in range(0,n):
        if s[i]=='0':
            if count1>0:
                count1-=1
            else:
                rem=n-i
                break
        if s[i]=='1':
            if count0>0:
                count0-=1
            else:
                rem=n-i
                break
    print(rem)