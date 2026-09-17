import sys
y,w=map(int,sys.stdin.readline().split())
m=max(y,w)
if ((7-m)/6)==1:
    print("1/1")
elif 7-m==2:
    print("1/3")
elif 7-m==3: print("1/2")
elif 7-m==4: print("2/3")
elif 7-m==5: print("5/6")
else: print("1/6")

