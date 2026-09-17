#Redo as this was translated by self after seeing the Cpp code, couldn't understand it despite the solution
import sys
t=int(sys.stdin.readline())
ans=[]
for x in range(t):
    a,b=map(int,sys.stdin.readline().split())
    xk,yk=map(int,sys.stdin.readline().split())
    xq,yq=map(int,sys.stdin.readline().split())
    pos_x=[-1,1,-1,1]
    pos_y=[-1,-1,1,1]
    pairs_k=set()
    pairs_q=set()
    for i in range(4):
        pairs_k.add((xk+pos_x[i]*a,yk+pos_y[i]*b))
        pairs_q.add((xq+pos_x[i]*a,yq+pos_y[i]*b))
        pairs_k.add((xk+pos_x[i]*b,yk+pos_y[i]*a))
        pairs_q.add((xq+pos_x[i]*b,yq+pos_y[i]*a))
    ans.append(len(pairs_k.intersection(pairs_q)))
print(*ans)
                