import sys
for _ in range(int(input())):
    s=sys.stdin.readline().strip()
    d={"1":0,"0":0}
    for i in range(len(s)):
        d[s[i]]+=1
    if d['0']==d['1']:
        print(0)
        continue
    for i in range(len(s)):
        if s[i]=="1" and d["0"]>0:
            d['0']-=1
        elif s[i]=="0" and d["1"]>0:
            d['1']-=1
        else:
            print(len(s)-i)
            break
        