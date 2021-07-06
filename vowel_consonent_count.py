vowel_count = 0  
consonent_count = 0 
i=0
str = input("enter the string")   
while i<len(str):   
    if str[i] in ("a","e","i","o","u"):  
        vowel_count = vowel_count + 1  
    elif str[i] >= "a" and str[i] <= "z":  
        consonent_count = consonent_count + 1 
    i=i+1
print("total number of vowel and consonant") 
print("vowel_count",vowel_count)  
print("consonent_count",consonent_count)