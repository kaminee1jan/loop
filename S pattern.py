r=0
while r<=6:
    c=0
    while c<=3:
        if (c==0) and (r!=0 and r!=0 and r!=3 and r!=4 and r!=5) or (c==1 or c==2) and(r!=1 and r!=2 and r!=4 and r!=5) or (c==3) and (r!=1 and r!=2 and r!=3 and r!=6):           
            print("*",end =" ")
        else:
            print(" ",end=" ")
        c=c+1
    print()
    r=r+1