import sys
n=int(sys.stdin.readline())
for x in range(n):
    string=sys.stdin.readline()
    s1="codeforces"
    count=0
    for i in range(len(s1)):
        if s1[i]!=string[i]:
            count+=1
    print(count) 