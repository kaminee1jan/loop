a=int(input("enter the number"))
i=1
c=1
while c<=a:
    j=1
    fac=0
    while j<=i:
        if i%j==0:
            fac=fac+1
        j=j+1
    if fac==2:
        c=c+1
        print(i)
    i=i+1
