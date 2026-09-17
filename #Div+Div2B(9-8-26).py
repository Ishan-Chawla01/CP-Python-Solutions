'''import sys

t = int(sys.stdin.readline())
mod = 998244353

for x in range(t):
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    count = 0
    flag=True
    if "0" not in s and "1" not in s:
        print(2**len(s) if n > 1 else 2)
        continue
    elif "?" not in s:
        
        flag = True
        for i in range(n - 2):
            if s[i] == s[i + 2]:
                flag = False
                break
        print(1 if flag else 0)
        continue
    for i in range(n-2):
        if s[i]=='?' and s[i+2]!='?':
            count+=2
        else:
            count+=1
        if s[i]==s[i+2] and s[i]!='?':
            count=0
            flag=False
            print(count)
            break
    if flag:
        print((count-1)%mod)'''
import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    ans = 0
    for a in range(2):
        for b in range(2):
            ok = True
            for i in range(n):
                if i % 2 == 0:
                    expected = a ^ ((i // 2) & 1)
                else:
                    expected = b ^ ((i // 2) & 1)
                if s[i] != '?' and int(s[i]) != expected:
                    ok = False
                    break
            ans += ok
    print(ans)