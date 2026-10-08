import sys
from collections import defaultdict
for _ in range(int(input())):
    s=list(sys.stdin.readline().strip())
    d=defaultdict(int)
    if len(s)==2:
        if s[0]!=s[-1]:
            print("NO")
            continue
    vowels={"a","e","i","o","u"}
    for char in s:
        d[char]+=1
    odd_count=0
    flag1=True
    for key,value in d.items():
        if value%2!=0:
            odd_count+=1
        if odd_count==2:
            flag1=False
            break
        elif odd_count>0 and len(s)%2==0:
            flag1=False
            break
    if not flag1:
        print("NO")
        continue
    left,right=0,len(s)-1
    flag=False

    while left<=right:
        #print(f"right {right}")
        #print(f"left {left} right {right}")
        if s[left]==s[right]:
            left+=1;right-=1
            continue
        else:
            #print(f"left {left} right {right}")
            if (s[left]==s[right-1]) and (s[right] in vowels or s[right-1] in vowels):
                s[right],s[right-1]=s[right-1],s[right]
            elif (s[left+1]==s[right]) and (s[left] in vowels or s[left+1] in vowels):
                s[left],s[left+1]=s[left+1],s[left]
            elif (s[left+1]==s[right-1]) and( (s[left] in vowels or s[left+1] in vowels) and (s[right] in vowels or s[right-1] in vowels)):
                s[left],s[left+1]=s[left+1],s[left]
                s[right],s[right-1]=s[right-1],s[right]
            else:
                print("NO")
                flag=True
                break
            left+=1;right-=1
    if not flag:
        print("YES")
    
