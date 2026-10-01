#Done by self, very easy
import sys
for x in range(int(input())):
    n=int(sys.stdin.readline())
    s=list(map(int,sys.stdin.readline().split()))
    s.sort()
    i=0
    pairs=0
    while i<n-1:
        if s[i]==s[i+1] or s[i]+1==s[i+1]:
            pairs+=1
            i+=1
        i+=1
    print(pairs)