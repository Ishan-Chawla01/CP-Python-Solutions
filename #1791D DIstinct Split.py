#Done by self
import sys
from collections import defaultdict
for _ in range(int(input())):
    n=int(sys.stdin.readline())
    s=sys.stdin.readline().strip()
    freq_a=defaultdict(int)
    a=""
    b=""
    ans=set();ans1=set()
    for idx,char in enumerate(s):
        freq_a[char]+=1
        if freq_a[char]<2:
            a=a+char
        else:
            b=s[idx::]
            #print(b)
            break
    for char in a:
        if char not in ans:
            ans.add(char)
    for char in b:
        if char not in ans1:
            ans1.add(char)
    print(len(ans)+len(ans1))