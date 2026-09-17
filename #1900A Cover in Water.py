import sys
num=int(sys.stdin.readline())
for x in range(num):
    n=int(sys.stdin.readline())
    s=sys.stdin.readline()
    count=0
    flag=True
    fin_count=0
    if '.' not in s:
        print("0")
        continue

    for i in range(n):
        if s[i]=='.':
            count+=1
        if count>2:
            print(2)
            flag=False
            break
        if s[i]=='#' or i==n-1:
            fin_count+=count
            count=0
    if flag:
        print(fin_count)


