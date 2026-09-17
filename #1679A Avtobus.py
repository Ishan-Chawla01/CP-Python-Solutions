import sys
t=int(sys.stdin.readline())
for x in range(t):
    n=int(sys.stdin.readline())
    if n%2!=0 or n<4:
        print(-1)
        continue
    else:
        val4,val6,minn,maxx=0,0,0,0
        if n%4==0:
            val4=n//4
            maxx=val4
        if n%6==0:
            val6=n//6            
            minn=val6
        if maxx!=0 and minn!=0:
            print(f"{minn} {maxx}")
            continue
        #maxx cars
        val6=0
        val4=n//4
        while val4*4+val6*6!=n and val4>=0:
            val4-=1
            val6+=1
        maxx=val4+val6
        #minn cars
        #From here a bit of AI advise ahs been used as I was unable to get the reason for error
        rem=n%6
        val4=0
        val6=n//6
        if rem!=0:
            if rem%4==0:
                val4+=rem//4
            else:
                val6-=1
                val4+=(rem+6)//4 #Note this... We need to start such that val4 starts by covering remainder left after val6 and not randomly at 0, but why?
        minn=val4+val6
        '''while val4*4+val6*6!=n and val6>=0:
            val6-=1
            val4+=2
        minn=val4+val6'''
        print(f"{minn} {maxx}")