num= int(input('enter the number'))  
n = num
sum=0
while num > 0:
    a= num%10
    sum=sum+a
    num=num//10
if n%sum ==0:
    print(n," is a harshad number")
else:  
    print(n," is not a harshad number")