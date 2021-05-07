n=int(input('enter the number'))
sum=0
l=len(str(n))
copy_n=n
while n>0:
 digit=n%10
 sum=sum+digit**l
 n=n//10
if sum==copy_n:
 print('amstorng number')
else:
 print('not amstorng number)