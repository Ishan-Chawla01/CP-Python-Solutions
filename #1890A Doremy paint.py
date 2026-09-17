import sys
n=int(sys.stdin.readline())# Number of test cases
for x in range(n):
    p=int(sys.stdin.readline())# Number of elements in the permutation
    arr=list(map(int,sys.stdin.readline().split()))# Stored permutation in the array
    #Case when all values are same
    
    temp_nums=[]
    #Checking types of values in permutation
    for i in range(p):
        if arr[i] not in temp_nums:
            temp_nums.append(arr[i])
    #If there are more than 2 types of values, then it is not possible to paint the permutation
    if len(temp_nums)>2:    
        print("NO") 
    elif len(temp_nums)==1:
        print("YES")
    else:
        #Checking if one of number of type of any one value is n//2
        count, counter=0,0
        for i in range(p):
            if arr[i]==temp_nums[0]:
                count+=1
            else:
                counter+=1
        if count==p//2 or counter==p//2:
            print("YES")
        else:
            print("NO")
