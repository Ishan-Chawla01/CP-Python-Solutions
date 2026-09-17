import sys
n=int(sys.stdin.readline())# Number of test cases
for _ in range(n):
    len_a=int(sys.stdin.readline())#Length of array a
    a=list(map(int,sys.stdin.readline().split()))
    b,c,=[],[]
    a=sorted(a)
    if(a[0]==a[-1]):
        print(-1)
        continue
    i=0
    while(a[i]==a[0]):
        i+=1
    print(f"{i} {len_a-i}")
    print(*a[:i])
    print(*a[i:])
## HOW DID IT GET ACCEPTED< I DON'T KNOW
    #print(f"A is: {a}")#redactable
    product_ini=1
    for x in set(a):
        product_ini*=x
    for i in range(0,len_a):
        #print(f"Element of 'a' chosen is:{a[i]}")#redactbale
        pro_new=product_ini//a[i]
        #print(f"New product is: {pro_new}")
        if pro_new%a[i]!=0:
            c.append(a[i])
            #print(f"Appending {a[i]} to c")#redactbale
        else:
            #print(f"Appending {a[i]} to b")#redactbale
            b.append(a[i])
        if(product_ini%a[i]==0):
            product_ini//=a[i]
    len_b,len_c=len(b),len(c)
    if(len_b==0):
        print ("-1")
        continue
    else:
        ##print("length of b and c is:"+str(len_b)+" "+str(len_c))
        #print("Array b is:")
        print(str(len_b)+" "+str(len_c))
        print(*b)
        #print("Array c is:")
        print(*c)
