num = 2
while(num <=100):
    count = 0
    i = 2
    while(i < num):
        if(num % i == 0):
            count = count + 1
            break
        i = i + 1
    if (count == 0):
        print(num)
    num = num + 1
    a=num
 
