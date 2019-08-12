num6 = int(input(" "))

if num6 > 1: 
      
  
   for i in range(2, num6//2): 
         
       
       if (num6 % i) == 0: 
           print("no") 
           break
   else: 
       print("yes") 
  
else: 
   print("no") 
