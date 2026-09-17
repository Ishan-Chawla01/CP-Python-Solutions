import sys

t = int(sys.stdin.readline())
for x in range(t):
    s = sys.stdin.readline().strip()  
    count_a = 0
    temp = []
    for i in range(len(s)):
        if s[i] == '0' and count_a == 0:
            count_a += 1  
        else:
            temp.append(s[i])
            
    s_after_alice = "".join(temp)
    
    count_b = 0
    ans = []
    for i in range(len(s_after_alice)):
        if s_after_alice[i] == '1' and count_b == 0:
            count_b += 1  
        else:
            ans.append(s_after_alice[i])
            
    print("".join(ans))