import sys
num=int(sys.stdin.readline())
for y in range(num):
    n,x=map(int,sys.stdin.readline().split())
    a=list(map(int,sys.stdin.readline().split()))
    max_dist=0
    a.append(x)
    #print(a)
    for i in range(0,n):
        if i==0:
            max_dist=a[0]
        else:
            max_dist=max(a[i]-a[i-1],max_dist)
            #print(f"current max is:{max_dist}")
    if max_dist> (a[n]-a[n-1])*2:
        print(max_dist)
    else:
        #print(f" printed maximum{(a[n]-a[n-1])*2}")
        print(f"{(a[n]-a[n-1])*2}")
# The only mistake was the range( you can't execute the loop till n-1 as on doing that for only 1 element, the loop will never run.)
''''''#2 5'''
#'''#1 4''''''wrong answer 20th numbers differ - expected: '3', found: '2'''
