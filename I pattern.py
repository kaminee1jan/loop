r=0
while r<=5:
    c=0
    while c<=4:
        if (r==0 or c==2) or (r==5):
            print("*",end =" ")
        else:
            print(" ",end=" ")
        c=c+1
    print()
    r=r+1