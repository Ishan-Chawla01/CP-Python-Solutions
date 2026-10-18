import sys
for _ in range(int(input())):
    n=int(sys.stdin.readline().strip())
    flag=True;cnt_2=0;cnt_3=0
    while n >1:
        if n%2==0:
            n//=2
            cnt_2+=1
        if n%3==0:
            n//=3
            cnt_3+=1
        if n%2!=0 and n%3!=0 and n>1:
            print(-1)
            flag=False
            break
    if flag==True:
        if not cnt_2>cnt_3:
            print(2*cnt_3-cnt_2)
        else:
            print(-1)
            