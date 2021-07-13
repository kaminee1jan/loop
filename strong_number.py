num=int(input("enter the number"))
sum=0
n=num
while n>0:
    factorial=1
    i=1
    reminder=n%10
    while i<=reminder:
        factorial=factorial*i
        i=i+1
    print("\nfactorial of",reminder,"=",factorial)
    sum=sum+factorial
    n=n//10
print("sum of factorial of a given number",num,"=",sum)   
if sum==num:
    print("this is strong number","=",num)
else:
    print("this is not strong number","=",num)
    