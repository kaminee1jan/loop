a=int(input("enter the number"))
i=1
c=0
while i>0:
    if i%2!=0:
        print(i,"odd number")
        c=c+1
        if c==a:
            break
    i=i+1
        