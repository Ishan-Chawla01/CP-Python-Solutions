from collections import Counter
for x in range(int(input())):
    a=int(input()); b=max(Counter(input().split()).values()); summ=a-b
    while a>b: summ+=1;b*=2
    print(summ)