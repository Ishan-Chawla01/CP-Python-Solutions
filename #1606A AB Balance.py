#Wow, seemed easy today, but hadn't when I had done before, BTW< again, all me, no AI
import sys
for x in range(int(input())):
    s=list(sys.stdin.readline())
    count_ab,count_ba=0,0
    for i in range(len(s)-1):
        if s[i]+s[i+1]=="ab":
            count_ab+=1
        elif s[i]+s[i+1]=="ba":
            count_ba+=1
    if count_ab==count_ba:
            print("".join(s))
            continue
    for i in range(len(s)-1):
        #Writing logic here if ab>ba, then then and there break the thing
        if count_ab>count_ba:
            s[i]="b" #Notice why can't we change i+1 > cause it can make ab, after at i and i+1 if you change it to a and that can violate the minimum condition asked by the problem
            count_ab-=1
        elif count_ba>count_ab:
            s[i]="a"
            count_ba-=1
    if count_ab==count_ba:
        print("".join(s))