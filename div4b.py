import sys
n=int(sys.stdin.readline())
for x in range(n):
    num=int(sys.stdin.readline())#Length of string
    string=sys.stdin.readline().strip()
    max_len=0
    temp_len=0
    for i in range(num):
        
        if string[i]=='1':
            temp_len=0
            continue
        elif string[i]=='0':
            temp_len+=1
            #print(f"temp len {temp_len} max_len {max_len}")
        if temp_len>max_len:
            max_len=temp_len
            #print(f"Upon comparison: temp len {temp_len} max_len {max_len}")
    print(max_len)
