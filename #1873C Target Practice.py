import sys
n=int(sys.stdin.readline()) # Number of test cases
board=[[]]
# Hard coding the array
board=[[1,1,1,1,1,1,1,1,1,1],[1,2,2,2,2,2,2,2,2,1],[1,2,3,3,3,3,3,3,2,1],[1,2,3,4,4,4,4,3,2,1],[1,2,3,4,5,5,4,3,2,1],[1,2,3,4,5,5,4,3,2,1],[1,2,3,4,4,4,4,3,2,1],[1,2,3,3,3,3,3,3,2,1],[1,2,2,2,2,2,2,2,2,1],[1,1,1,1,1,1,1,1,1,1]]

for i in range(n): #For each test case
    demo_board=[]
    count=0
    for j in range(10):
        demo_board.append(sys.stdin.readline())
    for j in range(10):
        for k in range(10):
            if demo_board[j][k]=='X':
                count+=board[j][k]
    print(count)   
