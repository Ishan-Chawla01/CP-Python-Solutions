#At 8:40, came here at 8:11
import sys
from collections import Counter
t=int(sys.stdin.readline())
for x in range(t):
    n=int(sys.stdin.readline())
    a=list(map(int,sys.stdin.readline().split()))
    d=Counter(a)
    deck=[[i,d[i]] for i in d]
    deck.sort(key=lambda x:x[0])
    health=0
    #print(deck)
    max_dmg=0
    flag=True
    prev=0
    for dmg, number in deck:
        
        if number>0:
            health+=dmg
        

