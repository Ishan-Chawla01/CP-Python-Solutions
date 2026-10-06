#By self by dry running on paper
import sys
for x in range(int(input())):
    n=int(sys.stdin.readline())
    a=list(map(int,sys.stdin.readline().strip().split()))
    ones=zeroes=0
    for num in a:
        if num==1:
            ones+=1
        elif num==0:
            zeroes+=1
    print(ones*2**zeroes)