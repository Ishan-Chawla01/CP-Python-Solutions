import sys
import statistics
num=int(sys.stdin.readline()) # Number of test cases

for x in range(num):
    count=0
    less=0
    n=int(sys.stdin.readline()) #The number of friends alice has
    location=list(map(int,sys.stdin.readline().split()))#Location of her friends
    location=sorted(location)
    median=statistics.median(location)
    for x in range(len(location)):
        if location[x]<median:
            less+=1
        elif location[x]>median:
            count+=1
    ans=max(less,count)
    print(ans)
