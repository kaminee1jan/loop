r=0
while r<=6:
    c=0
    while c<=4:
        if (c==0 or c==4) or (r==1 and(c==1 or c==3)) or (r==2 and c==2):             
            print("*",end =" ")
        else:
            print(" ",end=" ")
        c=c+1
    print()
    r=r+1