import sys
n=int(sys.stdin.readline())
for x in range(n):
    length=sys.stdin.readline()
    arr=list(map(int,sys.stdin.readline().split()))
    max_count=0
    temp_count=0
    for i in range(len(arr)):
        if arr[i]==0:
            temp_count+=1
        if max_count<temp_count:
            max_count=temp_count
        if arr[i]==1:
            temp_count=0
    print(max_count)