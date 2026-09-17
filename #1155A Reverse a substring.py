#LOL, EASIEST 1000 rated ever...
import sys
n=int(sys.stdin.readline())
s=sys.stdin.readline()
flag=False
for i in range(n-1):
    if ord(s[i])>ord(s[i+1]):
        print("YES")
        flag=True
        print(f"{i+1} {i+2}")
        break
if not (flag):
    print("NO") 