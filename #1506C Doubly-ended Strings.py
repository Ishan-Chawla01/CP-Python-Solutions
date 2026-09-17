import sys
t=int(sys.stdin.readline())
for x in range(t):
    max_count=0
    count=0
    a=sys.stdin.readline().strip()
    b=sys.stdin.readline().strip()

    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]==b[j]:
                for k in range(min(len(a),len(b))):
                    if i+k>=len(a) or j+k>=len(b):
                        break
                    if a[i+k]==b[j+k]:
                        count+=1
                    else:
                        break
                if count>max_count:
                    max_count=count
                count=0
    print(len(a)+len(b)-2*max_count)
