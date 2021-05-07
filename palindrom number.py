n=int(input('enter the number'))
a=n
rev=0
while n>0:
	rev=rev*10+(n%10)
	n=n//10
if a==rev:
	print('palindrom number')
else:
	print('palindrom number nhi')