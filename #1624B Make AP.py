#So close yet so far...
#why didn't I build a mathematical formula ywrr...
import sys
for x in range(int(input())):
    a,b,c=map(int,sys.stdin.readline().split())
    #ans="NO"
    '''if 2*b>a+c:
        m=1
        while m*a+c<=2*b or m*c+a<=2*b:
            
            if m*a+c==2*b or m*c+a==2*b:
                ans="YES"
                break
            m+=1
    elif 2*b<a+c:
        m=1
        while 2*b*m<=a+c:
            if 2*b*m==a+c:
                ans="YES"
                break
            m+=1
    else:
        ans="YES"'''
    if (2*b-c)%a==0 and 2*b-c>0:
        print("YES") #First, when doing m*a and seeing if m is an integer
    elif(2*b-a)%c==0 and 2*b-a>0:
        print("YES") #Second, doing m*c
    elif (a+c)%(2*b)==0 and a+c>0:#Third, scaling b
        print("YES")
    else:
        print("NO")        
    #print(ans)
        