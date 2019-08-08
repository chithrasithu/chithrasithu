num = int(input(""))

sum = 0

if num <= 0: 
   print("") 
else: 
   while num > 0:
        sum = sum + num
        num = num - 1;
    # displaying output
   print(sum)
