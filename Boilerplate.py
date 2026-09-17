import sys
import statistics
num=int(sys.stdin.readline()) # Number of test cases

for x in range(num):
    ans=""
    n=int(sys.stdin.readline()) #Height of frosting at ith position
    frosting=list(map(int,sys.stdin.readline().split())) #Frosting array
    cum_avg=[]
    sum=0
    for i in range(n):
        sum += frosting[i]
        avg = sum // (i + 1)
        cum_avg.append(avg)
    for i in range(n-1):
        if cum_avg[i] < cum_avg[i+1]:
            cum_avg[i+1]=cum_avg[i]
    print(" ".join(map(str, cum_avg)))