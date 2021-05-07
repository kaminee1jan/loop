a=int(input('enter the number'))
b=int(input('enter the number'))
if a>b:
 num1=a
else:
 num1=b
while 1:
 if num1%a==0 and num1%b==0:
  print('lcm',num1)
  break
 num1=num1+1
 . 