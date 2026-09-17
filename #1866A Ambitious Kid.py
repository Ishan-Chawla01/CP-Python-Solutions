import sys
n=int(sys.stdin.readline()) # Number of test cases
l=list(map(int,sys.stdin.readline().split())) # finding input array
min=l[0]
for x in l:
    if abs(x)<abs(min):
        min=abs(x)
if(min>0):
    print(min)
else: print(min*-1)
