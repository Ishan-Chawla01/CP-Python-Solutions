#Got a trick fairly easily
import sys
for _ in range(int(input())):
    s=sys.stdin.readline().strip()
    cnt=cnt1=0
    for char in s:
        if char=='0':
            cnt+=1
        else:
            cnt1+=1
    if min(cnt,cnt1)%2!=0:
        print("DA")
    else:
        print("NET")
