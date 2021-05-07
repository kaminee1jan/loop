r=0
while r<=6:
    c=0
    while c<=3:
        if (c==0) or (r==0) and (c==1 or c==2 or c==3) or (r==3 or r==6):
            print("*",end =" ")
        else:
            print(" ",end=" ")
        c=c+1
    print()
    r=r+1