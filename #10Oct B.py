#By slef entirely
import sys
for _ in range(int(input())):
    n=int(sys.stdin.readline())
    s=list(sys.stdin.readline().strip())
    k=0
    arr=[]
    stack=[]
    docs=[]
    for idx in range(len(s)):
        if s[idx]=='1':
            stack.append(idx+1)
            k+=1
        elif s[idx]=='2':
            if not stack:
                continue
            else:
                stack.pop()
                k-=1
                docs.append(idx+1)
                k+=1
        else: continue
        #print(stack)
        #print(docs)
    print(k)
    if k!=0:
        stack=set(sorted(stack+docs))
        print(*stack)
    else:
        print()